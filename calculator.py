def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: división por cero"
    return a / b

def main():
    print("Calculadora en Python")
    print("Operaciones disponibles: sumar, restar, multiplicar, dividir")
    operacion = input("Ingresa la operación: ")
    x = float(input("Primer número: "))
    y = float(input("Segundo número: "))

    if operacion == "sumar":
        resultado = sumar(x, y)
    elif operacion == "restar":
        resultado = restar(x, y)
    elif operacion == "multiplicar":
        resultado = multiplicar(x, y)
    elif operacion == "dividir":
        resultado = dividir(x, y)
    else:
        resultado = "Operación no válida"
    print("Resultado:", resultado)

if __name__ == "__main__":
    main()