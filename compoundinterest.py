principal = int(input("Enter principal amount: "))
rate= float(input("Enter rate of interest in decimals: "))
years = int(input("for how many years to calculate interest: "))

def compound_interest(principal, rate, years): 
    return principal*(1 + rate)**years 

def compound_interest_recursive(principal, rate, years):
    if years == 0:
        return principal
    else: 
        CI = compound_interest(principal, rate, years) - principal
        return CI
print(compound_interest_recursive(principal, rate, years))