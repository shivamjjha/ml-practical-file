# 'difference' bw two consecutive should strictly increase
def check_string_increasing_list(l):
    length = len(l)
    diff = 0
    for index, value in enumerate(l):
        if(index < length - 1):  # check till one less than length
            d = l[index+1] - l[index]
            # print(d)
            if(d <= diff):
                return False
        diff = d
        # print('diff', diff)

    return True


n = list(map(int, input('enter a list seperated by space: ').split()))

print(check_string_increasing_list(n))
