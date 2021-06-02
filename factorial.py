def factorial(x):
    return 1 if (x==1 or x==0) else x*factorial(x-1)

x=int(input("Please enter the number "))
print("\nResult of the factorial of {0} is {1} : " .format(x,factorial(x)))