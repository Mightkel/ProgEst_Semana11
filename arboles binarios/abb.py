#Paso A

def crear_nodo(valor):
    return {"valor": valor, "izq": None, "der": None}

def insertar(raiz, valor):
    if raiz is None:
        return crear_nodo(valor)
    if valor < raiz["valor"]:
        raiz["izq"] = insertar(raiz["izq"], valor)
    elif valor > raiz["valor"]:
        raiz["der"] = insertar(raiz["der"], valor)
    return raiz

raiz = None
for numero in [50, 30, 70, 20, 40, 60, 80]:
    raiz = insertar(raiz, numero)
    
#Paso B
    
def buscar(raiz, valor):
    if raiz is None:
        return False
    if raiz["valor"] == valor:
        return True
    if valor < raiz["valor"]:
        return buscar(raiz["izq"], valor)
    return buscar(raiz["der"], valor)

def inorden(raiz):
    if raiz is not None:
        inorden(raiz["izq"])
        print(raiz["valor"], end=" ")
        inorden(raiz["der"])

print(buscar(raiz, 60))
inorden(raiz)

#Paso C

def preorden(raiz):
    if raiz is not None:
        print(raiz["valor"], end=" ")
        preorden(raiz["izq"])
        preorden(raiz["der"])

def postorden(raiz):
    if raiz is not None:
        postorden(raiz["izq"])
        postorden(raiz["der"])
        print(raiz["valor"], end=" ")

def contar_nodos(raiz):
    if raiz is None:
        return 0
    return 1 + contar_nodos(raiz["izq"]) + contar_nodos(raiz["der"])

def altura(raiz):
    if raiz is None:
        return 0
    return 1 + max(altura(raiz["izq"]), altura(raiz["der"]))

# Reto: eliminación

def minimo(raiz):
    while raiz["izq"] is not None:
        raiz = raiz["izq"]
    return raiz

def eliminar(raiz, valor):
    if raiz is None:
        return None
    if valor < raiz["valor"]:
        raiz["izq"] = eliminar(raiz["izq"], valor)
    elif valor > raiz["valor"]:
        raiz["der"] = eliminar(raiz["der"], valor)
    else:
        if raiz["izq"] is None:
            return raiz["der"]
        if raiz["der"] is None:
            return raiz["izq"]
        sucesor = minimo(raiz["der"])
        raiz["valor"] = sucesor["valor"]
        raiz["der"] = eliminar(raiz["der"], sucesor["valor"])
    return raiz

print()
preorden(raiz); print()
postorden(raiz); print()
print(contar_nodos(raiz))
print(altura(raiz))

raiz = eliminar(raiz, 20)
raiz = eliminar(raiz, 30)
raiz = eliminar(raiz, 50)
inorden(raiz)