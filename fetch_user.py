from supabase_client import supabase

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
        .single()# allows us to fetch a single record instead of an array
        .execute()# executes the query and returns the response
    )

    if not response.data:
        raise Exception("User not found")

    return response.data