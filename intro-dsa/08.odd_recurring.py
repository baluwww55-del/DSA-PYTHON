# this is the simple program to check the single odd number in an array using python programming language :
class solution:
    def get_single(self, arr):
        n = len(arr)
        ans = 0 
        for i in range(n):
            ans = ans^arr[i]
        return ans 
arr = [1,2,3,4,1,2,3]
s = solution()
print("the single odd number is:", s.get_single(arr))

# this is the efficient approach to find the single odd repeating number in an array using x-or bitwise operator in python .
# we have multiple approaches using hashmap and all but the efficient approach depends on the time complexity and the x-or time complexity is O(n) and space complexity is O(1) because we are using only one variable to store the result of x-or operation .
