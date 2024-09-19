numero1 = int(input("Ingrese el primer numero:"))
numero2 = int(input("Ingrese el segundo numero:"))

for i in range(numero1, numero2+1):
    if i % 2 ==0:
        continue
    else:
        print(i)