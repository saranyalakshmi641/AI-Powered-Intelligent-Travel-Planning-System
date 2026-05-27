from utils.llm import ask_ai

def recommend_places(destination):

    prompt = f"""
    Suggest top tourist attractions in {destination}.
    """

    return ask_ai(prompt)