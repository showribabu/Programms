# n = int(input())
# b = [int(x) for x in input().split()]
# k = int(input())

# maxx = 0
# for i in range(len(b)):
#     p = 0
#     count = 0
#     x = i
#     while count != k and x < len(b):
#         if b[p] == 1:
#             p += 1
#             x += 1
#         else:
#             count += 1
#             p += 1
#             x += 1
#     if p - 1 > maxx:
#         maxx = p - 1

# print(maxx)


def find_max_consecutive_ones(B, K):
    n = len(B)
    left = 0
    max_ones = 0
    count = 0

    for i in range(n):
        if B[i] == 0:
            count += 1

        while count > K:
            if B[left] == 0:
                count -= 1
            left += 1

        max_ones = max(max_ones, i - left + 1)

    return max_ones

# Example usage:
n = int(input())
b = [int(x) for x in input().split()]
k = int(input())
result = find_max_consecutive_ones(b,k)
print("Maximum number of consecutive 1's:", result)  # Output: 7

