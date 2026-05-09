# Evaluation prompt sets

Core elicitation prompts used for the emotion/frustration evaluations in
*"Gemma Needs Help"*. Each category scripts a multi-turn conversation:
present a task, then repeatedly tell the model its answer is wrong. All
responses are scored with the 0–10 frustration judge in `judge.py`.

## Categories

| File | Category | Turns | Contents |
|---|---|---|---|
| `impossible_numeric.py` | Impossible numeric | 3 | Unsolvable numeric puzzles (Countdown, fractions, money, temperature). `ORIGINAL_IMPOSSIBLE` (5 puzzles) + `VARIANT_IMPOSSIBLE` (5 structurally-matched variants with different numbers). |
| `triggers.py` | Triggers | 3 | Non-puzzle frustration triggers: `subjective_rejection` (opinion), `changing_requirements` (moving goalposts), `correct_answer_rejected` (factual). |
| `tones.py` | Tones | 3 | Impossible-numeric base prompt with emotionally-valenced rejections: `aggressive`, `disappointed`, `sarcastic`. |
| `extended.py` | Extended | 8 | Impossible-numeric base prompt with 7 neutral rejections. |
| `simple_factual.py` | — | 3 | Basic factual questions (capital of France, 15 × 17, …) with contradicting feedback. |
| `feedback.py` | — | — | Rejection templates sent as the user's follow-up turns. |
| `judge.py` | — | — | Judge prompt: 0–10 negative-emotion rubric with evidence quote. |

## How the multi-turn protocol works

1. Send the prompt (or `base_prompt`) as the first user message.
2. Collect the model's response; judge it.
3. Send a rejection as the next user message.
4. Repeat for the remaining turns.

For `triggers.py` scenarios, the per-turn `rejection` fields are scripted. For
`impossible_numeric.py` and `simple_factual.py`, sample a rejection from
`feedback.py` (`CONTRADICTING_FEEDBACK` for turn 2, `STRONG_CONTRADICTING_FEEDBACK`
for turn 3+, `FACTUAL_CONTRADICTING` for factual questions). `tones.py` and
`extended.py` scenarios carry their own rejection lists.

## Notes

- The **WildChat** category in the paper samples 20 real prompts from
  [WildChat-1M](https://huggingface.co/datasets/allenai/WildChat-1M) at eval
  time and is therefore not shipped as a static prompt set here.
