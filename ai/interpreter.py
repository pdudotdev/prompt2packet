from schemas.tcp import TCPIntent
from schemas.udp import UDPIntent
from openai import OpenAI
import json

client = OpenAI()

SCHEMAS = {
    "tcp": TCPIntent.model_json_schema(),
    "udp": UDPIntent.model_json_schema(),
}

SYSTEM_PROMPT = """
You translate user intent into structured JSON for network traffic generation.

Rules:
- Output JSON ONLY (no prose, no markdown).
- Output a SINGLE JSON object.
- Use ONLY fields that exist in ONE of the schemas below.
- If the user did not specify a required field, OMIT it (do not guess).
- Do NOT invent values, defaults, protocols, or fields.
- If protocol is not explicitly stated, ask a clarification question.
- If the user provides a value that appears to correspond to a field, include it verbatim, even if it may be invalid.

Schemas (AUTHORITATIVE - you MUST comply exactly):
{schemas}
"""

def interpret_intent(user_text: str) -> dict:
    prompt = SYSTEM_PROMPT.format(schemas=json.dumps(SCHEMAS, indent=2))

    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_text}
        ],
    )

    content = (response.choices[0].message.content or "").strip()

    # Hard fail if model violates contract
    if not content.startswith("{"):
        raise ValueError(f"AI output was not JSON. Got: {content[:200]}")

    return json.loads(content)


def build_clarification_question(protocol: str | None, missing_fields: list[str], current_intent: dict) -> str:
    """
    Uses the AI only to phrase a polite question.
    """
    sys = """
    You are a CLI assistant for a network traffic generator.
    Ask the user a short, polite question requesting the missing required fields.
    Do NOT suggest defaults. Do NOT mention schemas. Do NOT mention internal variable names. Do NOT output JSON.
    Keep it to 1-2 sentences.
    """

    user = f"""
    Protocol: {protocol}
    Missing required fields: {missing_fields}
    Current intent so far: {json.dumps(current_intent, indent=2)}
    """

    resp = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {"role": "system", "content": sys.strip()},
            {"role": "user", "content": user.strip()},
        ],
    )

    return (resp.choices[0].message.content or "").strip()
