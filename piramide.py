blocks = int(input("Informe o número de blocos: "))
l = 1
a = 0

while blocks >= 0:
    blocks = blocks - l
    l = l + 1
    a = a + 1

print ("A altura da pirâmide é: ", a - 1)