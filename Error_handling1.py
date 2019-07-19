try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print "Can't power a string! "
while True:
    try:
        inp = int(input())
    except:
        print 'Bad input!'
    else:
        break
