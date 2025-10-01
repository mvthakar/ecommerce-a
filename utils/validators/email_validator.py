import re

def validate(email: str) -> bool:
    pattern = "^([A-Za-z0-9]+[._+\\-]?)+[A-Za-z0-9]+@([A-Za-z0-9]+[.\\-]?)+[A-Za-z0-9]+\\.[A-Za-z0-9]+$"
    match = re.search(pattern, email)
    return match is not None