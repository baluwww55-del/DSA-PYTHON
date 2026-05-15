# TWO ODD RECURRING :
# in an array the two elements will be odd recurring we have to find .
# we have several approach by using hashing or x-or but we are doing bitwise approach 
# simple code :
class Solution:
    def two_odd_num(self, Arr, N):
        x = 0
        s1 = 0
        s2 = 0

        # XOR of all elements
        for i in range(N):
            x = x ^ Arr[i]

        # Rightmost set bit
        x = x & -x

        # Divide into two groups
        for i in range(N):
            if x & Arr[i]:
                s1 = s1 ^ Arr[i]
            else:
                s2 = s2 ^ Arr[i]

        # Return in descending order
        if s1 >= s2:
            return [s1, s2]
        else:
            return [s2, s1]


Arr = [1,2,2,2,3,3,4,4,4,4,5,5,5]
N = len(Arr)

obj = Solution()
print("The two odd occurring numbers are:", obj.two_odd_num(Arr, N))
# this is the simple approach to find the two odd times repeating elements in an array .
