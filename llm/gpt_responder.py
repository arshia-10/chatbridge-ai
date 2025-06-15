# llm/gpt_responder.py

import subprocess

def get_ai_reply(prompt: str) -> str:
    try:
        result = subprocess.run(
            ["ollama", "run", "mistral"],
            input=prompt.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=60
        )
        return result.stdout.decode("utf-8").strip()
    except Exception as e:
        return f"❌ Error: {str(e)}"
