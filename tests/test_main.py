from mlops_starter import classify_number


def test_classify_positive_number() -> None:
    assert classify_number(7) == "положительное"


def test_classify_negative_number() -> None:
    assert classify_number(-4) == "отрицательное"


def test_classify_zero() -> None:
    assert classify_number(0) == "ноль — стоит на нейтральной полосе"
