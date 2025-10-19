# Piedra, Papel o Tijera — Versión Final

- **Desarrollador:**
  - Jorge Claudio (<joclaudiodi@uide.edu.ec>)
- **Fecha de entrega:** 19/10/2025

---

## Objetivo del programa
Desarrollar un juego de **Piedra, Papel o Tijera** en Python que permita:
- Jugar partidas **“mejor de N”** (por defecto mejor de 3, o un **N impar** elegido por la persona).
- Mostrar **reglas** y controles antes de jugar.
- Ser tolerante con entradas (atajos: **p**, **pa**, **t**) y permitir **salir** en cualquier momento escribiendo `salir`.
- Brindar **mensajes claros** y **marcador** después de cada ronda y al finalizar la partida.

---

##  Funcionalidades principales

### Menú interactivo en consola
1) **Jugar mejor de 3**  
2) **Jugar con objetivo personalizado** (mejor de **N impar**)  
3) **Ver reglas**  
4) **Salir**

### Validación de entradas
- Acepta `piedra / papel / tijera` y atajos `p / pa / t`.
- Cualquier entrada incorrecta **vuelve a pedir** el dato sin crashear.

### Salir cuando quieras
- Escribe `salir` en el menú o en el momento de elegir tu jugada.

### Rondas impar (sin empates finales)
- El objetivo es **impar**, por lo que **siempre hay un ganador** de la partida.

### Marcador y explicación
- Muestra el **marcador** tras cada ronda y una **frase de explicación** del resultado (ej. “tijera corta papel”).

### Código documentado
- Funciones con **docstrings** y **comentarios** didácticos para facilitar la lectura.

---
## Uso rápido (flujo)

Menú → elige 1 para “mejor de 3” o 2 para elegir tu propio N impar (ej. 5, 7…).

En cada ronda escribe tu jugada: piedra, papel, tijera (o p, pa, t).

El programa muestra:

- Tu jugada y la de la PC

- Resultado de la ronda (ganas, pierdes o empatas)

- Marcador actualizado

La partida termina cuando alguien alcanza el objetivo (N//2 + 1).

Escribe salir en cualquier momento para terminar.

Lógica y estructura (resumen técnico)

## Estructura principal

- main() → muestra el menú, orquesta el flujo y llama al resto.

- jugar_partida(mejor_de) → ejecuta una partida completa (mejor de N).

- jugar_ronda() → gestiona una ronda: pide jugada, genera jugada de la PC, decide el resultado.

- ganador(jugador, pc) → devuelve 1 si gana jugador, 0 empate, -1 si gana PC.

- entrada(txt) → normaliza y valida lo escrito por el usuario.

- pedir_mejor_de() → asegura que el objetivo N sea impar y ≥ 3.

- imprimir_reglas() → explica controles y reglas.

Decisiones (condicionales): validación de entradas, reglas del juego, final de partida.
Bucles:

- While en el menú (hasta que se elija salir).

- While en la partida (hasta que alguien alcance el objetivo).

Aleatoriedad: random.choice(["piedra", "papel", "tijera"]) para la jugada de la PC.

## Resultados y conclusiones

- Se implementó un juego funcional y robusto, con interfaz por consola fácil de usar.

- El código demuestra manejo de funciones, condicionales, bucles, validaciones y aleatoriedad.

- Se pensó en la experiencia del usuario: menú claro, reglas visibles, atajos y opción de salir siempre.
