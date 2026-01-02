def moderate_text(text: str) -> dict:
    
    # Mock moderation module.


    banned_keywords = ["hate", "kill", "violence"]

    for word in banned_keywords:
        if word in text.lower():
            return {
                "allowed": False,
                "flag": "unsafe_content"
            }

    return {
        "allowed": True,
        "flag": None
    }
