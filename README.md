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

