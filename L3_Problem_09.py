l_end = 0
h_end = 100
guess = 50

print "Please think of a number between 0 and 100!"
print "Is your secret number "+str(guess)+"?"

#print "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."

x = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

while x != 'c':
    if x == 'h':
        h_end = guess
        guess = (l_end + h_end)/2
    elif x == 'l':
        l_end = guess
        guess = (l_end + h_end)/2
    else:
        print "Sorry, I did not understand your input."        
        
    print "Is your secret number "+str(guess)+"?"
    x = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")            
 
if x=='c':
    print "Game over. Your secret number was: "+str(guess)