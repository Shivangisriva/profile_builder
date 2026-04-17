from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def build_profile(onboarding_data):
    conversation_transcript = onboarding_data.get("conversation_transcript")
    has_transcript = isinstance(conversation_transcript, str) and conversation_transcript.strip()

    if has_transcript:
        prompt = f"""
    You are a psychological profile builder.

    Primary source: voice conversation transcript.
    Secondary context: structured onboarding answers.

    Voice conversation transcript:
    {conversation_transcript}

    Structured onboarding answers:
    {onboarding_data}

    Generate structured JSON with:
    - personality_traits (list)
    - communication_style (string)
    - relationship_preferences (object)
    
    Output ONLY valid JSON, no other text.
    """
    else:
        prompt = f"""
    You are a psychological profile builder.

    Based on the following onboarding answers:
    {onboarding_data}

    Generate structured JSON with:
    - personality_traits (list)
    - communication_style (string)
    - relationship_preferences (object)
    
    Output ONLY valid JSON, no other text.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You output ONLY valid JSON."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content