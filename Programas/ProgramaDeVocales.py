# escribir un programa que solicite al usuario una vocal en minuscula 
# y luego una letra en mayuscula el programa debe convertir la letra 
#en minuscula y la vocal
# en mayuscula y al final deben de ser concatenadas ambas.

Vocal = input("Ingresar una Vocal en minúscula: ")
Letra = input("Ingresa una Letra en Mayúscula: ")
Vocal = Vocal.upper()
Letra = Letra.lower()

print("La Vocal fue: {} \nLa Letra fue: {} \n".format (Vocal , Letra))

print("¿Cuántos años tiene?")
Años = int(input())
print("Usted tiene", Años , "años")


