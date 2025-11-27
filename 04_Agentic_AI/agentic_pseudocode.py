"""
agentic_pseudocode.py
--------------------------------------------------------
This file represents the entire Agentic AI architecture.

SNE-Agentic-1 performs:
1. Planning (multi-step)
2. Execution (tool calling)
3. Reflection (retry logic)
4. Memory updates (short-term + long-term)
5. Multi-module reasoning (ITSM + HRSD + CSM + ITOM + GRC)

This is not runnable code — it is clean architecture-level
pseudocode for interviews, documentation, and future coding.
--------------------------------------------------------
"""


# -------------------------------------------------------
# GLOBAL MEMORY (long-term memory for the session)
# -------------------------------------------------------

AGENT_MEMORY = {
    "incidents": [],
    "hr_cases": [],
    "csm_cases": [],
    "grc_risks": [],
    "alerts": [],
    "summaries": []
}



# -------------------------------------------------------
# STEP 1 — CALL PLANNER (Generate Plan)
# -------------------------------------------------------

def call_agentic_planner(user_message):
    """
    Calls the Planner LLM using agentic_planner.txt.
    Returns:
        { "plan": [...] }
    """

    planner_prompt = load_file("04_Agentic_AI/agentic_planner.txt")
    prompt = planner_prompt.replace("{{user_message}}", user_message)

    planner_response = LLM_API_CALL(prompt)
    return parse_json(planner_response)



# -------------------------------------------------------
# STEP 2 — EXECUTE EACH STEP IN THE PLAN
# -------------------------------------------------------

def execute_plan(plan):
    """
    Executes each step of the plan one-by-one.
    Uses:
        - Tool Calling Agent (Step 2)
        - GenAI Agent (Step 3)
        - Reflection logic
        - Memory updates
    """

    results = []

    for step in plan:

        print(f"\n🟦 Executing: {step}")

        # Decide if this step requires:
        # 1. Tool call
        # 2. GenAI content generation
        # 3. Clarification question
        # 4. No action

        if "create incident" in step.lower():
            result = create_incident_tool_step(step)

        elif "hr case" in step.lower():
            result = create_hr_case_tool_step(step)

        elif "csm case" in step.lower():
            result = create_csm_case_tool_step(step)

        elif "risk" in step.lower():
            result = create_grc_risk_tool_step(step)

        elif "alert" in step.lower():
            result = get_alerts_tool_step(step)

        elif "summary" in step.lower():
            result = genai_summary_step(step)

        else:
            result = {"info": "No action needed for this step"}

        # Reflection Phase
        reflected = reflect_on_result(result)
        results.append(reflected)

        # Memory Update Phase
        update_memory_if_needed(reflected)

    return results



# -------------------------------------------------------
# STEP 3 — TOOL WRAPPERS (Using Step 2 Tools)
# -------------------------------------------------------

def create_incident_tool_step(step):
    fields = extract_fields(step)
    return create_incident(fields)

def create_hr_case_tool_step(step):
    fields = extract_fields(step)
    return create_hr_case(fields)

def create_csm_case_tool_step(step):
    fields = extract_fields(step)
    return create_csm_case(fields)

def create_grc_risk_tool_step(step):
    fields = extract_fields(step)
    return create_grc_issue(fields)

def get_alerts_tool_step(step):
    return get_itom_alerts("active=true")

def genai_summary_step(step):
    text = "Summaries of previous steps"
    return generate_genai_content(text, "EXEC_SUMMARY")



# -------------------------------------------------------
# STEP 4 — REFLECTION LOGIC
# -------------------------------------------------------

def reflect_on_result(result):
    """
    If the tool output indicates failure:
    - Retry
    - Modify arguments
    - Adjust plan
    """
    if "error" in str(result).lower():
        return {"reflection": "Retrying with modified inputs."}
    return result



# -------------------------------------------------------
# STEP 5 — MEMORY UPDATE LOGIC
# -------------------------------------------------------

def update_memory_if_needed(result):
    """
    Store important results in memory.
    """
    if "number" in result:
        AGENT_MEMORY["incidents"].append(result)

    if "hr_case" in result:
        AGENT_MEMORY["hr_cases"].append(result)

    if "risk" in result:
        AGENT_MEMORY["grc_risks"].append(result)

    # Summary storage
    if isinstance(result, str) and "SUMMARY" in result:
        AGENT_MEMORY["summaries"].append(result)



# -------------------------------------------------------
# MAIN AGENTIC LOOP
# -------------------------------------------------------

def run_agentic_ai(user_message):
    """
    1. Call Planner
    2. Execute steps
    3. Return combined results
    """

    plan_json = call_agentic_planner(user_message)
    plan = plan_json.get("plan", [])

    execution_results = execute_plan(plan)

    return {
        "plan": plan,
        "results": execution_results,
        "memory": AGENT_MEMORY
    }



# -------------------------------------------------------
# MOCK FUNCTIONS (Used for architecture demonstration)
# -------------------------------------------------------

def extract_fields(step):
    return {"short_description": "Generated from step"}

def load_file(path):
    return f"CONTENT_OF({path})"

def LLM_API_CALL(prompt):
    return "{ 'plan': ['Step 1', 'Step 2'] }"

def parse_json(text):
    return {"plan": ["Step 1: Demo", "Step 2: Demo"]}

# Tools from Step 2 (mock)
def create_incident(fields): return {"number": "INC0012345"}
def create_hr_case(fields): return {"hr_case": "CASE00123"}
def create_csm_case(fields): return {"csm_case": "CSM00123"}
def create_grc_issue(fields): return {"risk": "RISK00123"}
def get_itom_alerts(query): return {"alert": "CPU High"}
def generate_genai_content(text, task): return "SUMMARY: Demo content"
