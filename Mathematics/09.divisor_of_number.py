# THE DIVISOR OF NUMBERS :
# what is the divisor of a number ?
# divisor of a number is a concept tht n of an number is divisible by which number .
# simple example program :
# THE DIVISORS OF A NUMBER

def print_divisors(n):
    print(f"Divisors of {n} are:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)

n = 6
print_divisors(n)
# there is an efficient approach because this approach takes time complexity more 
# simple example of efficient approach 
def print_divisors(n):
    i = 1
    while i * i <= n:
        if n % i == 0:
            print(i)

            # Print the paired divisor if it is different
            if i != n // i:
                print(n // i)

        i += 1


# Example usage
n = 36
print("Divisors of", n, "are:")
print_divisors(n)
# so this is an clear and efficient approach of divisor of a numbers :
