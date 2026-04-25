# write a simple python program to count the number of digits by taking user input number.

x = int(input("enter x:")) # here we have taken user input and converted it into an integer.
count = 0
while x > 0: # used a loop which gives condition that x should be greater than 0.
    x = x//10 # here we are dividing the number by 10 and updating the value of x in each itration.
    count = count +1 
print(count) # here we are printing the count of digits in the number which we have taken as input from the user.

# so this is a simple python program to count the number of digits in a given number by taking user input.

    
