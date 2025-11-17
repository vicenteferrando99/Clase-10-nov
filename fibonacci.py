import argparse

def fibonacci_recursivo(n: int | str)->int:
    """
    Funcion que calcula el n-esimo numero de Fibonacci de forma recursiva.

    Argumentos:
    n (int) : la posicion en la secuencia de Fibonacci.

    returns:
    int: El n-esimo numero de Fibonacci
    """
    if isinstance(n,str):
        try:
            n=int(n)
        except ValueError:
            raise ValueError("debe ser un numero")

    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

def fibonacci_con_cache(n: int | str) -> int:
    """
    Funcion que calcula el n-esimo numero de Fibonacci usando cache (iterativo).

    Argumentos:
    n (int) : la posicion en la secuencia de Fibonacci.

    returns:
    int: El n-esimo numero de Fibonacci
    """
    if isinstance(n, str):
        try:
            n = int(n)
        except ValueError:
            raise ValueError("debe ser un numero")

    if n <= 0:
        return 0
    if n == 1:
        return 1

    cache = {0: 0, 1: 1}
    for k in range(2, n + 1):
        cache[k] = cache[k - 1] + cache[k - 2]
    return cache[n]


def main():
    parser = argparse.ArgumentParser(description="Calcula el n-esimo numero de Fibonacci.")
    parser.add_argument("-n", type=int, required=True, help="La posicion en la secuencia de Fibonacci")
    parser.add_argument("--metodo", type=str, choices=["recursivo", "cache"], default="cache",
                        help="Metodo de calculo: 'recursivo' o 'cache' (por defecto)")

    args = parser.parse_args()

    if args.metodo == "recursivo":
        if args.n > 10:
            print(f"Error: El metodo recursivo no se puede usar con n > 10 (se solicito n={args.n})")
            print("El metodo recursivo es muy ineficiente para valores grandes.")
            print("Por favor usa --metodo cache o reduce el valor de n.")
            return
        resultado = fibonacci_recursivo(args.n)
        print(f"Fibonacci({args.n}) usando metodo recursivo: {resultado}")
    else:
        resultado = fibonacci_con_cache(args.n)
        print(f"Fibonacci({args.n}) usando metodo con cache: {resultado}")


if __name__ == "__main__":
    main()
