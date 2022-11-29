#!/usr/bin/python3
def uppercase(str):
    result = list(result)
    for ch in str:
        if ord(ch) >= 65:
            result += chr(ord(ch) - 32)
        return result
