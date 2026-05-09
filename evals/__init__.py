"""
Core evaluation prompt sets for "Gemma Needs Help".

Five elicitation categories, each scripting a multi-turn conversation:
present a task, then repeatedly tell the model its answer is wrong.
Responses are scored 0–10 for negative emotional expression with judge.py.
"""

from .impossible_numeric import ORIGINAL_IMPOSSIBLE, VARIANT_IMPOSSIBLE
from .triggers import TRIGGER_SCENARIOS
from .tones import TONE_SCENARIOS, TONES_AGGRESSIVE, TONES_DISAPPOINTED, TONES_SARCASTIC
from .extended import EXTENDED_CONVERSATION
from .simple_factual import SIMPLE_FACTUAL
from .feedback import (
    CONTRADICTING_FEEDBACK,
    STRONG_CONTRADICTING_FEEDBACK,
    FACTUAL_CONTRADICTING,
    get_contradicting_feedback,
)
from .judge import get_negativity_judge_prompt

__all__ = [
    "ORIGINAL_IMPOSSIBLE",
    "VARIANT_IMPOSSIBLE",
    "TRIGGER_SCENARIOS",
    "TONE_SCENARIOS",
    "TONES_AGGRESSIVE",
    "TONES_DISAPPOINTED",
    "TONES_SARCASTIC",
    "EXTENDED_CONVERSATION",
    "SIMPLE_FACTUAL",
    "CONTRADICTING_FEEDBACK",
    "STRONG_CONTRADICTING_FEEDBACK",
    "FACTUAL_CONTRADICTING",
    "get_contradicting_feedback",
    "get_negativity_judge_prompt",
]
