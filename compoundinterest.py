principal = int(input("Enter principal amount: "))
rate= float(input("Enter rate of interest in decimals: "))
years = int(input("for how many years to calculate interest: "))


def compound_interest(principal, rate, years):
    if years == 0:
        return principal
    else:
        principal += principal*rate
        return compound_interest(principal, rate, years-1)
        
print(compound_interest(principal, rate, years))