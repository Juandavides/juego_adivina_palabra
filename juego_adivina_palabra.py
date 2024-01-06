import random

def obtener_palabras_aleatoria():
    palabras = ["python", "programacion", "juegos", "computadora","diversion"]
    return random.choice(palabras)

def mostrar_tablero(palabra_oculta, intentos):
    print("palabras:", "".join(palabra_oculta))
    print("intentos restantes:", intentos, " ","x"*intentos)
    print("=====================================")

def adivinar_letra(palabra, palabra_oculta, letra):
    aciertos = 0
    for i in range(len(palabra)):
        if palabra[i]  ==  letra:
            palabra_oculta[i]= letra
            aciertos += 1
    return aciertos

def juego_adina_palabra():
    palabra = obtener_palabras_aleatoria()
    palabra_oculta = ["_" for _ in palabra];
    intentos = 6
    letras_usadas= []

    while True:
        mostrar_tablero(palabra_oculta, intentos)

        if "_" not in palabra_oculta:
            print("Has ganado, la palabra era:", " ".join(palabra))
            break
        if intentos == 0:
            print("has perdido, la palabra era:", " ".join(palabra))
            break

        letra = input("ingresa una letra"). lower()

        if letra in letras_usadas:
            print("ya has adivinado esta letra, intenta con otra")
            continue
        letras_usadas.append(letra)

        aciertos = adivinar_letra(palabra, palabra_oculta, letra)

        if aciertos > 0:
            print("Adivinaste", aciertos, "letras")
        else:
            print("la letra no esta en la palabra")
            intentos -= 1
        print("======================================")

juego_adina_palabra()


