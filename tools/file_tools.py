import os
import json

def create_project_files(coding_agent_output: str):

    files = json.loads(coding_agent_output)

    print(type(files))

    for path, content in files.items():
        print("PATH =", path)
        print("CONTENT TYPE =", type(content))
        break

    for path, content in files.items():

        full_path = os.path.join(
            "generated_projects",
            path
        )

        folder = os.path.dirname(full_path)

        if folder:
            os.makedirs(folder, exist_ok=True)

        with open(full_path, "w", encoding="utf-8") as file:
            file.write(content)

    return "Project Created Successfully"