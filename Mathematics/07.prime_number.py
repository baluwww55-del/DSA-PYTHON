# CONCEPT: prime number :
# what is prime number : a prime number is a natural which is divisible by only and 1 and itself :
# simple code:
class solution:
    def is_prime(self,n):
        i = 2 
        if n == 1:
            return False
        while i*i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

n = 11
s = solution()
print("the prime number is :", s.is_prime(n))
# simple code to check if a number is prime or not using python function :
