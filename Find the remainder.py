# Task:
# Write a function that accepts two integers and returns the remainder of dividing the larger value by the smaller value.

# Division by zero should return an empty value.

# Examples:
# n = 17
# m = 5
# result = 2 (remainder of `17 / 5`)

# n = 13
# m = 72
# result = 7 (remainder of `72 / 13`)

# n = 0
# m = -1
# result = 0 (remainder of `0 / -1`)

# n = 0
# m = 1
# result - division by zero (refer to the specifications on how to handle this in your language)

def remainder(n, m):
    if m == 0 or n == 0:
        return None if m == 0 else 0

    larger = max(n, m)
    smaller = min(n, m)

    return larger % smaller

# Examples
test_cases = [
    (17, 5),    # Result: 2
    (13, 72),   # Result: 7
    (0, -1),    # Result: 0
    (0, 1)      # Result: None (division by zero)
]

for n, m in test_cases:
    result = remainder(n, m)
    print(f"n = {n}, m = {m}, result = {result}")