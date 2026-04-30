# program to find the gcd of two numbers : 
# what is the gcd of two numbers : gcd = the gretest common divisor 
# how to find the gcd of two number :
# simnple example :
# a = 12
# b = 15
# the common divisor of 12 and 15 are 1, 3 and 
# the greatest common divisor is 3
# simple code to find the greatdest common divisor of two numbers >
a = 12
b = 15

# swap if a is smaller
if a < b:
    c = a
    a = b
    b = c

while b > 0:
    r = a % b
    a = b
    b = r

print(a)