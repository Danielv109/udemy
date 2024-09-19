diccionario1 = {"Guatemala" : "Ciudad de Guatemala", "El salvador" : "San Salvador", "Honduras" : "Honduras", "Nicaragua" : "Managua", "Costa Rica" : "San Jose", "Mexico" : "Ciudad de Mexico", "Colombia" : "Bogota", "Venezuela" : "Caracas", "España" : "Madrid"} 

Respuesta = str(input("Ingrese un pais: "))
for i in diccionario1:
    if Respuesta.capitalize() in diccionario1:
        print(diccionario1.index(1))
    else:
        print("Ese pais no se encuentra")