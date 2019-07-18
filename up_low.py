def up_low(s):
    num_of_uppercase = 0
    num_of_lowercase = 0
    for letter in s:
        if letter.isupper():
            num_of_uppercase += 1
        elif letter.islower():
            num_of_lowercase += 1
    return "No. of Upper case characters : {}\nNo. of Lower case characters : {}".format(num_of_uppercase,num_of_lowercase)
print(up_low('Hello Mr. Rogers, how are you this fine Tuesday?'))
