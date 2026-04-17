import json
import os
from datetime import datetime

from supabase_client import supabase

def save_profile_to_json(user_id: str, profile_data: str):
    """
    Save generated profile to Supabase (primary) and local JSON (backup).
    Creates a profiles/ directory for backup files if it doesn't exist.
    """
    # Create profiles directory if it doesn't exist
    os.makedirs("profiles", exist_ok=True)
    
    # Parse the profile data (in case it's a string)
    try:
        # Strip markdown code fences if Groq wraps response in ```json ... ```
        cleaned = profile_data.strip()
        if cleaned.startswith("```"):
            cleaned = "\n".join(cleaned.split("\n")[1:])
        if cleaned.endswith("```"):
            cleaned = "\n".join(cleaned.split("\n")[:-1])
        profile_dict = json.loads(cleaned.strip())
    except json.JSONDecodeError:
        # If it's not valid JSON, save as-is with metadata
        profile_dict = {
            "raw_output": profile_data,
            "error": "Could not parse as JSON"
        }
    
    # Validate required schema keys (non-blocking warnings)
    if not isinstance(profile_dict.get("personality_traits"), list):
        print("⚠️ Warning: 'personality_traits' missing or not a list")
    if not isinstance(profile_dict.get("communication_style"), str):
        print("⚠️ Warning: 'communication_style' missing or not a string")
    if not isinstance(profile_dict.get("relationship_preferences"), dict):
        print("⚠️ Warning: 'relationship_preferences' missing or not an object")

    # Primary save: upsert AI profile to Supabase
    supabase_payload = {
        "user_id": user_id,
        "ai_profile": profile_dict,
        "updated_at": datetime.now().isoformat(),
    }
    try:
        supabase.table("profiles").upsert(supabase_payload, on_conflict="user_id").execute()
        print(f"☁️ Profile upserted to Supabase for user: {user_id}")
    except Exception as exc:
        print(f"⚠️ Warning: Supabase upsert failed for user {user_id}: {exc}")

    # Backup metadata for local JSON file
    backup_dict = {
        **profile_dict,
        "user_id": user_id,
        "generated_at": datetime.now().isoformat(),
    }
    
    # Save to file
    filename = f"profiles/{user_id}.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(backup_dict, f, indent=2, ensure_ascii=False)
    
    print(f"💾 Profile saved to: {filename}")
    return filename
