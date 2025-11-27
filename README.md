# 🧠 ServiceNow AI Agent Stack (Multi-Layer AI Architecture)

This repository contains a complete multi-agent AI system designed for ServiceNow workflows.
It includes:

Custom Domain LLM (ServiceNow-Aware)

LLM Agent (Tool Selector & API Executor)

Generative AI Agent (Enterprise Content Generator)

Agentic AI Layer (Plan → Act → Reflect → Memory)

Supported ServiceNow domains:

ITSM

ITOM

HRSD

CSM

GRC

This architecture is modular, fully documented, and can be executed with any LLM (OpenAI, Mistral, LLaMA, etc.) and any ServiceNow instance.

# 🧩 4-Layer Architecture

🔵 STEP 1 — Domain LLM (SNE-AI-1)

A domain-specific LLM built with:

system_prompt.txt

examples.txt

prompt_template.txt

The model converts natural language → structured JSON.

Output Example
{
 "module": "ITSM",
 "action": "Create Incident",
 "fields": {
   "short_description": "Email outage",
   "priority": "P2"
 },
 "confidence": 0.93
}


This becomes the source-of-truth for all downstream actions.

# 🟢 STEP 2 — Tool-Calling LLM Agent

The Agent maps user intent → ServiceNow API actions.

Uses:

tool_catalog.json

agent_prompt.txt

agent_flow.txt

agent_pseudocode.py

Example Agent Output
{
 "tool_name": "create_incident",
 "tool_arguments": {
   "short_description": "Email outage",
   "priority": "P2"
 },
 "user_friendly_message": "Creating a P2 incident for the outage."
}


Supported actions:

Module	Actions
ITSM	create_incident, get_incident
HRSD	create_hr_case
CSM	create_csm_case
ITOM	get_itom_alerts
GRC	create_grc_issue

# 🟧 STEP 3 — Generative AI Agent (SNE-GenAI-1)

Creates structured enterprise content:

Incident summaries

RCA (Root Cause Analysis)

Customer emails

HR case updates

GRC risk statements

Change implementation plans

Uses:

genai_prompt.txt

genai_examples.txt

genai_tasks.md

genai_pseudocode.py

Typical Output Example
SUMMARY:
Email outage affecting 45% of users.

DETAIL:
SMTP relay unreachable on Mail-Gateway-01.

RECOMMENDATIONS:
- Restart SMTP service
- Notify Messaging Support

# 🔴 STEP 4 — Agentic AI Layer (Planner + Memory + Reflection)

This turns the entire system into an intelligent autonomous agent.

Features:

✔ Multi-step planning
✔ Tool execution
✔ Reflection loop
✔ Error recovery
✔ Memory persistence
✔ Multi-module reasoning

Uses:

agentic_prompt.txt

agentic_planner.txt

agentic_memory.md

agentic_pseudocode.py

Example Agentic Plan
{
 "plan": [
   "Step 1: Retrieve ITOM alerts.",
   "Step 2: Analyze severity using GenAI.",
   "Step 3: Create incident if needed.",
   "Step 4: Generate summary.",
   "Step 5: Update memory."
 ]
}


This is how real autonomous AI behaves in enterprise environments.

📂 Repository Structure
ServiceNow_AI_Agent_Stack/
│
├── 01_Domain_LLM/
│   ├── system_prompt.txt
│   ├── examples.txt
│   ├── prompt_template.txt
│   └── README.md
│
├── 02_LLM_Agent/
│   ├── tool_catalog.json
│   ├── agent_prompt.txt
│   ├── agent_flow.txt
│   ├── agent_pseudocode.py
│   └── README.md
│
├── 03_GenAI_Agent/
│   ├── genai_prompt.txt
│   ├── genai_examples.txt
│   ├── genai_tasks.md
│   ├── genai_pseudocode.py
│   └── README.md
│
├── 04_Agentic_AI/
│   ├── agentic_prompt.txt
│   ├── agentic_planner.txt
│   ├── agentic_memory.md
│   ├── agentic_pseudocode.py
│   └── README.md
│
└── main_README.md   (this file)

🔬 How to Test the System

You can test the system in three ways:

# 1️⃣ Test Directly in ChatGPT (Recommended)

Example:

Test Step 1:

"Email outage affecting 40% of users."


Test Step 2:

"Simulate tool selection for the above JSON."


Test Step 3:

"Summarize this incident using GenAI."


Test Step 4:

"Simulate agentic workflow for CPU alert 95%."

# 2️⃣ Test Locally with Python (Optional)

Run:

from agentic_pseudocode import run_agentic_ai

response = run_agentic_ai("Analyze CPU alert and create incident.")
print(response)

# 3️⃣ Connect to ServiceNow REST APIs (Advanced)

Example:

POST /api/now/table/incident
{
  "short_description": "Test from AI Agent",
  "priority": "2"
}

# 📈 Future Roadmap
🔹 Add vector memory (FAISS / Chroma)
🔹 Add RAG for KB articles
🔹 Add multi-agent collaboration
🔹 Build UI Dashboard (Streamlit/React)
🔹 Connect to real ServiceNow PDI
🔹 Add fine-tuned Llama 3.1 model
🔹 Run the agent in LangGraph / Swarm

# 👤 Author

Srikanth Madabhushi
AI Automation & Workflow Engineer
MS in Artificial Intelligence
Portfolio: SrikanthMadabhushi.github.io
