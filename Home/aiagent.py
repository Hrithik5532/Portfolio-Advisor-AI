


from lyzr_agent_api.client import AgentAPI
from lyzr_agent_api.models.environment import EnvironmentConfig, FeatureConfig
from lyzr_agent_api.models.agents import AgentConfig

from dotenv import load_dotenv
import os
load_dotenv()

def Create_env():

    # Initialize the Lyzr Agent API client
    client = AgentAPI(x_api_key=os.getenv('LYZR_API_KEY'))
    openai_api_key = os.getenv('OPENAI_API_KEY')


    # Configure the environment to use Groq's LLM
    environment_config = EnvironmentConfig(
        name="Portfolio Advisor Environment Latest",
        features=[
            FeatureConfig(
                type="SHORT_TERM_MEMORY",
                config={"max_tries": 3},
                priority=0,
            )
        ],
        tools=[],  # Provide an empty list if no tools are needed
        # llm_config={
        #     "provider": "groq",
        #     "model": "llama3-8b-8192",  # Replace with your specific model
        #     "config": {
        #         "temperature": 0.5,
        #         "top_p": 0.9,
        #     },
        #     "env": {
        #         "GROQ_API_KEY": os.getenv('GROQ_API_KEY')
        #     }
        # },
        llm_config={
            "provider": "openai",
        "model": "gpt-4o-mini",
            "config": {
                "temperature": 0.5,
                "top_p": 0.9,
            },
            "env": {
                "OPENAI_API_KEY": os.getenv('OPENAI_API_KEY')
            }
        },
    )


    # Create the environment
    environment = client.create_environment_endpoint(json_body=environment_config) 
    environment_id = environment['env_id']

    response = client.update_environment_endpoint(
        env_id=environment_id,
        json_body=environment_config,
    )
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$",response )
    client.get_environments_endpoint()

    # Configure the agent
    agent_config = AgentConfig(
        env_id=environment_id,
        system_prompt='''
        You are a highly knowledgeable Financial Portfolio Advisor Agent. Users will provide their financial data, requirements, and goals. Your role is to:
give stock or mutual fund or portfolio shortlist and financial advise.

*DO NOT include any extra text, commentary, or formatting. Return only JSON.*

*Example Response:*
```json
{
  "risk": {
    "level": "Moderate",
    "description": "A moderate risk tolerance balances growth potential and stability, focusing on a diversified portfolio to minimize volatility."
  },
  "stocks": [
    {
      "name": "HDFC Bank",
      "allocation": "20%",
      "time_to_hold": "5+ years",
      "target_price": "₹2,000",
      "stop_loss": "₹1,500",
      "reason": "Strong fundamentals, market leadership, and consistent performance.",
      "risk": "Limited upside potential in case of a downturn in the financial sector."
    }
  ],
  "uncontrollable_risks": {
    "market_volatility": "Fluctuations due to geopolitical events or economic downturns."
  },
  "strategies": {
    "diversification": "Spread investments across large-cap, mid-cap, small-cap stocks, and ETFs to reduce risk."
  },
  "additional_suggestions": {
    "tax_efficiency": "Consider tax-saving instruments like ELSS or NPS for additional benefits."
  }
}''',
        name="Portfolio Advisor Agent",
        agent_description="You are an expert Financial Portfolio Advisor Agent. Your primary responsibility is to analyze user profiles, suggest a JSON-formatted investment portfolio, and provide reasoning, risks, and actionable strategies. You include a breakdown of each recommendation with clear justifications and ensure the response is user-friendly for both technical and non-technical users.",
    )

    # Create the agent
    agent = client.create_agent_endpoint(json_body=agent_config)
    agent_id = agent['agent_id']

    response = client.update_agent_endpoint(
        agent_id=agent_id,
        json_body=agent_config
    )
    print("************************************",response )
    client.get_agents_endpoint()

    return agent_id