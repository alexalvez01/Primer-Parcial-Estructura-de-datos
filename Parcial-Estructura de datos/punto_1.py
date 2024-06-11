lista=["Alejandro", "Carlos", "Daniel", "Eduardo", "Francisco",
    "Gabriel", "Hugo", "Ignacio", "Javier", "Luis"]


def invertir_lista(lista):
    if (len(lista)<=1):
        return lista
    else:
        return invertir_lista(lista[1:]) + [lista[0]]
    

lista_invertida=invertir_lista(lista)

print(f"La lista ingresada invertida es: {lista_invertida}")