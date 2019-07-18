def animal_crackers(text):
    return text.split()[0][0] == text.split()[1][0]
print(animal_crackers('Levelheaded Llama'))
