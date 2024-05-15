print("¿Cuál es tu nombre?")
Nombre = str(input())
print("¿Cuántos años tienes?")
Edad = int(input())
if Nombre== "Daniel":
    if Edad >= 18:
        print("Tú eres Daniel y tienes mayoría de edad")
    else:
        print("Tú eres Daniel pero no tienes mayoría de edad")
else: 
    print("Tú no eres Daniel")
