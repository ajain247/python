def compound_interest(p,r,t):
    return ((p*(1+(r/100))**t)-p)

prinipal=float(input("Please insert the Principal amount: "))
roi=float(input("\nPlease insert the rate of interest: "))
time=int(input("\nPlease insert the time in months: "))

print("\n\nThe Compound Interest for Principal amount {0}, Rate of Interest {1}% and {2} months will be: {3}" .format(prinipal,roi,time,compound_interest(prinipal,roi,time)))