from mlops_starter import classify_number


def test_classify_positive_number() -> None:
    assert classify_number(7) == "positive"


def test_classify_negative_number() -> None:
    assert classify_number(-4) == "negative"


def test_classify_zero() -> None:
    assert classify_number(0) == "zero"
