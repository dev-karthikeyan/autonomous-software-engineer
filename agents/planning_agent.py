from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage

load_dotenv()

model=ChatMistralAI(model="mistral-small-2603")

def planning_agent(requirement_agent : str) :

    prompt = f"""

    You are a Senior Software Architect.

    Based on the requirements below, create:

    1. Project Architecture
    2. Recommended Tech Stack
    3. Modules
    4. Development Tasks
    5. Suggested Folder Structure

    Requirements:
    {requirement_agent}

    """

    response=model.invoke([HumanMessage(content=prompt)])

    return response.content
