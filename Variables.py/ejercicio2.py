practica1 = float(input("Ingrese el valor de la practica1"))
practica2 = float(input("Ingrese el valor de la practica2"))
practica3 = float(input("Ingrese el valor de la practica3"))

ExamenParcial = float(input("Ingrese el valor del Examen Parcial"))
ExamenFinal = float(input("Ingrese el valor del Examen Final"))

promedioDePractica = (practica1+practica2+practica3)/3
Promedio = (promedioDePractica+2*ExamenParcial+3*ExamenFinal)/6

print("El promedio de Practica del estudiante es de\n: ",promedioDePractica,
"\n y el promedio Final es de\n: ",Promedio  )
