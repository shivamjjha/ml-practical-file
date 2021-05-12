def revrse_number(s):
    return "".join(list(reversed(s)))


n = int(input())
if(n > 0):
    print(revrse_number(str(n)))
else:
    print('number is < 0')
