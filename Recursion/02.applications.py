# Applications of recursion :
# when a function calls itself is known as recursion 
# we have some applications of recursion :
#  1. many algorithm technique are based on recursions :
# 1. dynamic programming 2. back tracking 3. divide and conquer (binary search ,quick sort and  merge sort )
# 2. many problems inherently recursive 
# tower of hanoi 
# dfs based traversal (dfs of graph tree )
# some practice code for recursion :
def fun(n):
    if n == 0:
        return 
    print(n)
    fun(n-1)
fun(3)
# so this is the little eg of recursion 
# another example :
def fun(n):
    if n == 0 :
        return 
    print(n)
    fun(n-1)
    print(n)
fun(3)
# so here the code will print 3,2,1 and at last it will stich to 1 and it will print forward as 1,2,3
# lets take another example of code :
def fun(n):
    if n == 0:
        return 
    fun(n-1)
    print(n)
    fun(n-1)
fun(3)
# here little critical code and its little tough to guess the output because we have used argument  before printing and after tht also we used.
# as we know there if fun(n-1) it will go upto fun(0) until its return but 1 sticks after that it wil print 1
# after printing 1 it will print positive because zero will negative return it will print 2 . 
# and after tht it will print 1 because of fun(n-1) after it will print 3 and after tht it will print 121 as it is .