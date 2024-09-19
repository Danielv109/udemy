diccionario = {"Nombre" : "Daniel", "Apellido" : "Villarreal", "Estatura" : 1.73}

print(diccionario)
#para mandar a llamarsolamente o las claves o los valores de dicho diccionario
print(diccionario.keys())
print(diccionario.values())

#para mandar a llamar una clave en especifico y que sólo regrese el valor de dicha clave
print(diccionario["Apellido"])

#para agregar un nuevo valor en eldiccionario
diccionario["peso"] = 60

#para modificar un dato deldiccionario
diccionario["Apellido"] = "Soto"
