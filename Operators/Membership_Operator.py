# 6. MEMBERSHIP OPERATORS => USED TO CHECK WHETHER A VALUE EXISTS IN A SEQUENCE.
# EX: in, not in

my_list = [10, 20, 30, 40]

print("The output of 20 in list : ", 20 in my_list)
print("The output of 50 in list : ", 50 in my_list)
print("The output of 50 not in list : ", 50 not in my_list)

my_list = [1, 2, 3, 4, 5]
value = int(input("Enter value to check: "))

print("Value in list :", value in my_list)
print("Value not in list :", value not in my_list)