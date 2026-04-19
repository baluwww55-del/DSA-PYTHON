# 1. what is meant by recursion ?
# recursion is a programming technique where a function calls itself in order too solve the prolem.
#  example :
def fun(n):
    if n == 1:
        return
    for i in range(n):
        print("gfg")
        fun(n//2)   # use integer divisionṇ

fun(4)
# here we have t(n) = 2t(n/2) + 0(1)
# so the answer is 0(1)

# another example :
def fun(n):
    if n == 1:
        return 
    for i in range(n):
        print("balu")
        fun(n-1)
fun(4)
# the output prints fourty times as "balu" because the we give fun(4) it prints like factorial of 
# 4 4*0, 4*3, 4*2, 4*1 it prints like this if we calculate the sum we get 40 times as "balu".

# another example : 
def fun(n):
    if n == 1:
        return
    for i in range(n):
        print("n")
        fun(n-1)
fun(4)
# the output prints like 4*0, 4*3, 4*2, 4*1 it prints like this if we calculate the sum we get 40 times as "n".
# so this is the sum of tree method of recursion.