PortfolioPilor: Personalized AI-Powered Financial Portfolio Advisor

Overview
PortfolioPilor is an AI-powered financial portfolio advisor designed to provide personalized investment strategies for users based on their unique financial conditions, goals, and risk tolerance. The system combines:

Retrieval-Augmented Generation (RAG): Integrating pre-indexed knowledge with live, AI-powered reasoning.
Real-Time Web Search: For market trends, stock data, and financial news.
Conversational AI Agent: Using Lyzr's API for human-like interaction and personalized suggestions.
Features
🎯 Key Capabilities
Personalized Portfolio Recommendations:
Suggests stocks, mutual funds, or ETFs tailored to user profiles.
Real-Time Data Integration:
Uses APIs to fetch live market trends, stock prices, and news.
Explanations for Suggestions:
Explains why each recommendation aligns with the user’s goals and risk tolerance.
Conversational AI:
Responds to user queries with human-like explanations via Lyzr’s API.
🔍 Technologies Used
Backend Framework: Django
AI Integration: Lyzr API
Knowledge Base: LlamaIndex (RAG)
Web Search: Google Custom Search API
Financial Data: Yahoo Finance and Alpha Vantage APIs
Database: PostgreSQL
Project Architecture
plaintext
Copy code
├── PortfolioPilor/
│   ├── models.py        # Database models (User, Financial Profile, TargetPlan)
│   ├── views.py         # Django views for API endpoints
│   ├── serializers.py   # Data validation using DRF serializers
│   ├── rag.py           # RAG logic for retrieval and generation
│   ├── urls.py          # API route mappings
│   ├── llama_index.json # Pre-indexed financial knowledge base
├── README.md            # Hackathon project overview
└── manage.py            # Django management script
How It Works
User Profile Initialization:

Users provide their financial details like income, savings, risk tolerance, financial goals, and preferences.
Data Collection:

Real-time data is fetched from:
Yahoo Finance API for stock market updates.
Google Custom Search for market trends and news.
Knowledge Retrieval:

Pre-indexed financial documents (e.g., investment guides, stock analyses) are queried using LlamaIndex.
AI-Powered Suggestions:

Combines user profile, retrieved knowledge, and live market data to generate personalized investment recommendations.
Explanations:

Justifies each recommendation with reasoning, trends, and alignment to user goals using Lyzr's conversational API.
Endpoints
1. User Profile Management
Endpoint	Method	Description
/signup	POST	Register a new user
/login	POST	Authenticate a user
/verify	POST	Verify user via OTP
2. Portfolio Recommendation
Endpoint	Method	Description
/target-plan/	POST	Save user financial data
/portfolio-advice	POST	Generate personalized investment advice
Key Features in Detail
1. Retrieval-Augmented Generation (RAG)
Combines pre-indexed knowledge with live reasoning.
Built with LlamaIndex, enabling efficient retrieval from financial documents.
2. Web Search for Real-Time Data
Integrates Google Custom Search for:
Trending stock news.
Real-time market sentiment.
Enhances advice with fresh data.
3. Conversational AI
Uses Lyzr API to:
Engage users with human-like explanations.
Answer specific financial queries.
How to Run
Prerequisites
Python 3.10+
PostgreSQL
API Keys for:
Google Custom Search
Yahoo Finance / Alpha Vantage
Lyzr API
Setup
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/PortfolioPilor.git
cd PortfolioPilor
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Set up environment variables in .env:

env
Copy code
OPENAI_API_KEY=your_openai_key
GOOGLE_API_KEY=your_google_search_key
GOOGLE_CX=your_custom_search_id
DATABASE_URL=your_database_url
Run migrations:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Start the server:

bash
Copy code
python manage.py runserver
Sample Request
Portfolio Advice Request
Input:
json
Copy code
{
    "user_id": "d0dc379f-72a8-4e69-b586-247a89803137",
    "user_input": "What are the best stocks for retirement planning?"
}
Output:
json
Copy code
{
    "response": "Based on your moderate risk tolerance and savings, I recommend the following stocks: AAPL (Apple Inc.), MSFT (Microsoft), and VOO (Vanguard S&P 500 ETF). These align with your goals for long-term growth."
}
Why PortfolioPilor?
1. Personalized Advice
Every user is unique. PortfolioPilor ensures each suggestion is tailored to the user's financial profile and goals.

2. Transparent Explanations
We don't just suggest; we explain why a stock or fund is right for you.

3. Real-Time Accuracy
By integrating live market data and RAG, PortfolioPilor ensures up-to-date and relevant recommendations.

4. Hackathon-Ready Features
Built with modularity and scalability in mind, PortfolioPilor showcases cutting-edge tech like RAG, Lyzr, and web search.

Future Enhancements
Multi-Language Support: Expand accessibility to non-English speakers.
Advanced Analytics: Visualize portfolio performance over time.
Enhanced Data Sources: Integrate more financial APIs for deeper insights.
Contributors



HrithikHadawale - AI Engineer and Backend Developer
Pratik  Dhumal - Frontend Developer
Demo







