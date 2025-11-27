"""
genai_pseudocode.py
---------------------------------------------------------
This is pseudocode for the Generative AI Agent used in Step 3.
It converts raw input (incidents, alerts, customer messages, etc.)
into high-quality enterprise text output.

The GenAI Agent uses:
- genai_prompt.txt (system instructions)
- genai_examples.txt (few-shot examples)
- genai_tasks.md (task catalog)
---------------------------------------------------------
"""


# -------------------------------------------------------
# Step 1 — Build Prompt
# -------------------------------------------------------

def build_genai_prompt(raw_input, task_type):
    """
    Builds the full GenAI prompt using:
    - genai_prompt.txt
    - genai_examples.txt
    - raw_input text (incident, alert, etc.)
    - task_type (e.g., INCIDENT_SUMMARY, CUSTOMER_EMAIL)

    Returns a structured LLM prompt.
    """

    system_prompt = load_file("03_GenAI_Agent/genai_prompt.txt")
    examples = load_file("03_GenAI_Agent/genai_examples.txt")

    prompt = f"""
{system_prompt}

# FEW-SHOT EXAMPLES
{examples}

# TASK TYPE
{task_type}

# RAW INPUT
\"\"\" 
{raw_input}
\"\"\"

# ACTION
Generate the following:
1. SUMMARY
2. DETAIL
3. RECOMMENDATIONS
"""

    return prompt


# -------------------------------------------------------
# Step 2 — Call the LLM
# -------------------------------------------------------

def call_genai_llm(prompt):
    """
    Calls the LLM (OpenAI / Llama / Mistral).
    Returns the full formatted content.
    """
    response = LLM_API_CALL(prompt)
    return response


# -------------------------------------------------------
# Step 3 — Generate Output
# -------------------------------------------------------

def generate_genai_content(raw_input, task_type):
    """
    Main entry point for GenAI content generation.
    """
    prompt = build_genai_prompt(raw_input, task_type)
    result = call_genai_llm(prompt)

    return {
        "task_type": task_type,
        "input": raw_input,
        "output": result
    }


# -------------------------------------------------------
# Example Usage
# -------------------------------------------------------

if __name__ == "__main__":

    # Example raw input from an incident
    incident_text = """
    Email service is down. SMTP server unreachable.
    Affects 45% of users. Started at 10:21 AM.
    """

    response = generate_genai_content(
        raw_input=incident_text,
        task_type="ITSM_INCIDENT_SUMMARY"
    )

    print("\n=== GENAI OUTPUT ===")
    print(response["output"])


# -------------------------------------------------------
# Utility Functions (Mocked)
# -------------------------------------------------------

def load_file(path):
    return f"CONTENT_OF({path})"

def LLM_API_CALL(prompt):
    return "MOCKED_GENAI_RESPONSE"
