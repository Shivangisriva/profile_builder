from supabase_client import supabase


def fetch_all_user_ids():
    response = (
        supabase
        .table("profiles")
        .select("user_id")
        .execute()
    )

    rows = response.data or []
    seen = set()
    user_ids = []

    for row in rows:
        user_id = row.get("user_id")
        if user_id and user_id not in seen:
            seen.add(user_id)
            user_ids.append(user_id)

    return user_ids

def fetch_user_onboarding(user_id: str):

    response = (
        supabase
        .table("profiles")
        .select("""
            basic_information,
            location_and_future_plans,
            work_and_life_stage,
            education_and_intellectual_life,
            relationship_direction_and_readiness,
            family_and_children,
            lifestyle,
            values_faith_and_culture,
            political_and_social_outlook,
            physical_and_attraction
        """)
        .eq("user_id", user_id)
        .execute()# executes the query and returns the response
    )

    rows = response.data or []

    if len(rows) == 0:
        raise ValueError(f"No onboarding record found in 'profiles' for user_id={user_id}")

    if len(rows) > 1:
        raise ValueError(
            f"Expected one onboarding record in 'profiles' for user_id={user_id}, found {len(rows)}"
        )

    return rows[0]