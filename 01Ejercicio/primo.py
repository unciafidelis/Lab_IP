N = int(input("Coloca un número: "))
if N <= 1:
    print("No es primo")
i=2
while i <= N:
    if N % i == 0 and i != 2:
        print("No es primo")
        break
    elif N%i == 0 and i== N:
        print("Es primo")
        break
    elif N%i != 0 and i < N:
        print("Es primo")
        break
    i+= 1