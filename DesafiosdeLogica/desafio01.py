def criar_lista_asteriscos(n):
    lista = []
    for i in range(1, n + 1):
        lista.append('*' * i)
    return lista


n = 5
lista_asteriscos = criar_lista_asteriscos(n)
print(lista_asteriscos)
