# Computing power :
# it is the concept in python used to compute the power of an given number 
# eg: n = 3 x = 4 3^4 = 81 
# this is the concept we have to write / implement this using the code 
# we use naive solution for this :
def print_power_set(x,n):
    res = 1
    for i in range(n):
        res = res*x
    return res 
n = 3
x = 4 
print("the solution", print_power_set(x,n))
# so this is not an good / efficient approach to implement this because it takes time complexity theta of n and aux 1 .
# so we are using better approach for this by bitwise operator and recursion .
def print_power_set(x,n):
    if n == 0 :
        return 1 
    temp = print_power_set(x,n//2)
    temp = temp*temp
    if (n%2==0):
        return temp
    else:
        return temp*x
    
n = 4 
x = 5
print("the solution", print_power_set(x,n))
# so this is the clear and efficient approach of the concept of computing power by using recursion and bitwise as well 

