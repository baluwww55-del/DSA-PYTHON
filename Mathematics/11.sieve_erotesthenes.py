# Sieve erotesthenes :
# simple code :
def sieve_of_eratosthenes(n):
    # Create a boolean array and mark all numbers as prime initially
    prime = [True] * (n + 1)

    # 0 and 1 are not prime numbers
    if n >= 0:
        prime[0] = False
    if n >= 1:
        prime[1] = False

    i = 2
    while i * i <= n:
        if prime[i] == True:
            # Mark all multiples of i as non-prime
            for j in range(i * i, n + 1, i):
                prime[j] = False
        i += 1

    # Collect all prime numbers
    res = []
    for i in range(2, n + 1):
        if prime[i] == True:
            res.append(i)

    return res


# Driver Code
n = 30
print("Prime numbers up to", n, "are:")
print(sieve_of_eratosthenes(n))
