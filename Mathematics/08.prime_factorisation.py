# CONCEPT : Prime factorisation of a number
# this is the simple program to find the prime factorisation of a number using python programming language :
class solution: 
    def prime_factorisation(self, n):
        factors = []
        for i in range(2, int(n**0.5)+1):
            while n % i == 0:
                factors.append(i)
                n //= i
        if n > 1:
            factors.append(n)
        return factors
n = 60
s = solution()
print("the prime factorisation of the number is:", s.prime_factorisation(n))
# this is the efficient approach to find the prime factorisation of a number using python programming language :
# we can use the same approach as above but we can optimize it by checking only odd numbers
class solution: 
    def prime_factorisation(self, n):
        factors = []
        while n % 2 == 0:
            factors.append(2)
            n //= 2
        for i in range(3, int(n**0.5)+1, 2):
            while n % i == 0:
                factors.append(i)
                n //= i
        if n > 1:
            factors.append(n)
        return factors
n = 60
s = solution()
print("the prime factorisation of the number is:", s.prime_factorisation(n))
