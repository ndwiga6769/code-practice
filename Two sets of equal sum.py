# Task
# If possible, divide the integers 1,2,…,n into two sets of equal sum.

# Input
# A positive integer n <= 1,000,000.

# Output
# If it's not possible, return [ ] (Javascript and Python) or ( ) (Python) or [[],[] ] (Java, C#) or None (Scala). If it's possible, return two disjoint sets. Each integer from 1 to n must be in one of them. The integers in the first set must sum up to the same value as the integers in the second set. The sets can be returned in a tuple, list, or array, depending on language.

# Examples:
# For n = 8, valid answers include:

# [1, 3, 6, 8], [2, 4, 5, 7] (or [[1, 3, 6, 8], [2, 4, 5, 7]])

# [8, 1, 3, 2, 4], [5, 7, 6]

# [7, 8, 3], [6, 1, 5, 4, 2], and others.

# For n = 9 it is not possible. For example, try [6, 8, 9] and [1, 2, 3, 4, 5, 7], but the first sums to 23 and the second to 22. No other sets work either.

def create_two_sets_of_equal_sum(n): 
    ## Divide the numbers 1,2,…,n into two sets of equal sum.
    ## If it's not possible, return [ ] or ( ).
    total_sum = n * (n + 1) // 2

    if total_sum % 2 != 0:
        return []

    target_sum = total_sum // 2
    set1, set2 = [], []
    set_sum = 0

    for i in range(n, 0, -1):
        if set_sum + i <= target_sum:
            set_sum += i
            set1.append(i)
        else:
            set2.append(i)

    if set_sum == target_sum:
        return [set1, set2]
    else:
        return []