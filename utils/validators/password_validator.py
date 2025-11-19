import re

def validate(password: str) -> bool:
    # Min length 8
    if len(password) < 8:
        return False
    
    # Must contain:
    #   1 capital
    capital_pattern = "[A-Z]+"
    if re.search(capital_pattern, password) is None:
        return False
    
    #   1 small
    small_pattern = "[a-z]+"
    if re.search(small_pattern, password) is None:
        return False
    
    #   1 number
    number_pattern = "[0-9]+" 
    if re.search(number_pattern, password) is None:
        return False
    
    #   1 special
    special_pattern = "\\W+"
    if re.search(special_pattern, password) is None:
        return False
    
    return True
