def sieve_of_eratosthenes(n):
    primes = [True] * (n+1)
    print(primes)
    primes[0] = primes[1] = False

    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1

    return primes

def is_prime(n):
    if n < 2:
        return False

    primes = sieve_of_eratosthenes(n)
    return primes[n]

# Test the function
num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
