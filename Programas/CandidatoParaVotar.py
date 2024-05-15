print("Buen dia\n Elija un Candidato indicando la letra por cada partido por favor")
print("A) Candidato 'A' por el partido rojo")
print("B) Candidato 'B' por el partido verde")
print("C) Candidato 'C' por el partido azul")
Candidato = str(input())
if Candidato.upper() == "A":
    print("Usted ha votado por el partido rojo")
elif Candidato.upper() == "B":
    print("Usted ha votado porel partido verde")
elif Candidato.upper() == "C":
    print("Usted ha votado por el partido azul")
else:
    print("Opción errónea,favor de indicar la letra correcta")
