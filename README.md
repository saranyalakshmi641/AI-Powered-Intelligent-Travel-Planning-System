# AI-Powered-Intelligent-Travel-Planning-System

VoyageAI is an AI-powered travel planning application that helps users plan trips easily with personalized recommendations, smart itineraries, hotel suggestions, flight options, and travel assistance — all in one place.

The project is built using Python, Streamlit, and LLaMA-based AI agents to provide a smooth and interactive travel planning experience.

🌍 Features
Smart AI-based travel planning
Personalized trip itinerary generation
Flight recommendations
Hotel recommendations
Budget analytics with charts
Interactive AI travel assistant chatbot
Beautiful modern UI using Streamlit
Multi-agent architecture
Travel type and seat preference customization
🛠️ Tech Stack
Python
Streamlit
Pandas
Plotly
LLaMA / Groq API
Multi-Agent AI System
📂 Project Structure
VoyageAI/
│
├── app.py
├── requirements.txt
├── agents/
│   ├── coordinator_agent.py
│   ├── chatbot_agent.py
│   ├── hotel_agent.py
│   ├── flight_agent.py
│   └── itinerary_agent.py
│
├── data/
├── assets/
└── README.md
🚀 How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/your-username/VoyageAI.git
2️⃣ Move into the Project Folder
cd VoyageAI
3️⃣ Install Required Packages
pip install -r requirements.txt
4️⃣ Run the Application
streamlit run app.py
💡 How It Works
User enters travel preferences
AI agents process the request
Flight and hotel recommendations are generated
Budget analysis is calculated
AI creates a travel itinerary
Chatbot assists users with travel-related questions
📊 Main Functionalities
✈️ Flight Recommendation

Suggests multiple flight options based on budget and preferences.

🏨 Hotel Recommendation

Provides hotel suggestions with ratings and pricing.

🗓️ Smart Itinerary

Generates a complete day-wise travel plan.

🤖 AI Travel Assistant

Answers travel-related queries interactively.

💸 Budget Analytics

Displays spending breakdown using charts.

🎯 Future Improvements
Real-time flight APIs
Google Maps integration
Weather forecasting
Online booking support
User authentication
Saved trip history
