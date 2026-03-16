# Placeholder for template engine service

def get_template_for_platform(platform):
    # Example: could be a lookup or template file
    templates = {
        "instagram": "Instagram Template",
        "facebook": "Facebook Template",
        "linkedin": "LinkedIn Template"
    }
    return templates.get(platform, "Default Template")
