def validar_numero():
    """
    Función que solicita al usuario ingresar un número entero positivo.
    """
    try:
        numero_entero = int(input("Ingrese un número positivo: "))
        if numero_entero > 0:
            return numero_entero
        else:
            print("El número es inválido. Debe ser un entero positivo.")
            return validar_numero()
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")
        return validar_numero()


def reduce_soloundigito(num):
    """
    Función que reduce un número a un solo dígito sumando sus cifras de manera recursiva.
    """
    if num < 10:
        return num
    else:
        num = sum(int(digit) for digit in str(num))
        return reduce_soloundigito(num)


def proceso_carrera(numero):
    """
    Función que simula una carrera entre números, determinando el ganador
    por pares de dígitos hasta que queda un único valor.
    """
    resultados = []
    digitos = [int(d) for d in str(numero)]

    while len(digitos) > 1:
        round_resultados = []
        siguiente_digito = []

        for i in range(0, len(digitos) - 1, 2):
            car_x = reduce_soloundigito(digitos[i] + digitos[i + 1])
            if i + 2 < len(digitos):
                car_y = reduce_soloundigito(
                    digitos[i + 2] + digitos[i + 3]
                ) if i + 3 < len(digitos) else digitos[i + 2]
            else:
                car_y = digitos[i + 1]

            
            if car_x > car_y:
                winner = "Carro_X"
                siguiente_digito.append(car_x)
            elif car_y > car_x:
                winner = "Carro_Y"
                siguiente_digito.append(car_y)
            else:
                winner = "Empate"
                siguiente_digito.extend([car_x, car_y])

            # Almacenar resultados
            round_resultados.append((digitos[i], digitos[i + 1], winner))

        # Actualizar la lista de dígitos
        digitos = siguiente_digito
        resultados.append(round_resultados)

    # Mostrar los resultados
    print("Resultados de la carrera:")
    for round, resultados_round in enumerate(resultados, start=1):
        print(f"Ronda {round_resultados}:")
        for resultado in resultados_round:
            print(f"  {resultado[0]} + {resultado[1]} -> {resultado[2]}")

    print(f"Ganador final: {digitos[0]}")


if __name__ == "__main__":
    numero = validar_numero()
    proceso_carrera(numero)
