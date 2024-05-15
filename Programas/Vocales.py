print("Escribe una letra")
Letra = str(input())

if Letra.lower() == "a":
    print("Escribiste la vocal 'A'")
elif Letra.lower() == "e":
    print("Escribistela vocal 'E'")
elif Letra.lower() == "i":
    print("Escribiste la vocal 'I'")
elif Letra.lower() == "o":
    print("Escribiste la vocal 'O'")   
elif Letra.lower() == "u":
    print("Escribiste la vocal 'U'")
else:
    print("No es una vocal\n", Letra)