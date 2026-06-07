from agents.requirement_agent import requirement_agent
from agents.planning_agent import planning_agent

user_request = input("ENTER YOUR PROJECT REQUIREMENT :")

requirement_agent_output=requirement_agent(user_request)

project_plan=planning_agent(requirement_agent_output)

print(project_plan)