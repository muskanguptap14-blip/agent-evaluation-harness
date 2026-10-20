def clean_text(value):
    if value is None:
        return ""
    text = str(value).strip()
    return text
