def capital_case(x):
    return x.capitalize()


def lower_case(x):
    return x.lower()


def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'


def test_lower_case():
    assert lower_case("SemaphoRE") == "semaphore"

