from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage

load_dotenv()

model=ChatMistralAI()

def coding_agent(planning_agent : str) :

    prompt=  f"""

    You are a Senior Software Engineer.

    Based on the project plan below:

    1. Identify all required files.
    2. Create the folder structure.
    3. Generate starter code for each file.

    Project Plan:
                {planning_agent}
"""
    
    response=model.invoke([HumanMessage(content=prompt)])

    return response