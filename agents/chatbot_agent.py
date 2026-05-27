from utils.llm import ask_ai

def trip_chatbot(
    user_question,
    trip_details
):

    prompt = f"""
    You are a luxury AI travel assistant.

    Trip Details:
    {trip_details}

    User Question:
    {user_question}

    Give:
    - Smart travel advice
    - Food recommendations
    - Safety tips
    - Best attractions
    - Local transportation tips

    Keep answers professional and useful.
    """

    return ask_ai(prompt)