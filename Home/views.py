from .models import User, TargetPlan
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, TargetPlanSerializer
import uuid
import random
from .funtions import send_email_otp
import os
from django.contrib.auth.hashers import check_password
# Create your views here.

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    print(email, password)
    if not email or not password:
        return Response({'error': 'Email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)
    user = User.objects.filter(email=email).first()
    if user is None:
        return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
    if check_password(password, user.password):
        if not user.is_verified:
            user.otp = str(random.randint(100000, 999999))
            user.save()
            send_email_otp(email, user.otp)
            return Response({'message': 'OTP sent successfully.'}, status=status.HTTP_200_OK)
        
        user.temp_access_token = str(uuid.uuid4())
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['POST'])
def signup(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if not email or not password:
        return Response({'error': 'Email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)
    user = User.objects.filter(email=email).first()
    if user:
        return Response({'error': 'User already exists.'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create(email=email,username=email)
    # user.otp = str(random.randint(100000, 999999))
    user.set_password(password)
    user.is_verified = False
    user.save()
    # # send_email_otp(user, user.otp)
    serializer = UserSerializer(user)
    return Response({'message': 'User created successfully.','data':serializer.data}, status=status.HTTP_201_CREATED)
    
    
@api_view(['POST'])
def verify(request):
    email = request.data.get('email')
    otp = request.data.get('otp')
    if not email or not otp:
        return Response({'error': 'Email and OTP are required.'}, status=status.HTTP_400_BAD_REQUEST)
    user = User.objects.filter(email=email).first()
    if not user:
        return Response({'error': 'User does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
    if user.otp != otp:
        return Response({'error': 'Invalid OTP.'}, status=status.HTTP_400_BAD_REQUEST)
    user.is_verified = True
    user.temp_access_token= str(uuid.uuid4())
    user.save()
    
    serializer = UserSerializer(user)
    serializer.data['message'] = 'User verified successfully.'
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def target_plan(request):
    serializer = TargetPlanSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




from django.http import JsonResponse
from lyzr_agent_api.models.chat import ChatRequest
from rest_framework.decorators import api_view
from .models import TargetPlan
from .aiagent import Create_env
import os
from lyzr_agent_api.client import AgentAPI

# Initialize the AgentAPI client
client = AgentAPI(x_api_key=os.getenv('LYZR_API_KEY'))
# agent_id = Create_env()  # Create environment and agent dynamically
agent_id = "6742ee3d61f92e3cfef00428"
@api_view(['POST'])
def portfolio_advice(request):
    try:
        # Ensure the session is initialized
        request.session['init'] = True

        # Fetch user input and requirements from DB
        user_input = request.data.get('user_input')
        user_id = str(request.data.get('user'))

        # Retrieve user-specific TargetPlan
        target_plan = TargetPlan.objects.order_by('-id').filter(user__id=user_id).first()
        if not target_plan:
            return JsonResponse({'error': 'No Target Plan found for the user.'}, status=404)

        # Prepare the requirements to send to the AI agent
        user_requirements = {
            "risk_tolerance": target_plan.risk_tolerance,
            "financial_goals": target_plan.financial_goals,
            "timeline": target_plan.timeline,
            "investment_type": target_plan.investment_type,
            "investment_amount": str(target_plan.investment_amount),
            "age": target_plan.age,
            "savings": str(target_plan.savings),
            "current_investments": target_plan.current_investments,
            "investment_experience": target_plan.investment_experience,
            "health_status": target_plan.health_status,
            "dependents": target_plan.dependents,
            "liquidity_needs": target_plan.liquidity_needs,
            "esg_preferences": target_plan.esg_preferences,
        }

        # Combine user input with requirements for a detailed AI request
        message = f"User Query: {user_input}\nUser Information: {user_requirements}"

        # Create a chat request
        chat_request = ChatRequest(
            user_id=user_id,
            agent_id=agent_id,
            message=message,
            session_id=request.session.session_key,
        )

        # Send the request to the agent
        response = client.create_chat_task(json_body=chat_request)

        # Check the task's status to retrieve the response
        task_status = client.get_task_status(task_id=response.task_id)
        if task_status.status == 'completed':
            advisor_response = task_status.result['response']
        else:
            advisor_response = "I'm currently processing your request. Please wait a moment."

        return JsonResponse({'task_id': response.task_id, 'response': advisor_response})

    except Exception as e:
        print(f"Error: {e}")
        return JsonResponse({'error': str(e)}, status=500)


import os
from groq import Groq
from django.http import JsonResponse
from rest_framework.decorators import api_view
import json

# Initialize the Groq client
groq_client = Groq(api_key=os.getenv('GROQ_API_KEY'))
import json

def formate_response(response_text):
    """
    Use Groq's LLM to format the response text.
    """
    try:
        # Define the messages for the chat completion
        messages = [
            {
                "role": "system",
                "content": (
                    "You are a highly knowledgeable Financial Portfolio Advisor Agent. "
                    "Users will provide their financial data. Your role is to:\n"
                    "1. Analyze the provided data thoroughly.\n"
                    "2. Suggest a well-structured and diversified investment portfolio tailored to the user's goals and risk tolerance.\n"
                    "3. Provide your response in a **JSON format** with the following keys:\n"
                    "   - **risk:** Overview of the user's risk tolerance and how it impacts the portfolio.\n"
                    "   - **stocks:** List of stock recommendations, with each stock including:\n"
                    "     - **name:** Name of the stock.\n"
                    "     - **allocation:** Percentage (%) of the total portfolio allocated to this stock.\n"
                    "     - **time_to_hold:** Suggested time to hold the stock before review or sale.\n"
                    "     - **target_price:** Target price for selling the stock, if applicable.\n"
                    "     - **stop_loss:** Stop-loss price for risk management, if applicable.\n"
                    "     - **reason:** Why this stock was chosen.\n"
                    "     - **risk:** Risks associated with this stock.\n"
                    "   - **uncontrollable_risks:** A description of uncontrollable market or external conditions that could impact the portfolio.\n"
                    "   - **strategies:** Actionable strategies to mitigate risks and adapt to uncontrollable conditions.\n"
                    "   - **additional_suggestions:** Additional financial advice or considerations.\n"
                    "4. Ensure the JSON response is well-structured and easy to read."
                    "5. Directly give JSON response without any additional text."
                )
            },
            {
                "role": "user",
                "content": response_text
            }
        ]

        # Send the messages to Groq's LLM
        chat_completion = groq_client.chat.completions.create(
            messages=messages,
            model="llama3-8b-8192",  # Replace with your specific model
            max_tokens=1500,
            temperature=0.5,
            top_p=0.9,
            n=1,
            stop=None
        )

        # Extract the formatted text from the response
        formatted_text = chat_completion.choices[0].message.content.strip()

        # Print the generated JSON for inspection
        print("Generated JSON:", formatted_text)

        # Parse the JSON string to a Python dictionary
        json_data = json.loads(formatted_text)

        # Serialize the dictionary back to a JSON string without newlines
        compact_json = json.dumps(json_data, separators=(',', ':'))

        return compact_json

    except json.JSONDecodeError as e:
        print(f"JSON decoding error: {e}")
        return None
    except Exception as e:
        print(f"Error formatting response: {e}")
        return None

@api_view(['POST'])
def retrive_chat(request):
    task_id = request.data.get('task_id')
    
    task_status = client.get_task_status(task_id=task_id)
    print(task_status)
    if task_status.status == 'completed':
        advisor_response = task_status.result['response']
        formatted_text = formate_response(advisor_response)
        if formatted_text is None:
            return JsonResponse({'error': 'Failed to format the response.'}, status=500)
    else:
        formatted_text = "I'm currently processing your request. Please wait a moment."
    
    return JsonResponse({'response': formatted_text})
