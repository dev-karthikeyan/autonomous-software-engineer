from orchestrator.orchestrator import run_project

user_request = input("ENTER YOUR PROJECT REQUIREMENT :")

reponse=run_project(user_request)

print(reponse)