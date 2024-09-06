arcoiris=("Azul", "Verde", "Rojo", "Amarillo")
print(arcoiris)
print("--longitud arcoiris--")
print(len(arcoiris))
animales=("pantera",20, "estatura", 1.7, )
print(animales) 
print("elementos de la tupla") 
print(animales[2]) 
rateros =("juan", "ana", "pedro")
y = list(rateros)
y[0]= "polainas"
x= tuple(y)
print(x)
print("Agregando elementos")
Nanimal=("boby", "chetos")
y=list(Nanimal)
print(y)

y.append("tontolin")
otratupla= tuple(y)
print(otratupla)

print("Uso de for en tuplas")
for elcolor in arcoiris:
    print(elcolor)

thisdiccionario =	{
"Nombre": "Jorge Emiliano GUerrero Blanco",
"Localizacion": "Guerrero Blanco",
"No.Control": "a.22308051281067"
}
print(thisdiccionario)

thisconjunto = {"Esteban", "Melgar", "Oropeza"}
print(thisconjunto)

