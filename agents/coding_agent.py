from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage

load_dotenv()

model=ChatMistralAI()

def coding_agent(planning_agent : str) :

    prompt=  f"""

    You are a Senior Software Engineer.

    Based on the project plan below:

    Generate the complete project files.

    Return ONLY valid JSON.

    Rules:
    1. Return only JSON.
    2. No explanations.
    3. No markdown.
    4. No code blocks.
    5. Keys must be file paths.
    6. Values must contain the code/content for that file.

    
    Project Plan:
                {planning_agent}

"""
    
    response=model.invoke([HumanMessage(content=prompt)])

    return response.content