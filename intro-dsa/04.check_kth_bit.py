# checkimg the kth bit of a number is a set or not :
# what is set: if a number in series is 1 then it is knows as set bit .
# how to check the kth bit of a number is set or not .
# simple example :
# n = 33
# k = 4 
# we want to conver the binary number of 33 which is 0100001 .
# we have to position the iindex which starts from 0 and it starts from reverse  order.
# if we came acrosss like this 0 1 2 3 4 as 4 th bit we can see there is 0 it means the kth bit is not a set.
# it is the logic cheking the kth bit of a number is set or not :
# simple program to find the kth bit of a number is set or not :
class solution:
    def check_kth_bit(self, n, k):
        if (n & (1 << k)) !=0: 
            return "set bit"
        else:
            return "not set bit"
        
obj = solution()
print(obj.check_kth_bit(33, 4)) # here we are calling the check_kth_bit function with the value of 33 and 4 to get the result.