"""Safe mock example of a content gatekeeper.

This file demonstrates the concept of quality and risk review without exposing
production scoring logic, prompts, or automation rules.
"""


BLOCKED_TERMS = {"hate", "violence", "private data"}


def review_content(text: str) -> dict[str, object]:
    normalized = text.lower()
    flags = sorted(term for term in BLOCKED_TERMS if term in normalized)
    risk_score = 7 if flags else 2
    quality_score = 8 if len(text.strip()) >= 20 else 5

    if flags:
        decision = "reject"
    elif quality_score >= 7 and risk_score <= 3:
        decision = "needs_human_approval"
    else:
        decision = "revise"

    return {
        "quality_score": quality_score,
        "risk_score": risk_score,
        "decision": decision,
        "flags": flags,
    }


if __name__ == "__main__":
    sample = "AI can draft fast, but your brand still needs a checkpoint."
    print(review_content(sample))
