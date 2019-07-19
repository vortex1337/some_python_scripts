def square():
    n = int(input('Enter an integer: '))
    print n**2
def ask():
    while True:
        try:
            square()
        except:
            print 'Bad input! Try again: '
        else:
            break
ask()
