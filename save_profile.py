import json
import os
from datetime import datetime

def save_profile_to_json(user_id: str, profile_data: str):
    """
    Save generated profile to a JSON file.
    Creates a profiles/ directory if it doesn't exist.
    """
    # Create profiles directory if it doesn't exist
    os.makedirs("profiles", exist_ok=True)
    
    # Parse the profile data (in case it's a string)
    try:
        profile_dict = json.loads(profile_data)
    except json.JSONDecodeError:
        # If it's not valid JSON, save as-is with metadata
        profile_dict = {
            "raw_output": profile_data,
            "error": "Could not parse as JSON"
        }
    
    # Add metadata
    profile_dict["user_id"] = user_id
    profile_dict["generated_at"] = datetime.now().isoformat()
    
    # Save to file
    filename = f"profiles/{user_id}.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(profile_dict, f, indent=2, ensure_ascii=False)
    
    print(f"💾 Profile saved to: {filename}")
    return filename
