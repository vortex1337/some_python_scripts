def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True
def count_primes(num):
    res = 0
    for i in range(3, num):
        if is_prime(i):
            res+=1
    return res
