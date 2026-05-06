import numpy as np

def generar_realizacion(n=10, rng=None): # Genera UN valor de X, construye un numero binario con n monedas
    if rng is None:
        rng = np.random.default_rng()
    monedas = rng.integers(0, 2, size=n) # Suelta algo como: [1, 0, 1, 1, 0, ...]
    potencias = 2.0 ** np.arange(1, n + 1)
    return np.sum(monedas / potencias)


def valores_posibles(n=10): # devuelve todos los valores posibles de X
    denominador = 2 ** n
    return np.array([k / denominador for k in range(denominador)])


def funcion_masa_probabilidad(n=10): # devuelve los valores posibles y sus probabilidades (todas iguales)
    vals = valores_posibles(n)
    prob = 1.0 / (2 ** n)
    probs = np.full(len(vals), prob)
    return vals, probs


def esperanza_teorica(n=10): # Calcula E[X]
    return sum(0.5 / (2 ** i) for i in range(1, n + 1))


def varianza_teorica(n=10): # Calcula Var(X) = E[X^2] - (E[X])^2
    return sum(0.25 / (4 ** i) for i in range(1, n + 1))