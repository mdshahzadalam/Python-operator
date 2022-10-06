#5. Write a python script which takes a three digit number from the user and displays
#   only its first digit.

x=int(input("enter a number:-"))
while x>=10:
    x=x//10
print(x)