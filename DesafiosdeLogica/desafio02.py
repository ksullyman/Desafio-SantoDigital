def menor_diferenca(array):
    array.sort()  # Classifica o array em ordem crescente
    menor_dif = float('inf')  # Inicializa a menor diferença como infinito
    pares = []  # Lista para armazenar os pares com a menor diferença

    for i in range(0, len(array) - 1):
        diferenca = abs(array[i+1] - array[i])

        if diferenca < menor_dif:
            menor_dif = diferenca
            pares = [(array[i], array[i+1])]
        elif diferenca == menor_dif:
            pares.append((array[i], array[i+1]))

    return pares

# Exemplo de uso
numeros = [3, 8, 50, 5, 1, 18, 12]
resultado = menor_diferenca(numeros)
print(resultado)
