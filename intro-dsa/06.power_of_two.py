# CONCEPT: power of two :
# what is power of two :a number which is the result of multiplying 2 by itself is called a power of two :
# simple code using class :
class solution:
    def is_power_of_two(self,n):
        c = 0 
        while n>0:
            if n&1 == 1:
                c += 1
                n == n//2
            if c == 1:
                return True
        return False
    
n = 16
s = solution()
print("the number of solution is:", s.is_power_of_two(n))
#  this is the simple code to check if a number is power of two or not using python class and solution function :

# and we have simple and efficient code to check if a number is power of two or not using bit manipulation :
class solution:
    def is_power_of_two(self, n):
        if n <= 0:
            return False
        return (n & (n - 1)) == 0

n = 16
s = solution()
print("the number of solution is:", s.is_power_of_two(n)) 