def check_if_prime(x):
    if x>1:
        for i in range(2,x):
            if (x%i==0):
                print("Not Prime")
                break
        else:
            print("Prime")
x = int(input("Please enter a prime number to check if it is a prime number or not: " ))
check_if_prime(x)