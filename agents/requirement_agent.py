from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage

load_dotenv()

model = ChatMistralAI(model="mistral-small-2603")

def requirement_agent(user_request: str):

    prompt = f"""
You are a Senior Software Requirements Analyst.

Analyze the user's request and create a detailed software requirements document.

Extract:

1. Project Type
2. Project Goal
3. Core Features
4. Functional Requirements
5. Non-Functional Requirements
6. Suggested Technologies
7. Inputs
8. Outputs
9. Constraints
10. Assumptions

User Request:
{user_request}

Return a structured requirements document.
"""

    response = model.invoke(
        [HumanMessage(content=prompt)]
    )

    return response.content