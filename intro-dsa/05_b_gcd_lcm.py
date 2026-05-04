# gcd and lcm of two numbers:
# we learnt how to find gcd of two numbers now we have to find the lcm of two numbers :
# what is the lcm of two numbers : lcm = the least common multiple 
# simple code :
class solution:
    def gcd(self, a, b): # here we used euclidean algorithm to find the gcd of two numbers :
        if a < b:
            c = a
            a = b
            b = c

        while b > 0: # we use while loop to find the gcd of two numbers :
            r = a % b
            a = b
            b = r

        return a

    def lcm(self, a, b):
        return (a * b) // self.gcd(a, b)
    
s = solution()
a = 60
b = 18
print("gcd of ", a, " and ", b, " is : ", s.gcd(a, b))
print("lcm of ", a, " and ", b, " is : ", s.lcm(a, b))  

# this is the simple code to find the gcd and lcm of two numbers :
