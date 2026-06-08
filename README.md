# Autonomous Software Engineer

An AI-powered multi-agent system that transforms a user requirement into a structured software project.

The system analyzes requirements, creates a development plan, generates source code, and automatically builds the project structure.

---

## Overview

This project demonstrates how multiple AI agents can collaborate to automate the early stages of software development.

The workflow consists of:

1. Requirement Analysis
2. Project Planning
3. Code Generation
4. File Creation

---

## Features

* Requirement Analysis Agent
* Project Planning Agent
* Code Generation Agent
* Automatic File Creation
* Multi-Agent Architecture
* JSON-Based Project Generation
* End-to-End Project Scaffolding

---

## Workflow

```text
User Requirement
       ↓
Requirement Agent
       ↓
Planning Agent
       ↓
Coding Agent
       ↓
Project JSON Output
       ↓
File Creation Tool
       ↓
Generated Software Project
```

---

## Architecture

### Requirement Agent

Analyzes the user's request and extracts:

* Project Type
* Features
* Technologies
* Expected Output

### Planning Agent

Creates:

* Project Architecture
* Recommended Tech Stack
* Modules
* Development Tasks
* Folder Structure

### Coding Agent

Generates:

* Source Code
* Project Structure
* Configuration Files
* Dependencies

Example Output:

```json
{
  "main.py": "...",
  "requirements.txt": "...",
  "src/app.py": "..."
}
```

### File Creation Tool

Converts the generated JSON into actual files and folders.

---

## Tech Stack

* Python
* LangChain
* Mistral AI
* Rich
* Python Dotenv

---

## Project Structure

```text
autonomous-software-engineer/
│
├── agents/
│   ├── requirement_agent.py
│   ├── planning_agent.py
│   └── coding_agent.py
│
├── orchestrator/
│   └── orchestrator.py
│
├── tools/
│   └── file_tools.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Usage

Run the application:

```bash
python main.py
```

Example:

```text
ENTER YOUR PROJECT REQUIREMENT :

Build a weather application
```

The system will:

1. Analyze the requirement
2. Create a project plan
3. Generate source code
4. Create project files automatically

---

## Example Requests

```text
Build a weather app
```

```text
Create a chatbot using Python
```

```text
Build a task management application
```

```text
Create a personal finance tracker
```

---

## Current Version

### Version 1

Implemented:

* Requirement Agent
* Planning Agent
* Coding Agent
* Project File Generation

---

## Future Improvements

* Review Agent
* Documentation Agent
* Self-Correction Loop
* Testing Agent
* Deployment Agent
* Web Dashboard
* Multi-Model Support
* GitHub Repository Generation

---

## Learning Outcomes

This project explores:

* Multi-Agent Systems
* LLM Orchestration
* Prompt Engineering
* AI Workflow Design
* Automated Code Generation
* Project Scaffolding
* LangChain Integration

---

## Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository and submit pull requests.

---

## Project Vision

The long-term goal of this project is to evolve from a project generator into an autonomous AI software engineering system capable of planning, generating, reviewing, testing, and eventually deploying complete software applications.
