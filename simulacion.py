import numpy as np
from parte1 import generar_realizacion

# Genera muchas realizaciones de X y calcula su media y varianza empírica
def calcular_empirico(n=10, num_muestras=200_000, seed=42): # Seed fijo para reproducibilidad, para mismos resultados
    rng = np.random.default_rng(seed)
    monedas = rng.integers(0, 2, size=(num_muestras, n)) # Genera una matriz de 0s y 1s, cada fila es una realización de n monedas
    potencias = 2.0 ** np.arange(1, n + 1)
    muestras = np.sum(monedas / potencias, axis=1) # Calcula el valor de X para cada realización (suma ponderada de las monedas)
    return muestras, muestras.mean(), muestras.var()

def verificar_cantidad_valores(n=10): # Devuelve la cantidad teórica de valores posibles
    return 2 ** n