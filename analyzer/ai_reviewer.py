from openai import OpenAI

client = OpenAI()

def ai_review(code: str):
    prompt = f"""
You are a senior Java architect.

Review the following Java code and provide:
1. Design issues
2. Code smells
3. Suggested improvements

Be concise.

Code:
{code}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content
