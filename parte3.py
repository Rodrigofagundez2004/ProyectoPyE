import numpy as np
import time
from modelo import generar_realizacion

def simular_par_monedas(n=10, rng=None):
    if rng is None:
        rng = np.random.default_rng()
    X = generar_realizacion(n, rng)
    Y = generar_realizacion(n, rng)
    return X, Y

def simular_muestra_pares(n_monedas, tamano_muestra, seed=42):
    rng = np.random.default_rng(seed)
    Xs = np.zeros(tamano_muestra)
    Ys = np.zeros(tamano_muestra)
    for i in range(tamano_muestra):
        Xs[i], Ys[i] = simular_par_monedas(n_monedas, rng)
    return Xs, Ys

def aproximar_pi(n_monedas, tamano_muestra):
    Xs, Ys = simular_muestra_pares(n_monedas, tamano_muestra)
    dentro = np.mean((Xs**2 + Ys**2) <= 1)
    return 4 * dentro

def contar_digitos_correctos(aprox_pi):
    pi_str = f"{np.pi:.15f}"
    aprox_str = f"{aprox_pi:.15f}"
    digitos = 0
    for i in range(len(pi_str)):
        if i < len(aprox_str) and pi_str[i] == aprox_str[i]:
            digitos += 1
        else:
            break
    return max(0, digitos - 2)

def ejecutar_parte3():
    print("=" * 70)
    print("PARTE 3 - APROXIMACIÓN DE π USANDO MONEDAS")
    print("=" * 70)
    
    print("\n[Pregunta 3] Simulación con 10 monedas:")
    print(f"{'n (tamaño muestra)':<20} {'4 * frecuencia':<15} {'Error absoluto':<15} {'Tiempo (s)':<10}")
    print("-" * 65)
    
    for n in [1000, 10000, 100000, 1000000]:
        inicio = time.time()
        pi_aprox = aproximar_pi(10, n)
        tiempo = time.time() - inicio
        error = abs(pi_aprox - np.pi)
        print(f"{n:<20,} {pi_aprox:<15.8f} {error:<15.2e} {tiempo:<10.4f}")
    
    print("\n[Pregunta 4] Dígitos correctos:")
    for n in [1000, 10000, 100000, 1000000]:
        pi_aprox = aproximar_pi(10, n)
        digitos = contar_digitos_correctos(pi_aprox)
        print(f"n = {n:7,} → π ≈ {pi_aprox:.10f} → {digitos} dígito(s) correcto(s)")
    
    print("\n[Pregunta 5] Variando número de monedas (n_muestra = 100,000 fijo):")
    print(f"{'Monedas':<10} {'Aprox π':<15} {'Error':<15} {'Dígitos':<10} {'Tiempo (s)':<10}")
    print("-" * 65)
    
    for k in [10, 12, 14, 16, 18, 20]:
        inicio = time.time()
        pi_aprox = aproximar_pi(k, 100000)
        tiempo = time.time() - inicio
        error = abs(pi_aprox - np.pi)
        digitos = contar_digitos_correctos(pi_aprox)
        print(f"{k:<10} {pi_aprox:<15.8f} {error:<15.2e} {digitos:<10} {tiempo:<10.4f}")
    
    print("\n[Pregunta 6] Análisis de eficiencia:")
    print("\nCaso 1: Aumentar tamaño de muestra (10 monedas fijo)")
    print(f"{'n_muestra':<15} {'Aprox π':<12} {'Error':<12} {'Tiempo (s)':<10}")
    print("-" * 55)
    
    for n in [1000, 10000, 100000, 1000000]:
        inicio = time.time()
        pi_aprox = aproximar_pi(10, n)
        tiempo = time.time() - inicio
        error = abs(pi_aprox - np.pi)
        print(f"{n:<15,} {pi_aprox:<12.8f} {error:<12.2e} {tiempo:<10.4f}")
    
    print("\nCaso 2: Aumentar monedas (n_muestra = 100,000 fijo)")
    print(f"{'monedas':<10} {'Aprox π':<12} {'Error':<12} {'Tiempo (s)':<10}")
    print("-" * 55)
    
    for k in [10, 12, 14, 16, 18, 20]:
        inicio = time.time()
        pi_aprox = aproximar_pi(k, 100000)
        tiempo = time.time() - inicio
        error = abs(pi_aprox - np.pi)
        print(f"{k:<10} {pi_aprox:<12.8f} {error:<12.2e} {tiempo:<10.4f}")
    
    print("\n" + "=" * 70)
    print("CONCLUSIÓN: Aumentar el número de monedas es más eficiente")
    print("que aumentar el tamaño de muestra, porque el error de")
    print("discretización se reduce rápidamente con poco costo adicional.")
    print("=" * 70)

if __name__ == "__main__":
    ejecutar_parte3()