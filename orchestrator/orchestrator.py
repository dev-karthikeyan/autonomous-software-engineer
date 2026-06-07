from agents.requirement_agent import requirement_agent
from agents.planning_agent import planning_agent
from agents.coding_agent import coding_agent

def run_project(user_request : str) :

    requirement_agent_output=requirement_agent(user_request)

    planning_agent_output=planning_agent(requirement_agent_output)

    coding_agent_output=coding_agent(planning_agent_output)

    return coding_agent_output 