#!/usr/bin/python
def roman_to_int(roman_string):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    result = 0
    for i in range(len(roman_string)):
        value = roman_dict[roman_string[i]]
        if i < len(roman_string) - 1:
            if roman_dict[roman_string[i]] < roman_dict[roman_string[i + 1]]:
                result -= value
        else:
            result += value
    return result
