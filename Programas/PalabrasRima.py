print("Ingresa dos palabras:")
Pal1 = str(input())
Pal2 = str(input())

if len(Pal1) < 3 or len(Pal2) < 3:
    print("Debe ingresar una palabra mas larga")
elif Pal1[-3] == Pal2[-3]:
    print("Las palabras riman")
elif Pal1[-2] == Pal2[-2]:
    print("Las palabras riman un poco")
else:
    print("Las palabras no riman")
    