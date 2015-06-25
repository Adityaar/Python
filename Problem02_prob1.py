balance = 4213 
annualInterestRate = 0.2 
monthlyPaymentRate = 0.04 

mir = annualInterestRate/12 
totPaid = 0 
unpaid_bal = 0
for month in range (12): 
    minMonthlyPayment = monthlyPaymentRate * balance
    unpaid_bal = balance - minMonthlyPayment
    balance = unpaid_bal + ( mir * unpaid_bal )

    totPaid = totPaid + minMonthlyPayment
    print ("Month: " + str(month+1))
    print ("Minimum monthly payment: " + str(round(minMonthlyPayment,2)))
    print ("Remaining balance: " + str(round(balance,2)))

print ("Total paid: " + str(round(totPaid,2)))
print ("Remaining balance: " + str(round(balance,2)))
