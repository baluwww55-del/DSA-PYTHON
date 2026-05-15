# CONCEPT : finding the odd number in a list of numbers :
# we have a list of numbers and we have to find the odd number in that list of numbers :
# example : we have a list of numbers [1, 2, 3, 4, 5] and we have to find the odd number in that list of numbers :
# so the odd number in that list of numbers is 1, 3, 5  
# simple code to find the odd number in a list using function :
from os import name
def findodd(l):
    res = name 
    for x in l:
        count = l.count(x)
        if count % 2 != 0:
            res = x
            return res 
        
l = [1,1,1,1,2,2,3,3,3,3,4,5,]
print("the odd number in the list is : ", findodd(l)) 
# this is the simple code to find the odd number in a list using python function :

# we have also another method to find the odd number in a list of numbers using bitwise operator :
def findodd(l):
    res = 0 
    for x in l:
        res = res^x
        return res 
l = [1,1,1,1,2,2,3,3,3,3,4,5,5,5]
print("the odd number in the list is : ", findodd(l))
# this is the simple code to find the odd number in a list using bitwise operator :
# this method is more efficient than the previous method because it has a time complexit of O(n) .
