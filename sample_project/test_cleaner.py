from cleaner import clean_text


def test_strips_whitespace():
    assert clean_text("  hello world  ") == "hello world"


def test_empty_string_is_safe():
    assert clean_text("   ") == ""
    assert clean_text("") == ""
