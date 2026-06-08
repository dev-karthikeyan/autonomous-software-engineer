from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage

load_dotenv()

model = ChatMistralAI(model="mistral-small-2603")

def coding_agent(planning_agent: str):

    prompt = f"""
You are a Senior Software Engineer.

Generate the complete project as a JSON object.

IMPORTANT:

- Return ONLY raw JSON.
- Do NOT wrap output in markdown code blocks.
- Do NOT include explanations.
- Do NOT include comments outside JSON.
- Keys must be file paths.
- Values must be file contents.
- Output must be valid for Python json.loads().
- Escape all backslashes correctly.
- Escape all double quotes correctly.
- Return a single JSON object only.

Project Plan:

{planning_agent}
"""

    response = model.invoke(
        [HumanMessage(content=prompt)]
    )

    return response.content.strip()