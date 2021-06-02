def max_num(a,b):
    if a>b:
        return a
    else:
        return b

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("The maximum of {0} and {1} is : {2}" .format(a,b,max_num(a,b)))