def build_agent_input(user_data: dict):
           # transformation layer.
           # we want to convert the raw onboarding data into a format that's more digestible for the AI model.
    return {
        "demographics": user_data["basic_information"],
        "location": user_data["location_and_future_plans"],
        "career_stage": user_data["work_and_life_stage"],
        "intellectual_profile": user_data["education_and_intellectual_life"],
        "relationship_readiness": user_data["relationship_direction_and_readiness"],
        "family_preferences": user_data["family_and_children"],
        "lifestyle": user_data["lifestyle"],
        "values": user_data["values_faith_and_culture"],
        "politics": user_data["political_and_social_outlook"],
        "attraction_profile": user_data["physical_and_attraction"],
    }