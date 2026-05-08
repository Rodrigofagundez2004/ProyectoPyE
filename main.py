from parte1 import (
    valores_posibles,
    esperanza_teorica,
    varianza_teorica
)
from parte2 import ejecutar_experimentos, experimento_con_monedas
from simulacion import calcular_empirico

def reporte_verificacion(n=10): # Verifica que la cantidad de valores posibles es 2^n y compara E[X] y Var(X) empírica con teórica
    print("=" * 50)
    print(f"Verificación para n = {n}")
    print("=" * 50)

    cantidad = len(valores_posibles(n))
    print(f"Valores posibles: {cantidad} (esperado: {2**n})")

    e_teo = esperanza_teorica(n)
    v_teo = varianza_teorica(n)

    _, e_emp, v_emp = calcular_empirico(n) # Genera muchas muestras y calcula media y varianza empírica

    print(f"\nE[X] teórico   : {e_teo:.8f}")
    print(f"E[X] empírico  : {e_emp:.8f}")

    print(f"\nVar(X) teórico : {v_teo:.8f}")
    print(f"Var(X) empírico: {v_emp:.8f}")

    print(f"\nError E[X]: {abs(e_teo - e_emp):.2e}")
    print(f"Error Var(X): {abs(v_teo - v_emp):.2e}")


if __name__ == "__main__":
    reporte_verificacion(10)

    print("\nComparación para distintos n\n")
    print(f"{'n':>4} │ {'E[X]':>10} │ {'Var(X)':>10}")
    print("-" * 32)

    for n in [5, 10, 15, 20, 25, 30, 35, 40]:
        e = esperanza_teorica(n)
        v = varianza_teorica(n)
        print(f"{n:>4} │ {e:>10.6f} │ {v:>10.6f}")

    print("\nReferencia: Uniforme[0,1] → E=0.5, Var≈0.08333\n")
    
    ejecutar_experimentos()

    experimento_con_monedas()