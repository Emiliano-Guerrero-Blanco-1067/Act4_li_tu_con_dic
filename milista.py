# ejemplo de listas
misNovios = ["Agripina", "Anastacia", "Maria"]
misNumeros = [666, 77, 10]

# Mostrando mis novias
print(misNovios)

# Mostrando mis numeros
print(misNumeros)
print("---accediendo a los elementos de la lista---")
print(misNovios[-2])
if "Ana" in misNovios :
    print("si, 'Agripina' esta en la lista de mis novios ")
else:
    print("Chale no eres mi novio")    
print("Numero de novios")
Nnovios= len(misNovios)
print(f"Numero de novios= {Nnovios}")
print("ciclo en las listas")
posicion= 0

for medianaranja in misNovios:
    print(posicion," ",medianaranja)
    posicion=posicion+1
