def simple_interest(p,r,t):
    return (p*r*t)/100

prinipal=float(input("Please insert the Principal amount: "))
roi=float(input("\nPlease insert the rate of interest: "))
time=int(input("\nPlease insert the time in months: "))

print("\n\nThe Simple Interest for Principal amount {0}, Rate of Interest {1}% and {2} months will be: {3}" .format(prinipal,roi,time,simple_interest(prinipal,roi,time)))