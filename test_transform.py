from transform import clean_country_name


def test_clean_country_name():
    assert clean_country_name(" egypt ") == "EGYPT"


def test_clean_country_name_null():
    assert clean_country_name(None) == "UNKNOWN"
