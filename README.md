# PortfolioPilor: Personalized AI-Powered Financial Portfolio Advisor

## Overview
PortfolioPilor is an AI-powered financial portfolio advisor designed to provide personalized investment strategies for users based on their unique financial conditions, goals, and risk tolerance. The system combines:

- **Retrieval-Augmented Generation (RAG)**: Integrating pre-indexed knowledge with live, AI-powered reasoning
- **Real-Time Web Search**: For market trends, stock data, and financial news
- **Conversational AI Agent**: Using Lyzr's API for human-like interaction and personalized suggestions

## Features

### 🎯 Key Capabilities
- **Personalized Portfolio Recommendations**:
    - Suggests stocks, mutual funds, or ETFs tailored to user profiles
- **Real-Time Data Integration**:
    - Uses APIs to fetch live market trends, stock prices, and news
- **Explanations for Suggestions**:
    - Explains why each recommendation aligns with the user's goals and risk tolerance
- **Conversational AI**:
    - Responds to user queries with human-like explanations via Lyzr's API

### 🔍 Technologies Used
- Backend Framework: Django
- AI Integration: Lyzr API
- Knowledge Base: LlamaIndex (RAG)
- Web Search: Google Custom Search API
- Financial Data: Yahoo Finance and Alpha Vantage APIs
- Database: PostgreSQL

## Project Architecture

├── PortfolioPilor/
│   ├── models.py        # Database models (User, Financial Profile, TargetPlan)
│   ├── views.py         # Django views for API endpoints
│   ├── serializers.py   # Data validation using DRF serializers
│   ├── rag.py          # RAG logic for retrieval and generation
│   ├── urls.py         # API route mappings
│   ├── llama_index.json # Pre-indexed financial knowledge base
├── README.md           # Hackathon project overview
└── manage.py          # Django management script


## How It Works
1. **User Profile Initialization**:
     - Users provide their financial details like income, savings, risk tolerance, financial goals, and preferences

2. **Data Collection**:
     - Real-time data is fetched from:
       - Yahoo Finance API for stock market updates
       - Google Custom Search for market trends and news

3. **Knowledge Retrieval**:
     - Pre-indexed financial documents are queried using LlamaIndex

4. **AI-Powered Suggestions**:
     - Combines user profile, retrieved knowledge, and live market data

5. **Explanations**:
     - Justifies each recommendation with reasoning, trends, and alignment to user goals

## API Endpoints

### 1. User Profile Management
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/signup` | POST | Register a new user |
| `/login` | POST | Authenticate a user |
| `/verify` | POST | Verify user via OTP |

### 2. Portfolio Recommendation
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/target-plan/` | POST | Save user financial data |
| `/portfolio-advice` | POST | Generate personalized investment advice |

## Setup and Installation

### Prerequisites
- Python 3.10+
- PostgreSQL
- API Keys for:
    - Google Custom Search
    - Yahoo Finance / Alpha Vantage
    - Lyzr API

### Installation Steps
1. Clone the repository:

git clone repo
cd PortfolioPilor


2. Install dependencies:

pip install -r requirements.txt


3. Set up environment variables in `.env`:

OPENAI_API_KEY=your_openai_key
GOOGLE_API_KEY=your_google_search_key
GOOGLE_CX=your_custom_search_id
DATABASE_URL=your_database_url


4. Run migrations:

python manage.py makemigrations
python manage.py migrate


5. Start the server:

python manage.py runserver


## Usage Example

### Portfolio Advice Request

// Input:
{
      "user_id": "d0dc379f-72a8-4e69-b586-247a89803137",
      "user_input": "What are the best stocks for retirement planning?"
}

// Output:
{
      "response": "Based on your moderate risk tolerance and savings, I recommend the following stocks: AAPL (Apple Inc.), MSFT (Microsoft), and VOO (Vanguard S&P 500 ETF). These align with your goals for long-term growth."
}


## Key Features

### 1. Personalized Advice
- Every user is unique
- Tailored suggestions based on financial profile and goals

### 2. Transparent Explanations
- Detailed reasoning for each recommendation

### 3. Real-Time Accuracy
- Integration with live market data and RAG

### 4. Hackathon-Ready Features
- Built with modularity and scalability
- Showcases cutting-edge tech

## Future Enhancements
- Multi-Language Support
- Advanced Analytics
- Enhanced Data Sources

## Contributors
- HrithikHadawale - AI Engineer and Backend Developer
- Pratik Dhumal - Frontend Developer

## License
[Add your license information here]
