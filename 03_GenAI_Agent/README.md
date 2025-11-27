# 🧠 Step 3 — Generative AI Agent

This step adds a Generative AI layer that produces high-quality enterprise content using
the Domain LLM from Step 1.

## ✨ Capabilities

The Generative AI Agent can generate:

### ITSM
- Incident summaries  
- Problem RCA (root cause analysis)  
- Change request justification  
- Technical troubleshooting steps  

### HRSD
- Employee communication  
- Case updates  
- HR policy explanations  

### CSM
- Customer email replies  
- Apology messages  
- Case resolution summaries  

### ITOM
- Alert analysis explanations  
- Infrastructure impact summaries  
- Suggested remediation steps  

### GRC
- Risk statements  
- Control failures  
- Compliance deviation summaries  

---

## Folder Contents

| File | Purpose |
|------|---------|
| genai_prompt.txt | System instructions for the GenAI agent |
| genai_examples.txt | Few-shot examples of generated outputs |
| genai_tasks.md | List of supported GenAI tasks |
| genai_pseudocode.py | Architecture/pseudocode of how the GenAI agent works |

---

## Next Step
After Step 3, we proceed to Step 4 — **Agentic AI (Plan → Act → Reflect)**.
