def roman_to_integer(s):
    roman_to_integer_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    num = 0
    prev_value = 0

    for i in range(len(s) - 1, -1, -1):
        value = roman_to_integer_dict[s[i]]
        if value < prev_value:
            num -= value
        else:
            num += value
        prev_value = value

    return num

# Example usage:
n = input("Enter the Roman numeral: ")
result = roman_to_integer(n)
print("The equivalent number is:", result)
