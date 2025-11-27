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
