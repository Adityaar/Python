import turtle

def tree(branchLen,t):
    """ Recursive method to draw a tree. """
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)

def main():

    """ Main method that creates the turtle object from turtle package.
        Make sure to install tkinter via pip.
    """
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75, t)
    myWin.exitonclick()

main()
