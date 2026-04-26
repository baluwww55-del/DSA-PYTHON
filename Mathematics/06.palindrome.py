n = input("enter n:")
if n == n[::-1]: # here we are checking if the string n is equal to its reverse n[::-1].
    print("it is a palindrome:")
else:
    print("it is not a palindrome:")
# so this is a simple python program to check if the given string is a palindrome or not by taking using stringslicing.

# we have another case where if the input is an integer then we can code it like this:
class solution:
    def ispalindrome(self, n):
        n1 = 0 
        m = n 
        while m>0 :
            n1 = n*10 + m%10 # here we are mutliplying n1 by 10 and adding the last digit of m to n1.
            m = m//10

        if n == n1:
            return True
        else:
            return False