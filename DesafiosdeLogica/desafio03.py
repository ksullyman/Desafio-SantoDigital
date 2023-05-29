def obter_subconjuntos(conjunto):
    n = len(conjunto)# n recebe o conjunto com len verificando o tamanho da lista
    subconjuntos = [[]]  # Inicialmente, o conjunto vazio é incluído

    for i in range(n):# i percorrerá toda a lista de n
        subconjuntos += [s + [conjunto[i]] for s in subconjuntos]

    return subconjuntos


# Exemplo de uso
conjunto = [1, 2]
resultado = obter_subconjuntos(conjunto)
print(resultado)
