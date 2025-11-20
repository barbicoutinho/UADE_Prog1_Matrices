import random

def crearTablero(n):
    """
    Crea un tablero de tamaño N x N (matriz) inicializado con espacios (' ').
    """
    # Se crea una lista de listas (matriz) donde cada elemento es un espacio.
    # 
    tablero = [[' ' for _ in range(n)] for _ in range(n)]
    return tablero

def colocarTesoro(tablero):
    """
    Coloca un tesoro aleatoriamente en una posición del tablero.
    Retorna la posición (fila, columna) del tesoro.
    """
    n = len(tablero)
    # Genera un índice de fila aleatorio entre 0 y N-1
    fila_tesoro = random.randint(0, n - 1)
    # Genera un índice de columna aleatorio entre 0 y N-1
    columna_tesoro = random.randint(0, n - 1)
    
    # Marca la posición del tesoro en el tablero (opcional, para visualización interna)
    # En este caso, solo retornaremos las coordenadas, sin modificar el tablero visible.
    
    return (fila_tesoro, columna_tesoro)

def obtenerTamanioTablero():
    """
    Solicita el tamaño del tablero (N) al usuario y valida que sea un entero mayor que cero.
    """
    while True:
        try:
            n_str = input("Ingrese el tamaño del tablero (N): ")
            n = int(n_str)
            if n > 0:
                return n
            else:
                print("Error: El tamaño debe ser un número entero mayor que cero.")
        except ValueError:
            print("Error: Ingrese un número entero válido.")

def jugarTesoroEscondido():
    """
    Función principal que implementa la lógica del juego.
    """
    print("--- Juego del Tesoro Escondido ---")
    
    # 1. Solicitar y validar el tamaño del tablero (N)
    n = obtenerTamanioTablero()
    
    # 2. Crear el tablero
    tablero = crearTablero(n)
    
    # 3. Colocar el tesoro y guardar su posición
    posicion_tesoro = colocarTesoro(tablero)
    fila_tesoro, columna_tesoro = posicion_tesoro
    
    intentos = 0
    tesoro_encontrado = False
    
    print(f"\nTablero de {n}x{n} creado. ¡A buscar el tesoro!")
    print("Las coordenadas de fila y columna deben estar entre 1 y", n)
    
    # Bucle principal del juego
    while not tesoro_encontrado:
        intentos += 1
        
        print(f"\n--- Intento N° {intentos} ---")
        
        # 4. Solicitar coordenadas del jugador
        try:
            # Solicitamos al usuario coordenadas base 1 (entre 1 y N)
            fila_usuario = int(input(f"Ingrese Fila (1 a {n}): "))
            columna_usuario = int(input(f"Ingrese Columna (1 a {n}): "))
            
            # 5. Convertir a coordenadas base 0 (índices de la matriz)
            # Esto es crucial para trabajar con Python: índice = coordenada - 1
            fila_adivinada = fila_usuario - 1
            columna_adivinada = columna_usuario - 1
            
            # 6. Validar que las coordenadas estén dentro de los límites del tablero (1 a N)
            if not (1 <= fila_usuario <= n and 1 <= columna_usuario <= n):
                print("¡Error! Las coordenadas ingresadas están fuera del tablero. Inténtalo de nuevo.")
                intentos -= 1 # No contamos el intento si la coordenada es inválida
                continue
                
            # 7. Verificar si las coordenadas coinciden con la ubicación del tesoro
            if fila_adivinada == fila_tesoro and columna_adivinada == columna_tesoro:
                tesoro_encontrado = True
                print("\n¡Felicitaciones! Has encontrado el tesoro.")
            else:
                print("Inténtalo de nuevo. Las coordenadas no son correctas.")
                
        except ValueError:
            print("¡Error! Por favor, ingresa solo números enteros para las coordenadas.")
            intentos -= 1 # No contamos el intento si la entrada es inválida
            continue
            
    # 8. Mostrar el resultado final
    print(f"\n--- FIN DEL JUEGO ---")
    print(f"El tesoro se encontraba en la posición (Fila: {fila_tesoro + 1}, Columna: {columna_tesoro + 1}).")
    print(f"Cantidad total de intentos realizados: {intentos}")

# Ejecutar el juego
if __name__ == "__main__":
    jugarTesoroEscondido()
