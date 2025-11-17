# Calculadora de Fibonacci

Este proyecto implementa dos métodos para calcular números de la secuencia de Fibonacci en Python.

## Descripción

El archivo [fibonacci.py](fibonacci.py) contiene dos implementaciones diferentes para calcular el n-ésimo número de Fibonacci:

1. **Método recursivo**: Implementación simple pero ineficiente (limitado a n ≤ 10)
2. **Método con caché**: Implementación iterativa optimizada que usa un diccionario para almacenar resultados

## Requisitos

- Python 3.10 o superior

## Uso desde línea de comandos

### Sintaxis básica

```bash
python fibonacci.py -n <número>
```

Por defecto, usa el método con caché.

### Ejemplos

```bash
# Calcular el 10º número de Fibonacci (método con caché por defecto)
python fibonacci.py -n 10

# Calcular el 5º número de Fibonacci usando método recursivo
python fibonacci.py -n 5 --metodo recursivo

# Calcular el 50º número de Fibonacci (solo con caché)
python fibonacci.py -n 50 --metodo cache
```

### Argumentos disponibles

- `-n`: **(Requerido)** La posición en la secuencia de Fibonacci que deseas calcular
- `--metodo`: **(Opcional)** Método de cálculo: `recursivo` o `cache` (por defecto: `cache`)

### Limitaciones

- El método **recursivo** está limitado a `n ≤ 10` debido a su ineficiencia
- El método con **caché** puede manejar valores mucho más grandes sin problemas de rendimiento

## Uso como módulo en Python

También puedes importar las funciones en tu propio código:

```python
from fibonacci import fibonacci_recursivo, fibonacci_con_cache

# Usando el método recursivo
resultado = fibonacci_recursivo(7)
print(resultado)  # 13

# Usando el método con caché
resultado = fibonacci_con_cache(50)
print(resultado)  # 12586269025

# Las funciones también aceptan strings
resultado = fibonacci_con_cache("10")
print(resultado)  # 55
```

### Funciones disponibles

#### `fibonacci_recursivo(n)`

Calcula el n-ésimo número de Fibonacci de forma recursiva.

**Parámetros:**
- `n` (int | str): La posición en la secuencia de Fibonacci

**Retorna:**
- `int`: El n-ésimo número de Fibonacci

**Nota:** No recomendado para `n > 10` debido a problemas de rendimiento.

#### `fibonacci_con_cache(n)`

Calcula el n-ésimo número de Fibonacci usando un enfoque iterativo con caché.

**Parámetros:**
- `n` (int | str): La posición en la secuencia de Fibonacci

**Retorna:**
- `int`: El n-ésimo número de Fibonacci

**Nota:** Método recomendado para valores grandes de n.

## Manejo de errores

Ambas funciones validan la entrada:

```python
# Si pasas un string que no es convertible a número
fibonacci_con_cache("abc")  # Lanza ValueError: "debe ser un numero"

# Para n <= 0, retorna 0
fibonacci_con_cache(0)  # 0
fibonacci_con_cache(-5)  # 0
```

## Ejemplos de salida

```bash
$ python fibonacci.py -n 10
Fibonacci(10) usando metodo con cache: 55

$ python fibonacci.py -n 5 --metodo recursivo
Fibonacci(5) usando metodo recursivo: 5

$ python fibonacci.py -n 15 --metodo recursivo
Error: El metodo recursivo no se puede usar con n > 10 (se solicito n=15)
El metodo recursivo es muy ineficiente para valores grandes.
Por favor usa --metodo cache o reduce el valor de n.
```

## La secuencia de Fibonacci

La secuencia de Fibonacci es: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...

Donde cada número es la suma de los dos anteriores:
- F(0) = 0
- F(1) = 1
- F(n) = F(n-1) + F(n-2) para n > 1