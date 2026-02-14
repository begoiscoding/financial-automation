"""
DEBT OPTIMIZATION TOOL
----------------------
Author: Bego - Financial Automation Developer

This script works globally. Whether it's a 25% APR in the US or a 150% rate 
in high-inflation markets, the logic remains the same: stop the bleeding 
of compound interest.

Description: Calculates the lowest $10-multiple monthly payment to ensure debt 
             a debt is cleared within 12 months.
"""

def calculate_lowest_payment(balance, annualInterestRate):
    
    # Financial parameters
    monthlyInterestRate = annualInterestRate / 12.0
    
    # Initialize guess for payment
    monthlyPayment = 10
    
    # Exhaustive search to find the minimum payment
    while True:
        tempBalance = balance
        
        # Simulate 12 months of payments
        for month in range(12):
            unpaidBalance = tempBalance - monthlyPayment
            interest = unpaidBalance * monthlyInterestRate
            tempBalance = unpaidBalance + interest
            
        # Check if debt is paid off
        if tempBalance <= 0:
            break
        else:
            monthlyPayment += 10
            
    return monthlyPayment

# Example usage for a client report:

test_balance = 7500
test_rate = 0.249 #Credit Card APR (24.9%)
print("Lowest Payment:", calculate_lowest_payment(test_balance, test_rate))
