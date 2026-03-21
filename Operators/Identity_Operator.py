# 7. IDENTITY OPERATORS => USED TO COMPARE MEMORY LOCATION OF TWO OBJECTS.
# EX: is, is not

x = [1, 2, 3]
y = [1, 2, 3]
z = x

print("The output of x is y : ", x is y)
print("The output of x is z : ", x is z)
print("The output of x is not y : ", x is not y)

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

print("a is b :", a is b)
print("a is not b :", a is not b)