if __name__ == '__main__':
    s = input()
# method 1 easy to understand but long long code
    hasAlphanum = False
    hasAlpha = False
    hasDigit = False
    hasLowerCase = False
    hasUpperCase = False
    for char in s:
        if char.isalnum():
            hasAlphanum = True
            break
    print(hasAlphanum)

    for char in s:
        if char.isalpha():
            hasAlpha = True
            break
    print(hasAlpha)

    for char in s:
        if char.isdigit():
            hasDigit = True
            break
    print(hasDigit)

    for char in s:
        if char.islower():
            hasLowerCase = True
            break
    print(hasLowerCase)

    for char in s:
        if char.isupper():
            hasUpperCase = True
            break
    print(hasUpperCase)


# method 2 using any() clear code
    print(any(char.isalnum() for char in s))
    print(any(char.isalpha() for char in s))
    print(any(char.isdigit() for char in s))
    print(any(char.islower() for char in s))
    print(any(char.isupper() for char in s))
