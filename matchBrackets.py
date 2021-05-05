s = input('enter a string: ')


def checkString(t):
    check = 0

    for c in t:
        if c == '(':
            check += 1
        if c == ')':
            check -= 1
            if(check < 0):
                return False

    if(check != 0):  # if number are not equal
        return False

    return True


print(checkString(s))
