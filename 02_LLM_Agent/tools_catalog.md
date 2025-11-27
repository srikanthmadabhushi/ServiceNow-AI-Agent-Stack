# 🔧 ServiceNow Tools Catalog (for LLM Agent)

These are the actions (“tools”) the Agent can use.  
Each tool maps to a **ServiceNow REST API** or a **Flow Designer action**.

---

## 🟦 1. ITSM Tools

### `create_incident(fields)`
- **Table:** `incident`
- **REST:** `POST /api/now/table/incident`
- **Fields Example:**
  - `short_description`
  - `description`
  - `category`
  - `subcategory`
  - `priority`
  - `assignment_group`
  - `caller_id`

### `get_incident(sys_id)`
- **REST:** `GET /api/now/table/incident?sys_id={sys_id}`

---

## 🟧 2. HRSD Tools

### `create_hr_case(fields)`
- **Table:** `sn_hr_core_case`
- **REST:** `POST /api/now/table/sn_hr_core_case`
- **Fields Example:**
  - `short_description`
  - `opened_for`
  - `hr_case_type`
  - `assignment_group`

---

## 🟩 3. CSM Tools

### `create_csm_case(fields)`
- **Table:** `sn_customerservice_case`
- **REST:** `POST /api/now/table/sn_customerservice_case`
- **Fields Example:**
  - `short_description`
  - `account`
  - `contact`
  - `priority`

---

## 🟥 4. GRC Tools

### `create_grc_issue(fields)`
- **Table:** `sn_grc_issue` or `sn_risk_risk` (instance may vary)
- **REST:** `POST /api/now/table/sn_grc_issue`
- **Fields Example:**
  - `short_description`
  - `risk_type`
  - `severity`

---

## 🟪 5. ITOM Tools (Optional for MVP, recommended later)

### `get_itom_alerts(filter)`
- **Table:** `em_alert` (if present)
- **REST:** `GET /api/now/table/em_alert?{query}`
- **Purpose:** Fetch alerts, events, CI issues

---

## 📌 How the Agent Uses These Tools

1. The Domain LLM (Step 1) returns:
   - module  
   - action  
   - fields  

2. The Agent LLM decides which tool to call.

3. The orchestration code executes:
   - `create_incident()`
   - `create_hr_case()`
   - etc.

4. ServiceNow creates the record in PDI.

5. The Agent returns the result to the user:
   - “Incident INC0012345 created successfully.”

---

This file is used later in:
- **Agent Prompt**
- **Agentic AI Planning**
- **Python Orchestration**
- **GitHub documentation**
- **Interview explanations**
