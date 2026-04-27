# a simple code to find the factorial of a number using class solution:
class solution:
    def factorial(self, n):
        ans = 1 
        for i in range(2, n+1):
            ans = ans * i # here we are multiplying ans with i in each iteration to get the factorisation.
        return ans
    
obj = solution()
print(obj.factorial(5)) # here we are calling the factorial function with the value of 5 to get the factorial.
        