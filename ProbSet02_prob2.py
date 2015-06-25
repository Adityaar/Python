balance = 320000
annualInterestRate = 0.2 
#monthlyPaymentRate = 0.04 

mir = annualInterestRate/12 
unpaid_bal = 0

mPay=10
nBal=balance

def mp(min_pay,bal):
    for month in range (12): 
        unpaid_bal = bal - min_pay
        bal = unpaid_bal + ( mir * unpaid_bal )
    return bal

while nBal > 0:
    nBal = mp(mPay,balance)
    if nBal > 0:
        mPay += 10 

print ("Lowest payment: " + str(mPay))