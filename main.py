from fetch_user import fetch_user_onboarding
from prepare_payload import build_agent_input
from agent import build_profile
from save_profile import save_profile_to_json

def process_user(user_id: str):
    """
    Profile building pipeline:
    1. Fetch user data from Supabase
    2. Transform data for AI processing
    3. Generate profile using OpenAI
    4. Save profile to JSON file
    """
    print(f"🔄 Processing user: {user_id}")
    
    # 1️⃣ Fetch from Supabase
    print("📥 Fetching user data from Supabase...")
    raw_data = fetch_user_onboarding(user_id)
    print("✅ User data retrieved")

    # 2️⃣ Prepare for AI
    print("🔄 Transforming data for AI...")
    ai_payload = build_agent_input(raw_data)
    print("✅ Payload prepared")

    # 3️⃣ Send to Agent
    print("🤖 Generating profile with OpenAI...")
    structured_profile = build_profile(ai_payload)
    print("✅ Profile generated")
    
    # 4️⃣ Save to JSON
    save_profile_to_json(user_id, structured_profile)
    
    print("\n" + "="*50)
    print("GENERATED PROFILE:")
    print("="*50)
    print(structured_profile)
    print("="*50)
    
    return structured_profile

if __name__ == "__main__":
    process_user("f9b89427-8cb7-480f-8704-a794dec8b541")