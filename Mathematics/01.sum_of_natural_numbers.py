# program to find the sum of first n natural numbers by taking input from the user.
# it will give the sum of numbers from 1 to n.
# n is the number of natural numbers we want to sum up.

n = int(input("Enter a number: "))
n = n * (n + 1) // 2
print("the sum of first n natural numbers is:",n)

# for to get sum of the natural number we took the formula which we learnt in school.
# the formula is n(n+1)/2 where n is the number of natural numbers we want to sum up.
# so we applied like this formula n = 54 
# 54 * (54+1)//2 = 1485 this is the answer of the sum of first 54 natural numbers.
