# Iterative power of binary exponentiation .
# simple code :
def power(x, n):
    res = 1

    while n > 0:
        # If n is odd, multiply result by x
        if n % 2 != 0:
            res = res * x

        # Square x and halve n
        x = x * x
        n = n // 2

    return res


# Driver Code
x = 3
n = 4
print(power(x, n))   # Output: 81
# so this is the simple code of iterative power of binary exponentiation .