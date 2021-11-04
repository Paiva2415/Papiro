#!/usr/bin/python3

beatles = []
print("Step 1:", beatles)

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("\nStep 2:", beatles)

for i in range(2):
    novo = input("Insira o nome do próximo integrante: ")
    beatles.append(novo)
print("\nStep 3:", beatles)

del beatles[3]
del beatles[3]
print("\nStep 4:", beatles)

beatles.insert(0, "Ringo Star")
print("\nStep 5:", beatles)


# testing list legth
print("The Fab", len(beatles))