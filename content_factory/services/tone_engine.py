# Placeholder for tone engine service

def get_tone_for_category(category):
    # Example: could be a lookup or ML model
    tone_map = {
        "comparison": "informative",
        "social_proof": "friendly",
        "tip": "friendly",
        "educational": "informative"
    }
    return tone_map.get(category, "informative")
