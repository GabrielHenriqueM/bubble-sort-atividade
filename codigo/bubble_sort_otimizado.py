def bubble_sort_otimizado(lista):
    comparacoes = 0
    n = len(lista)
    for i in range(n):
        trocou = False
        for j in range(0, n - i - 1):
            comparacoes += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
        if not trocou:
            break
    return lista, comparacoes

if __name__ == "__main__":
    vetor = [64, 34, 25, 12, 22, 11, 90]
    print("\nBUBBLE SORT OTIMIZADO")
    print("Antes da ordenação:", vetor)
    ordenado, comparacoes = bubble_sort_otimizado(vetor.copy())
    print("Depois da ordenação:", ordenado)
    print(f"Total de comparações: {comparacoes}\n")
