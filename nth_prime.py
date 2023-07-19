def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

n = int(input("Enter the value of n (1 to 100): "))

count = 0
number = 2

while count < n:
    if is_prime(number):
        count += 1
        if count == n:
            print(f"The {n}th prime number is: {number}")
            break
    number += 1
