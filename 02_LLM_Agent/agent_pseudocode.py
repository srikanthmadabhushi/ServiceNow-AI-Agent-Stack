"""
agent_pseudocode.py
---------------------------------------------------------
This is NOT full code.
This is clear architecture-level pseudocode showing how
the ServiceNow LLM Agent works end-to-end.

Once Step 3 and Step 4 are complete, this can be converted
to real Python code.
---------------------------------------------------------
"""

# -------------------------------------------------------
# STEP 1 — CALL DOMAIN LLM (SNE-AI-1)
# -------------------------------------------------------

def call_domain_llm(user_message):
    """
    Sends user_message to the Domain LLM created in Step 1.
    Uses:
        - system_prompt.txt
        - examples.txt
        - prompt_template.txt
    Returns JSON:
        module, action, fields, next_steps, confidence
    """

    # Load and build prompt (pseudo)
    system_prompt = load_file("01_Custom_LLM/system_prompt.txt")
    examples = load_file("01_Custom_LLM/examples.txt")
    template = load_file("01_Custom_LLM/prompt_template.txt")

    prompt = template.replace("{{system_prompt}}", system_prompt)\
                     .replace("{{examples}}", examples)\
                     .replace("{{user_message}}", user_message)

    # CALL LLM (OpenAI, Llama, or Mistral)
    domain_llm_response = LLM_API_CALL(prompt)

    # Return parsed JSON structure
    return parse_json(domain_llm_response)


# -------------------------------------------------------
# STEP 2 — CALL AGENT LLM (TOOL SELECTOR)
# -------------------------------------------------------

def call_agent_llm(domain_json):
    """
    Sends domain_json to the Agent LLM using agent_prompt.txt
    Returns:
        tool_name
        tool_arguments
        user_friendly_message
    """

    agent_prompt = load_file("02_LLM_Agent/agent_prompt.txt")

    formatted_prompt = agent_prompt.replace("{{domain_json}}", str(domain_json))

    agent_llm_response = LLM_API_CALL(formatted_prompt)

    return parse_json(agent_llm_response)


# -------------------------------------------------------
# STEP 3 — TOOL IMPLEMENTATION (REST API CALLS)
# -------------------------------------------------------

def create_incident(fields):
    """
    Calls ServiceNow Incident API:
    POST /api/now/table/incident
    """
    return SNOW_POST("/api/now/table/incident", fields)


def create_hr_case(fields):
    return SNOW_POST("/api/now/table/sn_hr_core_case", fields)


def create_csm_case(fields):
    return SNOW_POST("/api/now/table/sn_customerservice_case", fields)


def create_grc_issue(fields):
    return SNOW_POST("/api/now/table/sn_grc_issue", fields)


def get_incident(sys_id):
    return SNOW_GET(f"/api/now/table/incident?sys_id={sys_id}")


def get_itom_alerts(filter_query):
    return SNOW_GET(f"/api/now/table/em_alert?{filter_query}")


# -------------------------------------------------------
# STEP 4 — AGENT ORCHESTRATION LOOP
# -------------------------------------------------------

def agent_handle_message(user_message):
    """
    The brain of the Agent.
    1. Calls Domain LLM → Gets module/action/fields
    2. Calls Agent LLM → Gets tool+arguments
    3. Calls tool function → Executes action in ServiceNow
    4. Returns final message to user
    """

    # STEP 1 - Domain understanding
    domain_json = call_domain_llm(user_message)

    # STEP 2 - Decide tool
    agent_decision = call_agent_llm(domain_json)

    tool_name = agent_decision.get("tool_name")
    tool_args = agent_decision.get("tool_arguments")
    user_msg = agent_decision.get("user_friendly_message")

    # STEP 3 - Execute tool
    result = None

    if tool_name == "create_incident":
        result = create_incident(tool_args)

    elif tool_name == "create_hr_case":
        result = create_hr_case(tool_args)

    elif tool_name == "create_csm_case":
        result = create_csm_case(tool_args)

    elif tool_name == "create_grc_issue":
        result = create_grc_issue(tool_args)

    elif tool_name == "get_incident":
        result = get_incident(tool_args.get("sys_id"))

    elif tool_name == "get_itom_alerts":
        result = get_itom_alerts(tool_args)

    elif tool_name is None:
        # No action needed
        result = {"message": "No tool required."}

    # STEP 4 - Final combined output
    final_response = {
        "user_message": user_msg,
        "servicenow_result": result,
        "domain_understanding": domain_json
    }

    return final_response


# -------------------------------------------------------
# MOCK FUNCTIONS (for architecture only)
# -------------------------------------------------------

def LLM_API_CALL(prompt):
    """ Placeholder for actual LLM API call """
    return "{ 'tool_name': 'create_incident' }"


def SNOW_POST(url, body):
    """ Placeholder for ServiceNow POST call """
    return {"status": "success", "url": url, "body": body}


def SNOW_GET(url):
    """ Placeholder for ServiceNow GET call """
    return {"status": "success", "url": url}


def load_file(path):
    """ Placeholder file loader """
    return f"CONTENT_OF({path})"


def parse_json(text):
    """ Placeholder for JSON parsing """
    return {"parsed": "json"}
