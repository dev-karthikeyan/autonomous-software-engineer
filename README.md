# 🤖 Autonomous Software Engineer

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square)
![LangChain](https://img.shields.io/badge/LangChain-latest-green?style=flat-square)
![Mistral AI](https://img.shields.io/badge/Mistral_AI-latest-orange?style=flat-square)
![Version](https://img.shields.io/badge/version-1.0-gray?style=flat-square)

A multi-agent AI system that transforms a plain-English requirement into a fully scaffolded software project — analysis, planning, code generation, and file creation, end-to-end.

---

## How it works

Four agents collaborate in sequence. Each one hands off its output to the next, building from raw requirement all the way to files on disk.

```
User Requirement → Requirement Agent → Planning Agent → Coding Agent → File Creation → Generated Project
```

---

## Agents

### 🔍 Requirement Agent
Parses the user prompt and extracts structured intent.
- **Outputs:** Project type · Features · Tech stack

### 🗺️ Planning Agent
Designs the architecture and development plan.
- **Outputs:** Modules · Folder structure · Tasks

### 💻 Coding Agent
Generates all source files as structured JSON.
- **Outputs:** Source code · Config files · Dependencies

### 📁 File Creation Tool
Converts the JSON output into real files and folders on disk.
- **Outputs:** Writes files · Creates directories

---

## Coding Agent Output Format

The coding agent returns a JSON map of file paths to file contents, which the file creation tool then materialises.

```json
{
  "main.py": "# Entry point\n...",
  "requirements.txt": "langchain\nmistralai\nrich",
  "src/app.py": "# Core app logic\n...",
  "src/config.py": "# Environment config\n..."
}
```

---

## Project Structure

```
autonomous-software-engineer/
├── agents/
│   ├── requirement_agent.py
│   ├── planning_agent.py
│   └── coding_agent.py
├── orchestrator/
│   └── orchestrator.py
├── tools/
│   └── file_tools.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Tech Stack

| Technology | Role |
|---|---|
| Python | Core language |
| LangChain | Agent orchestration |
| Mistral AI | LLM backend |
| Rich | Terminal UI |
| python-dotenv | Environment config |

---

## Usage

```bash
python main.py
```

Then enter your requirement at the prompt:

```
ENTER YOUR PROJECT REQUIREMENT:

Build a weather application
```

The system analyses the requirement, plans the architecture, generates source code, and writes the project to disk — no manual scaffolding needed.

---

## Example Prompts

```
Build a weather app
```
```
Create a Python chatbot
```
```
Build a task management application
```
```
Create a personal finance tracker
```

---

## Roadmap

| Status | Feature | Description |
|---|---|---|
| ✅ Done | Core pipeline | Requirement → Planning → Coding → File creation |
| 🔜 Next | Review agent | Validates and critiques generated code before writing to disk |
| 🔜 Next | Testing agent | Auto-generates unit tests for produced source files |
| 📌 Planned | Self-correction loop | Agents retry and refine on validation failure |
| 📌 Planned | Documentation agent | Generates README and inline docs automatically |
| 📌 Planned | Deployment agent | Scaffolds CI/CD config and deploys to cloud targets |
| 📌 Planned | GitHub integration | Creates repo, commits, and opens PRs automatically |
| 📌 Planned | Web dashboard | Visual interface for monitoring agent runs |

---

## What You'll Learn

- Multi-agent system design
- LLM orchestration patterns
- Prompt engineering
- AI workflow design
- Automated code generation
- Project scaffolding
- LangChain integration

---

## Contributing

Contributions, suggestions, and pull requests are welcome. Fork the repo, make your changes, and open a PR.

The long-term vision is a fully autonomous AI engineering system that can plan, generate, review, test, and deploy complete software applications.

---

## Project Vision

> Evolve from a project generator into an autonomous AI software engineering system capable of planning, generating, reviewing, testing, and eventually deploying complete software applications.