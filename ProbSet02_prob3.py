balance = 320000
annualInterestRate = 0.2 

mir = annualInterestRate/12 

#mPay=10
#nBal=balance


epsilon = 0.01
numGuesses = 0

low = balance/12
high = (balance * ( 1+ mir )**12)/12.0
mPay = (high + low)/2.0
nBal = balance


while abs(nBal) > epsilon:
    nBal = balance
    for month in range (12):
        nBal = (nBal - mPay) * (1 + mir)
    if nBal <= 0:
        high = mPay
    else:    
        low = mPay
    mPay = (low + high)/2.0

print ("Lowest payment: " + str(round(mPay,2)))