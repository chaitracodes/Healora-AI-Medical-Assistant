def get_ai_response(user_input: str) -> str:
    text = user_input.lower()

    if any(word in text for word in ["fever", "cold", "cough"]):
        return (
            "You may be experiencing flu-like symptoms.\n\n"
            "Suggestions:\n"
            "- Stay hydrated\n"
            "- Take proper rest\n"
            "- Monitor your temperature\n\n"
            "Consult a doctor if symptoms persist or worsen."
        )

    if any(word in text for word in ["headache", "migraine", "nausea"]):
        return (
            "Headaches can be caused by stress, dehydration, or lack of sleep.\n\n"
            "Suggestions:\n"
            "- Drink water\n"
            "- Rest in a quiet place\n"
            "- Avoid screens\n\n"
            "Seek medical advice if severe or recurring."
        )

    if any(word in text for word in ["stomach", "vomiting", "diarrhea"]):
        return (
            "These symptoms may indicate digestive discomfort.\n\n"
            "Suggestions:\n"
            "- Eat light food\n"
            "- Avoid oily or spicy meals\n"
            "- Stay hydrated\n\n"
            "Consult a doctor if dehydration occurs."
        )

    return (
        "Please describe your symptoms clearly.\n\n"
        "Healora provides general health guidance and is not a diagnostic tool."
    )
