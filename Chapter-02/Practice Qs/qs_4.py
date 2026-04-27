# WAP to find the greatest of 3 numbers entered by the user.
a = int(input("enter first number : "))
b = int(input("enter second number : "))
c = int(input("enter third number : "))

if(a >= b and b >= c):
    print("first number is largest",a)
elif(b >= c):
    print("second number is largest",b)
else:
    print("third number is largest",c)


# ---------------------------------------------------------------------------------------------------


a = 10
b = 19
c = 15

if(a >= b and b >= c):
    print("This is largest no.",a)
elif(b >= c):
    print("This is largest no.",b)
else:
    print("This is largest no.",c)