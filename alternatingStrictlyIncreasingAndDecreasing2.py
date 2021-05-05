""" 
  Write a function accordian(l) that takes as input a list of integer l and returns
  True if the absolute difference between each adjacent pair of elements alternates
  between increasing strictly and decreasing strictly.
"""


def check_alternate_strictly_increasing_decreasing(li: list):
    length = len(li)
    pairs = zip(li[:], li[1:])

    # 1 for increasing, 0 for decreasing
    PREVIOUS_CHECK = 1 if li[1] - li[0] > 0 else 0
    # [1, 2, 3, 4]
    list_for_loop = list(pairs)[1:]
    print('prevCheck is', PREVIOUS_CHECK, 'for first pair')
    print('now checking for list', list_for_loop)
    print(len(list_for_loop))
    for (first, second) in list_for_loop:
        CURRENT_CHECK = second - first

        print('checking for pair', first, second)

        if((PREVIOUS_CHECK == 1 and CURRENT_CHECK > 0) or (CURRENT_CHECK == 0 and second - first < 0)):
            print('result is false for current pair')
            return False

        PREVIOUS_CHECK = CURRENT_CHECK

    return True


li = list(map(int, input('enter a list of numbers seperated by space: ').split()))

print(check_alternate_strictly_increasing_decreasing(li))

# print([1, 2, 3, 4, 5, 6][::2])
# print([1, 2, 3, 4, 5, 6][1::2])
