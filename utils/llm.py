'''from langchain_groq import ChatGroq
from config import GROQ_API_KEY, MODEL_NAME

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name=MODEL_NAME,
    temperature=0.7
)

def ask_ai(prompt):

    try:

        response = llm.invoke(prompt)

        return response.content

    except Exception as e:

        return f"AI Error: {str(e)}"
'''

import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

from config import MODEL_NAME

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name=MODEL_NAME,
    temperature=0.7
)

def ask_ai(prompt):

    try:

        response = llm.invoke(prompt)

        return response.content

    except Exception as e:

        return f"AI Error: {str(e)}"
