import time
import random
from bubble_sort_simples import bubble_sort
from bubble_sort_otimizado import bubble_sort_otimizado

def gerar_lista(tamanho):
    return [random.randint(0, 1000) for _ in range(tamanho)]

def testar_algoritmo(nome, func, lista):
    inicio = time.time()
    resultado, comparacoes = func(lista.copy()) 
    fim = time.time()
    tempo = fim - inicio
    print(f"{nome}: {tempo:.6f} segundos | Comparações: {comparacoes}")
    return resultado, tempo, comparacoes

if __name__ == "__main__":
    tamanhos = [10, 100, 1000]
    print("\nCOMPARAÇÃO ENTRE BUBBLE SORT SIMPLES E OTIMIZADO\n")

    for tamanho in tamanhos:
        print(f"Teste com {tamanho} elementos:")
        lista_teste = gerar_lista(tamanho)

        testar_algoritmo("Simples   ", bubble_sort, lista_teste)
        testar_algoritmo("Otimizado ", bubble_sort_otimizado, lista_teste)
        print()
