import argparse

from fetch_user import fetch_all_user_ids, fetch_unprocessed_user_ids, fetch_user_onboarding
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
    try:
        raw_data = fetch_user_onboarding(user_id)
    except ValueError as exc:
        print(f"❌ {exc}")
        return None
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


def process_all_users():
    print("📥 Fetching all users from Supabase...")
    user_ids = fetch_all_user_ids()

    if not user_ids:
        print("⚠️ No users found in 'profiles' table")
        return

    print(f"✅ Found {len(user_ids)} users")

    success_count = 0
    skipped_count = 0
    failed_count = 0

    for index, user_id in enumerate(user_ids, start=1):
        print(f"\n[{index}/{len(user_ids)}] Starting user {user_id}")
        try:
            result = process_user(user_id)
            if result is None:
                skipped_count += 1
            else:
                success_count += 1
        except Exception as exc:
            failed_count += 1
            print(f"❌ Failed for user {user_id}: {exc}")

    print("\n" + "=" * 50)
    print("RUN SUMMARY")
    print("=" * 50)
    print(f"✅ Success: {success_count}")
    print(f"⚠️ Skipped: {skipped_count}")
    print(f"❌ Failed: {failed_count}")
    print("=" * 50)


def process_batch_users(batch_size: int):
    print(f"📥 Fetching first {batch_size} unprocessed users from Supabase...")
    user_ids = fetch_unprocessed_user_ids(batch_size)

    if not user_ids:
        print("⚠️ No unprocessed users found (ai_profile IS NULL)")
        return

    print(f"✅ Found {len(user_ids)} unprocessed users")

    success_count = 0
    skipped_count = 0
    failed_count = 0

    for index, user_id in enumerate(user_ids, start=1):
        print(f"\n[{index}/{len(user_ids)}] Starting user {user_id}")
        try:
            result = process_user(user_id)
            if result is None:
                skipped_count += 1
            else:
                success_count += 1
        except Exception as exc:
            failed_count += 1
            print(f"❌ Failed for user {user_id}: {exc}")

    print("\n" + "=" * 50)
    print("RUN SUMMARY")
    print("=" * 50)
    print(f"✅ Success: {success_count}")
    print(f"⚠️ Skipped: {skipped_count}")
    print(f"❌ Failed: {failed_count}")
    print("=" * 50)


def parse_args():
    parser = argparse.ArgumentParser(description="Build AI profiles from Supabase onboarding data")
    parser.add_argument("--user", help="Process a single user_id")
    parser.add_argument(
        "--batch",
        type=int,
        help="Process first N unprocessed users where ai_profile is NULL",
    )
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    if args.user and args.batch is not None:
        raise SystemExit("Use either --user or --batch, not both.")

    if args.user:
        process_user(args.user)
    elif args.batch is not None:
        if args.batch <= 0:
            raise SystemExit("--batch must be a positive integer.")
        process_batch_users(args.batch)
    else:
        process_all_users()