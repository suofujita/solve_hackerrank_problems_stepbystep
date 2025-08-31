def swap_case(s):
    out_string = ''
    for char in s:
        if char.isupper():
            out_string += char.lower()
        else:
            out_string += char.upper()
    return out_string

s = input()
result = swap_case(s)
print(result)