import math
import random

def pedir_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            print("  El valor debe ser mayor que 0.")
        except ValueError:
            print("  Entrada inválida, escribe un número.")


def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print("  El valor debe ser mayor que 0.")
        except ValueError:
            print("  Entrada inválida, escribe un número entero.")


def en_elipse(x, y, a, b):
    return (x ** 2) / (a ** 2) + (y ** 2) / (b ** 2) <= 1


def en_hiperbola(x, y, c, d):
    return (x ** 2) / (c ** 2) - (y ** 2) / (d ** 2) >= 1


def main():
    print("****Calculemos el área de la intersección elipse mediante Monte Carlo.*****")
    print("\nIngresa los valores de las constantes para la elipse y la hipérbola:")
    a = pedir_float("Constante elipse a: ")
    b = pedir_float("Constante elipse b: ")
    c = pedir_float("Constante hipérbola c: ")
    d = pedir_float("Constante hipérbola d: ")
    cantidad = pedir_entero("Cantidad de puntos aleatorios: ")

    dentro_elipse = 0
    dentro_interseccion = 0

    for _ in range(cantidad):
        x = random.uniform(-a, a)   # x entre -a y a
        y = random.uniform(-b, b)   # y entre -b y b
        if en_elipse(x, y, a, b):
            dentro_elipse += 1
            if en_hiperbola(x, y, c, d):
                dentro_interseccion += 1

    area_elipse = math.pi * a * b
    if dentro_elipse > 0:
        area_interseccion = area_elipse * dentro_interseccion / dentro_elipse
    else:
        area_interseccion = 0.0

    print("\n******Respuestas******")
    print(f"Puntos generados:                      {cantidad}")
    print(f"Puntos dentro de la elipse:            {dentro_elipse}")
    print(f"Puntos en la intersección:             {dentro_interseccion}")
    print(f"Área de la elipse (pi*a*b):            {area_elipse:.4f}")
    print(f"Área aproximada de la intersección:    {area_interseccion:.4f}")


if __name__ == "__main__":
    main()