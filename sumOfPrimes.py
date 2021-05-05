import math


def check_prime(t):
    if(t == 1):
        return False
    limit = math.sqrt(t)

    for i in range(2, int(limit) + 2):
        if(t % i == 0):
            return False

    return True


def sum_of_primes(l):
    sum = 0
    for p in l:
        if(check_prime(p)):
            print(p, 'is prime')
            sum += p

    return sum


n = map(int, input('enter a list seperated by space: ').split())

print('answer: ', sum_of_primes(n))
