from utils.llm import ask_ai

def create_itinerary(destination, days, travel_type):

    prompt = f"""
    Create a professional {days}-day travel itinerary for {destination}.

    Travel Type: {travel_type}

    Include:
    - Attractions
    - Food suggestions
    - Best timings
    - Travel tips
    - Activities
    """

    return ask_ai(prompt)