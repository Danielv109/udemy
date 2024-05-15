print("Ingresa un numero entero")
Num1 = int(input())

if Num1 > 0:
    print("El Valor Absoluto de" ,Num1, "es:\n",Num1)
else:
    print("El valor absoluto de", Num1, "es:\n",Num1*-1)

#Este formato de abs es para sacar el valor absoulto en python y lo saca 
#aunque sea negativo
print(abs(Num1))