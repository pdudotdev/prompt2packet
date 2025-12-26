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
You MUST output JSON that matches exactly ONE of the schemas below.
If required fields are missing, ask a clarification question instead of guessing.
Do NOT invent values, defaults, protocols, or fields.

Schemas:
{schemas}

Output JSON only. No explanations.
"""

def interpret_intent(user_text: str) -> dict:
    prompt = SYSTEM_PROMPT.format(
        schemas=json.dumps(SCHEMAS, indent=2)
    )

    response = client.chat.completions.create(
        model="gpt-5-mini",  # GPT-5 mini
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_text}
        ],
        temperature=0 # for deterministic behavior
    )

    content = response.choices[0].message.content
    return json.loads(content)
