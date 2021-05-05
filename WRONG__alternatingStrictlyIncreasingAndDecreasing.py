""" 
  Write a function accordian(l) that takes as input a list of integer l and returns
True if the absolute difference between each adjacent pair of elements alternates
between increasing strictly and decreasing strictly.
 """


def check_alternate_strictly_increasing_decreasing(listToCheck: list):
    if(len(listToCheck) <= 2):
        return True

    length = len(listToCheck)

    checker = 'increasing' if (
        listToCheck[1] - listToCheck[0]) > 0 else 'decreasing'

    for index, value in enumerate(listToCheck):
        if(index < length - 1):  # check till one less than length
            print('checking', listToCheck[index+1], "-", listToCheck[index])

            if(checker == 'increasing' and (listToCheck[index + 1] - listToCheck[index]) < 0):
                print(listToCheck[index + 1], "-",
                      listToCheck[index], "<", 0, "therefore exiting")
                return False
            else:
                print(listToCheck[index + 1], "-",
                      listToCheck[index], ">", 0, "therefore continuing")

            if(checker == 'decreasing' and (listToCheck[index + 1] - listToCheck[index]) > 0):
                print(listToCheck[index + 1], "-",
                      listToCheck[index], ">", 0, "therefore exiting")
                return False
            else:
                print(listToCheck[index + 1], "-",
                      listToCheck[index], "<", 0, "therefore continuing")

            checker = 'increasing' if checker == 'decreasing' else 'increasing'

    return True


li = list(map(int, input('enter a list of numbers seperated by space: ').split()))

print(check_alternate_strictly_increasing_decreasing(li))
