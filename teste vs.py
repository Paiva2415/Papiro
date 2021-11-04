palavra2 = " "

palavra = input ("Digita: ")

for letter in palavra.upper():
    if letter == "A":
        palavra2 = letter
        continue
    elif letter == "E":
        palavra2 = palavra2 + letter
        continue
    elif letter == "I":
        palavra2 = palavra2 + letter
        continue
    elif letter == "O":
        palavra2 = palavra2 + letter
        continue
    elif letter == "U":
        palavra2 = palavra2 + letter
        continue
    print (letter)

print (palavra2)