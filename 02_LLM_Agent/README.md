# 🤖 Step 2 – LLM Agent (Tool-Calling Agent)

This step builds a ServiceNow-aware LLM Agent that can:

- Understand the user request
- Decide which ServiceNow module is needed (ITSM / HRSD / CSM / GRC / ITOM)
- Select the right tool (API/Flow)
- Return a structured instruction for execution

This Agent uses:
- The Domain LLM from `01_Custom_LLM`
- A set of ServiceNow tools (REST APIs / Flows)
- A simple orchestration loop

## Capabilities (MVP)

- Create ITSM Incidents
- Create HRSD Cases
- Create CSM Cases
- Log GRC Issues or Risks
- (Optional) Fetch ITOM Alerts

## Folder Files

| File | Description |
|------|-------------|
| tools_catalog.md | List of tools available to the Agent |
| agent_prompt.txt | Defines how the LLM selects tools |
| agent_flow.txt | Step-by-step workflow for the Agent |
| agent_pseudocode.py | Code structure for the orchestration |

Proceed with the remaining files to fully build the Agent.
