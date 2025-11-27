# 🧠 Agentic Memory Model — “SNE-Agentic-1”

This memory system allows the Agent to maintain short-term and long-term context across multiple steps of a task.

It enables:
- Multi-step reasoning  
- Better tool usage  
- Avoiding repeated actions  
- Correlations across ITSM, ITOM, HRSD, CSM, GRC  
- Historical awareness (“this happened before”)  

---

# 🔹 1. Memory Types

## **1. Short-Term Memory**
Used inside a single user request.

Stores:
- Current plan  
- Tool outputs  
- Latest ticket numbers  
- Intermediate results  
- Alert details  
- Generated summaries  

This resets after the task completes.

---

## **2. Long-Term Memory**
Persists across tasks during the session.

Stores:
- Recently created incidents  
- Recently created HR/CSM/GRC cases  
- Past alerts and their outcomes  
- Problem/RCA summaries  
- User preferences (optional)  

This helps the agent identify:
- Recurrences  
- Patterns  
- Dependencies  
- Cross-module relationships  

---

# 🔹 2. Memory Schema (JSON Structure)

```json
{
  "incidents": [
    {
      "number": "INC0012345",
      "sys_id": "abc123",
      "short_description": "Email outage",
      "created_at": "2025-11-26T10:21:00Z"
    }
  ],
  "hr_cases": [],
  "csm_cases": [],
  "grc_risks": [],
  "alerts": [],
  "problems": [],
  "summaries": [],
  "preferences": {}
}

```
-----
# 🔹3. Memory Update Rules
After every tool call:

If a new incident is created → add to incidents[]

If a new HR case is created → add to hr_cases[]

If a new CSM case is created → add to csm_cases[]

If a GRC risk is logged → add to grc_risks[]

If an alert is analyzed → save to alerts[]

If GenAI writes summary → save to summaries[]

-------
# 🔹 4. How Memory Helps the Agent
✓ ITOM → ITSM correlation

If an alert says CPU is 95% and memory contains:

"incidents": ["High CPU alert last night"]


→ Agent can say: “This issue is recurring, should we create a Problem record?”

✓ HRSD follow-up

Memory:

hr_cases: ["HR-CASE-00123"]


User: “What happened to my laptop request?”
→ Agent knows the case number and retrieves it.

✓ CSM customer issue recurrence

Memory of:

csm_cases: ["Customer cannot access account"]


→ Helps detect repeated issues.

✓ GRC risk escalation

If two DR tests failed recently → memory helps agent decide:
→ “This requires a GRC Risk record.”

✓ Better summaries

Memory helps the GenAI agent combine information into executive summaries.

---------
# 🔹 5. Output Format for Memory Updates

Each time a tool is executed:

{
  "memory_update": {
    "incidents": [...],
    "alerts": [...],
    "summaries": [...]
  }
}


This file defines how the Agent stores, updates, and uses memory to make multi-step intelligent decisions.


---
