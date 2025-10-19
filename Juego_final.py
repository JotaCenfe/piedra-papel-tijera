"""
====================================
  Juego: Piedra, Papel o Tijera
  Autor: Jorge Claudio
  Versión: Final
====================================

Cómo jugar:
- Elige piedra, papel o tijera (o sus atajos: p / pa / t).
- La computadora elige al azar.
- Gana quien llegue primero a "objetivo" puntos (mejor de N).
- Puedes escribir 'salir' en cualquier momento para abandonar.
"""
# ---------------------------------------
# 0) Importaciones
# ---------------------------------------
# 'random' sirve para que la PC "piense" (elija al azar).
import random


# ---------------------------------------
# 1) Diccionarios y reglas del juego
# ---------------------------------------
# Opciones permitidas. La clave es lo que escribe el usuario y
# el valor es la jugada "normalizada" (piedra/papel/tijera).
# Así aceptamos atajos cómodos (p, pa, t) además de la palabra completa.
OPCIONES = {
    "piedra": "piedra",
    "papel":  "papel",
    "tijera": "tijera",
    "p":      "piedra",
    "pa":     "papel",
    "t":      "tijera",
}

# Reglas: quién le gana a quién (con una frase para explicarlo).
# Ejemplo: ("piedra", "tijera") significa: piedra le gana a tijera
REGLAS = {
    ("piedra", "tijera"): "piedra aplasta tijera",
    ("tijera", "papel"):  "tijera corta papel",
    ("papel",  "piedra"): "papel envuelve piedra",
}

# Lista de jugadas válidas (la usamos para que la PC elija al azar).
JUGADAS_VALIDAS = ("piedra", "papel", "tijera")


# ---------------------------------------
# 2) Funciones de utilidad
# ---------------------------------------
def limpiar(texto: str) -> str:
    """Quita espacios al principio y final, y convierte a minúsculas."""
    return texto.strip().lower()


def normalizar_entrada(txt: str) -> str:
    """
    Convierte lo que escribe el usuario a una jugada válida:
    - 'piedra', 'papel', 'tijera'
    - o atajos: 'p', 'pa', 't'
    Si no es válido, devuelve "".
    Si el usuario escribe 'salir', devolvemos exactamente 'salir'.
    """
    txt = limpiar(txt)
    if txt == "salir":
        return "salir"
    return OPCIONES.get(txt, "")


def pedir_mejor_de() -> int:
    """
    Pide al usuario el "mejor de N".
    Debe ser un número IMPAR y mayor o igual a 1 (1, 3, 5, 7...).
    Repite la pregunta hasta que esté bien.
    """
    while True:
        dato = input("¿A cuántos puntos quieres jugar? (mejor de N, ej. 3, 5, 7). Escribe '3' si no sabes: ")
        dato = limpiar(dato)
        if not dato.isdigit():
            print("  → Debes escribir un número entero (1, 3, 5...). Intenta otra vez.\n")
            continue
        n = int(dato)
        if n < 1 or n % 2 == 0:
            print("  → Debe ser un IMPAR mayor o igual a 1 (ej. 1, 3, 5, 7...). Intenta otra vez.\n")
            continue
        return n


def pedir_jugada_usuario() -> str:
    """
    Pregunta al usuario por su jugada y la valida.
    Acepta 'piedra/papel/tijera' o atajos 'p/pa/t'.
    Permite 'salir' para abandonar la partida.
    Devuelve 'piedra' | 'papel' | 'tijera' | 'salir'.
    """
    while True:
        eleccion = input("Elige (piedra/papel/tijera) o atajos (p/pa/t). Escribe 'salir' para abandonar: ")
        jugada = normalizar_entrada(eleccion)
        if jugada == "salir":
            return "salir"
        if jugada:  # si es piedra/papel/tijera
            return jugada
        print("  → Entrada no válida. Prueba con: piedra, papel, tijera (o p, pa, t).")


def elegir_jugada_pc() -> str:
    """La PC elige al azar una jugada válida."""
    return random.choice(JUGADAS_VALIDAS)


def resultado_ronda(jugador: str, pc: str) -> int:
    """
    Determina el resultado de UNA ronda:
      1  si gana el jugador,
      0  si hay empate,
     -1  si gana la PC.

    Regla general:
    - Si ambas jugadas son iguales → empate.
    - Si (jugador, pc) está en REGLAS → gana jugador.
    - Si no, gana la PC.
    """
    if jugador == pc:
        return 0
    if (jugador, pc) in REGLAS:
        return 1
    return -1


def imprimir_titulo():
    print("\n====================================")
    print("      JUEGO: PIEDRA, PAPEL o TIJERA")
    print("====================================\n")


def imprimir_reglas():
    print("Reglas básicas:")
    print(" - Piedra aplasta Tijera")
    print(" - Tijera corta Papel")
    print(" - Papel envuelve Piedra\n")


# ---------------------------------------
# 3) Lógica de UNA RONDA
# ---------------------------------------
def jugar_ronda() -> int | None:
    """
    Ejecuta UNA ronda:
      - Pide jugada al usuario.
      - Si escribe 'salir', devolvemos None → señal de salida anticipada.
      - La PC elige al azar.
      - Mostramos jugadas y explicación del resultado.
      - Devolvemos  1 / 0 / -1 según el ganador.
    """
    jug = pedir_jugada_usuario()
    if jug == "salir":
        # None = “el usuario sale”: el proceso que nos llamó decide qué hacer.
        return None

    pc = elegir_jugada_pc()
    print(f"  Tú elegiste: {jug}  |  PC eligió: {pc}")

    r = resultado_ronda(jug, pc)
    if r == 0:
        print("  → Empate. Nadie suma puntos.\n")
    elif r == 1:
        print(f"  → ¡Ganaste la ronda! {REGLAS.get((jug, pc), '')}\n")
    else:
        print(f"  → Perdiste la ronda. {REGLAS.get((pc, jug), '')}\n")
    return r


# ---------------------------------------
# 4) Una PARTIDA completa (mejor de N)
# ---------------------------------------
def jugar_partida(mejor_de: int) -> tuple[int, int] | None:
    """
    Juega una PARTIDA completa hasta que alguien alcance el objetivo.
    El “objetivo” es la mitad de N redondeada hacia arriba: mejor_de//2 + 1.
    Devuelve (puntos_jugador, puntos_pc) si terminas.
    Devuelve None si el usuario salió antes de terminar.
    """
    objetivo = mejor_de // 2 + 1  # p.ej.: mejor de 3 → objetivo 2
    puntos_j, puntos_pc = 0, 0

    imprimir_reglas()
    print(f"Comienza la partida: ¡gana quien llegue a {objetivo} punto(s) primero!\n")

    while puntos_j < objetivo and puntos_pc < objetivo:
        r = jugar_ronda()

        # Si r es None, el usuario escribió 'salir' en la ronda:
        if r is None:
            print("\nHas elegido salir de la partida. ¡Hasta la próxima!\n")
            return None

        if r == 1:
            puntos_j += 1
        elif r == -1:
            puntos_pc += 1

        print(f"Marcador → Tú: {puntos_j} | PC: {puntos_pc}\n")

    # Resultado final:
    print("=========== RESULTADO FINAL ===========")
    if puntos_j > puntos_pc:
        print("🎉 ¡Felicitaciones! Ganaste la partida.\n")
    elif puntos_pc > puntos_j:
        print("🤖 La PC ganó la partida. ¡Buen juego!\n")
    else:
        print("🤝 ¡Empate final!\n")  # (con objetivo impar no debería ocurrir)
    return (puntos_j, puntos_pc)


# ---------------------------------------
# 5) Menú principal (permite rejugar)
# ---------------------------------------
def preguntar_si(texto: str) -> bool:
    """Pregunta “(s/n)” y devuelve True si la respuesta comienza con 's'."""
    resp = limpiar(input(texto + " (s/n): "))
    return resp.startswith("s")


def main():
    # “Semilla” de la aleatoriedad. Sin argumentos → no determinista (ok).
    random.seed()
    imprimir_titulo()

    while True:
        print("Menú:")
        print("  1) Jugar (mejor de 3)")
        print("  2) Jugar con objetivo personalizado (mejor de N)")
        print("  3) Ver reglas")
        print("  4) Salir\n")

        opcion = limpiar(input("Elige una opción: "))
        print()

        if opcion == "1":
            resultado = jugar_partida(mejor_de=3)

        elif opcion == "2":
            n = pedir_mejor_de()
            resultado = jugar_partida(mejor_de=n)

        elif opcion == "3":
            imprimir_reglas()
            continue

        elif opcion in {"4", "salir"}:
            print("¡Gracias por jugar! 👋")
            break

        else:
            print("Opción no válida. Intenta de nuevo.\n")
            continue

        # Si el usuario salió durante la partida, no preguntamos “volver a jugar”
        if resultado is None:
            break

        # Ofrecer otra partida
        if not preguntar_si("¿Quieres jugar otra partida?"):
            print("\n¡Gracias por jugar! 👋")
            break

        print("\n" + "=" * 38 + "\n")


# Punto de entrada: esto hace que main() se ejecute
# solo si corres este archivo directamente (y no si lo importas desde otro).
if __name__ == "__main__":
    main()
