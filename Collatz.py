n = int(input("Insira um número: "))
passos = 0

while n > 1:
    if n % 2 == 0:
        n = n / 2
        print (n)
        passos = passos + 1
    else:
        n = (3 * n + 1)
        print (n)
        passos = passos + 1

print (passos)