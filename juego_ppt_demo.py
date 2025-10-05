"""
Juego de Piedra, Papel o Tijera

Autor: Jorge Claudio
"""

import random  # Para que la computadora elija aleatoriamente

# ---- Constantes y reglas del juego ----
# Mapeo de atajos a jugadas válidas (normalización de entrada)
OPCIONES = {
    "piedra": "piedra",
    "papel":  "papel",
    "tijera": "tijera",
    "p":      "piedra",
    "pa":     "papel",
    "t":      "tijera"
}

# REGLAS: pares (gana, pierde) -> explicación textual
# Esto permite decidir el ganador consultando si (jugador, pc) está en REGLAS.
REGLAS = {
    ("piedra", "tijera"): "piedra aplasta tijera",
    ("tijera", "papel"):  "tijera corta papel",
    ("papel",  "piedra"): "papel envuelve piedra",
}

def entrada(txt: str) -> str:
    """
    Recibe el texto ingresado por el usuario y lo convierte a una jugada válida.
    Devuelve "piedra", "papel" o "tijera"; si no es válido, devuelve "".
    """
    return OPCIONES.get(txt.strip().lower(), "")

def ganador(jugador: str, computadora: str) -> int:
    """
    Determina el resultado de la ronda:
    -  1 si gana el jugador
    -  0 si hay empate
    - -1 si gana la computadora

    Lógica:
    - Empate si son iguales.
    - Si (jugador, computadora) está en REGLAS -> gana jugador.
    - En cualquier otro caso -> gana la computadora.
    """
    if jugador == computadora:
        return 0
    if (jugador, computadora) in REGLAS:
        return 1
    return -1

def jugar_ronda() -> int:
    """
    Ejecuta una sola ronda:
    - Pide y valida la jugada del usuario (con atajos).
    - La PC elige aleatoriamente.
    - Muestra resultado y explicación breve.
    Devuelve 1 / 0 / -1 según resultado.
    """
    while True:
        eleccion = input("Elige (piedra/papel/tijera) o (p/pa/t): ")
        jugada = entrada(eleccion)
        if not jugada:
            print("Entrada no válida. Intenta de nuevo.\n")
            continue

        pc = random.choice(["piedra", "papel", "tijera"])
        print(f"Tú: {jugada} | PC: {pc}")

        res = ganador(jugada, pc)
        if res == 0:
            print("Empate. No suma puntos.\n")
        elif res == 1:
            print(f"¡Ganaste la ronda! {REGLAS.get((jugada, pc), '')}\n")
        else:
            print(f"Perdiste la ronda. {REGLAS.get((pc, jugada), '')}\n")
        return res

def main():
    print("=== Juego de Piedra, Papel o Tijera ===\n")
    puntos_jg, puntos_pc = 0, 0
    objetivo = 2  # Mejor de 3: gana quien llega a 2

    # ---- BUCLE REPETITIVO PRINCIPAL ----
    while puntos_jg < objetivo and puntos_pc < objetivo:
        r = jugar_ronda()
        if r == 1:
            puntos_jg += 1
        elif r == -1:
            puntos_pc += 1
        print(f"Marcador -> Tú: {puntos_jg} | PC: {puntos_pc}\n")

    # ---- Decisión final (estructura lógica) ----
    if puntos_jg > puntos_pc:
        print("🎉 ¡Ganaste la partida (mejor de 3)!")
    else:
        print("🤖 La PC ganó la partida (mejor de 3). ¡Sigue practicando!")

if __name__ == "__main__":
    main()
