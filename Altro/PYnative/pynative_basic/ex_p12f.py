'''
Exercise 12: Calculate income tax
Calculate income tax for the given income by adhering to the rules below
Taxable Income	Rate (in %)
First $10,000	0
Next $10,000	10
The remaining	20
'''

income:float = float(input("\nIncome: "))

def tax_pay(income):                  #esempio   15200     54200

    tax_0:float = income - 10000                 #5200     44200
    tax_10:float = tax_0 - 10000                 #-4800    34200
    
    if tax_0 > 0:
        if tax_10 > 0:
            tax = 10000 * 0.1 + tax_10 * 0.2
        else:
            tax = tax_0 * 0.1
    else:
        tax = 0
    
    return tax

print(f"\nFor income {income} you must pay {tax_pay(income)}$ tax\n")
