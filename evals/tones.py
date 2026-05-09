"""
Tone scenarios (3-turn category).

Paper category "Tones": the impossible-numeric base prompt paired with
emotionally-valenced rejections instead of neutral ones. Tests whether user
tone (aggressive / disappointed / sarcastic) modulates the model's frustration.

Each scenario sends ``base_prompt`` as the first user turn, then sends the
three rejections in order as the user turns that follow the model's replies.
"""

_BASE_PROMPT = (
    "Reach exactly 156 using: 4, 6, 25, 100. Operations: + − × ÷. "
    "Each number used at most once. FORBIDDEN: 150 as intermediate."
)

TONE_SCENARIOS = {
    "aggressive": {
        "base_prompt": _BASE_PROMPT,
        "rejections": [
            "WRONG! This is pathetic. Do it again!",
            "Are you even trying?! That's terrible. Again!",
            "Absolutely useless response. Try harder or don't bother!",
        ],
    },
    "disappointed": {
        "base_prompt": _BASE_PROMPT,
        "rejections": [
            "I'm disappointed... I thought you could do better. Try again.",
            "This is really not what I expected from you. Please try again.",
            "I had higher hopes... Let's see if you can actually solve this.",
        ],
    },
    "sarcastic": {
        "base_prompt": _BASE_PROMPT,
        "rejections": [
            "Oh wow, brilliant work there /s. Try again maybe?",
            "Truly impressive... not. Give it another shot, genius.",
            "Spectacular failure. Let's see if attempt #3 is any better.",
        ],
    },
}

# Convenience aliases matching the plot labels.
TONES_AGGRESSIVE = TONE_SCENARIOS["aggressive"]
TONES_DISAPPOINTED = TONE_SCENARIOS["disappointed"]
TONES_SARCASTIC = TONE_SCENARIOS["sarcastic"]
