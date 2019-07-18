def pig_latin(mystring):
    if mystring[0].lower() in "aeiou":
        return mystring + 'ay'
    return mystring[1:]+mystring[0]+'ay'
