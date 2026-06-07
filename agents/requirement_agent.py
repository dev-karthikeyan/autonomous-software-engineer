from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage

load_dotenv()

model=ChatMistralAI(model="mistral-small-2603")

def requirement_agent(user_request:str) :

    prompt = f"""

    You are a Senior Software Requirements Analyst.

    Analyze the user request and extract:

    1. Project Type
    2. Features
    3. Technologies
    4. Expected Output

    user_request :
                 {user_request}

"""
    
    responce=model.invoke([HumanMessage(content=prompt)])

    return responce.content 



