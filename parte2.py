# 1. imports
# 2. constantes (A, B)
# 3. funciones base (simular_muestra, frecuencia_intervalo)
# 4. funciones de experimento
# 5. funciones de ejecución (prints)

import numpy as np

A = 2 / 7
B = 6 / 7

# Simula n_muestras de X usando n_monedas, devuelve un array con los valores de X
def simular_muestra(n_monedas=10, n_muestras=1000, seed=None): 
    rng = np.random.default_rng(seed)
    monedas = rng.integers(0, 2, size=(n_muestras, n_monedas))
    potencias = 2.0 ** np.arange(1, n_monedas + 1)
    return np.sum(monedas / potencias, axis=1)


def frecuencia_intervalo(muestras, a=A, b=B): # Calcula la frecuencia de muestras que caen en el intervalo [a, b]
    return np.mean((muestras >= a) & (muestras <= b))


def experimento(n_monedas=10, n_muestras=1000): # Ejecuta un experimento completo: simula las muestras y calcula la frecuencia en el intervalo
    muestras = simular_muestra(n_monedas, n_muestras)
    return frecuencia_intervalo(muestras)


def experimento_con_monedas(): # Analiza cómo cambia la frecuencia al variar la cantidad de monedas
    monedas_lista = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    n_muestras = 100000
    valor_teorico = 4 / 7

    print("\n" + "=" * 60)
    print("Efecto de la cantidad de monedas")
    print("=" * 60)

    for m in monedas_lista:
        freq = experimento(m, n_muestras)
        print(f"Monedas: {m:>3} | Frecuencia: {freq:.6f} | Error: {abs(freq - valor_teorico):.2e}")


def ejecutar_experimentos(): # Ejecuta experimentos para distintos tamaños de muestra y compara con el valor teórico
    tamaños = [10**3, 10**4, 10**5, 10**6]
    valor_teorico = 4 / 7

    print("=" * 60)
    print("Parte 2 - Aproximación Monte Carlo")
    print("=" * 60)
    print(f"Valor teórico: {valor_teorico:.6f}\n")

    for n in tamaños:
        freq = experimento(10, n)
        print(f"Muestras: {n:>7} | Frecuencia: {freq:.6f} | Error: {abs(freq - valor_teorico):.2e}")