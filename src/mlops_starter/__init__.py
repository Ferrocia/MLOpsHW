"""Small examples for MLOps coursework."""


def classify_number(value: int) -> str:
    """Return whether an integer is positive, negative, or zero."""
    if value > 0:
        return "positive"
    if value < 0:
        return "negative"
    return "zero"
