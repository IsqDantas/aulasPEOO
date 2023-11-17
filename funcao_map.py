def calcular_quadrado(a: int):
    return a ** 2


def main():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numeros_ao_quadrado = list(map(calcular_quadrado, numeros))
    print(numeros_ao_quadrado)


if __name__ == '__main__':
    main()
