#!/sh/bin/pyenv python3
# Consider the sequence U(n, x) = x + 2x**2 + 3x**3 + .. + nx**n where x is a real number and n a positive integer.

# When n goes to infinity and x has a correct value (ie x is in its domain of convergence D), U(n, x) goes to a finite limit m depending on x.

# Usually given x we try to find m. Here we will try to find x (x real, 0 < x < 1) when m is given (m real, m > 0).

# Let us call solve the function solve(m) which returns x such as U(n, x) goes to m when n goes to infinity.

# Examples:
# solve(2.0) returns 0.5 since U(n, 0.5) goes to 2 when n goes to infinity.

# solve(8.0) returns 0.7034648345913732 since U(n, 0.7034648345913732) goes to 8 when n goes to infinity.

# Note:
# You pass the tests if abs(actual - expected) <= 1e-12

def solve(m):
    # Define a function to calculate U(n, x) given x and n
    def U(x):
        return x / (1 - x)**2
    
    # Define the precision value
    epsilon = 1e-12
    
    # Initialize variables for binary search
    low, high = 0, 1
    
    # Perform binary search to find x
    while high - low > epsilon:
        mid = (low + high) / 2
        if U(mid) < m:
            low = mid
        else:
            high = mid

    return (low + high) / 2

# Test cases
print(solve(2.0))  # Output: 0.5
print(solve(8.0))  # Output: 0.7034648345913732
