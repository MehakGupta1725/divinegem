# recommendation_engine.py

from gemstones import gemstones

# Concern-based recommendations
concern_mapping = {
    "Career": "Emerald",
    "Finance": "Yellow Sapphire",
    "Love & Marriage": "Diamond",
    "Health": "Pearl",
    "Education": "Emerald"
}

# Zodiac-based recommendations
zodiac_mapping = {
    "Aries": "Red Coral",
    "Taurus": "Diamond",
    "Gemini": "Emerald",
    "Cancer": "Pearl",
    "Leo": "Ruby",
    "Virgo": "Emerald",
    "Libra": "Diamond",
    "Scorpio": "Red Coral",
    "Sagittarius": "Yellow Sapphire",
    "Capricorn": "Blue Sapphire",
    "Aquarius": "Blue Sapphire",
    "Pisces": "Yellow Sapphire"
}


def get_recommendation(zodiac, concern):
    """
    Returns:
    {
        "primary": ...,
        "alternative": ...,
        "reason": ...
    }
    """

    primary = concern_mapping.get(concern)

    alternative = zodiac_mapping.get(zodiac)

    if primary == alternative:
        reason = (
            f"Both your concern ({concern}) and zodiac sign "
            f"({zodiac}) indicate {primary} as a suitable gemstone."
        )
    else:
        reason = (
            f"{primary} is recommended based on your primary concern "
            f"({concern}), while {alternative} aligns with your zodiac "
            f"sign ({zodiac})."
        )

    return {
        "primary": primary,
        "alternative": alternative,
        "reason": reason
    }