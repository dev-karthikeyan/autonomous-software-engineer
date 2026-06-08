from orchestrator.orchestrator import run_project
from tools.file_tools import create_project_files

user_request = input("ENTER YOUR PROJECT REQUIREMENT : ")

coding_agent_output = run_project(user_request)

result = create_project_files(coding_agent_output)

print(result)