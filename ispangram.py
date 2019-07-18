import string
def ispangram(str):
    alphabet = string.ascii_lowercase
    for letter in str:
        if letter in alphabet:
             alphabet=alphabet.replace(letter,'')
    return alphabet == ""
print(ispangram("The quick brown fox jumps over the lazy dog"))
