# the concept is of count of sets.
# first what is the count of sets ?
# we have learnt earlier the set is a 1(binary) representation is called as set . 
# example : we have binary of 5 is 101 and it has 2 set bits so the count of sets is 2.
# simple code to find the count of sets in a number :
# we are using naive solution to find the count of sets in a number :
# so what is naive solution ?

# Naive solution :
# travers through all the bits from lsb to msb and increment the count if the bit is set :
# simple code to find the count of sets in a number using naive solution :
def count_set_0f_bits(n):
    res = 0 
    while n:
        res = res + (n & 1)
        res+=1
        n = n//2 
        return res 
n = 5
print("count of sets in ", n, " is : ", count_set_0f_bits(n))
# this is the simple code to find the count of sets in a number using naive solution :
# we can also change the n according to our wish to find the count of sets of an number :
