def myfunc(mystring):
    result = ''
    for i in range(len(mystring)):
        if i % 2 == 0:
            result+=mystring[i].lower()
        else:
            result+=mystring[i].upper()
    return result
print(myfunc("Anthropomorphism"))
