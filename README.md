Consigna:

El desafío consiste en implementar el juego del “Tesoro Escondido” utilizando programación en Python. 
El juego requiere que el jugador adivine la ubicación de un tesoro oculto en un tablero cuadrado (misma cantidad de filas que de columnas, implementándolo con una matriz).  


 

Para poder lograr el objetivo, deberá tener en cuenta las siguientes consideraciones:  

Implementa el código para el juego "Tesoro Escondido" utilizando las funciones sugeridas a continuación.  
El juego debe comenzar solicitando al usuario que ingrese el tamaño del tablero (valor de N). 
Asegúrate de validar que el valor ingresado sea un número entero mayor que cero. 
Utiliza la función crearTablero(n) para crear un tablero vacío de tamaño N x N (filas x columnas). 
En cada elemento de la matriz, se debe poner el carácter espacio (‘ ‘). 
Utiliza la función colocarTesoro(tablero) para colocar un tesoro aleatoriamente en una posición del tablero. 
Utilice la librería random para tal fin. 
Luego, el juego debe solicitar al jugador que ingrese las coordenadas de fila y columna para buscar el tesoro.  
Utiliza una estructura de control iterativa para verificar si las coordenadas ingresadas coinciden con la ubicación del tesoro. 
Si el tesoro es encontrado, muestra el mensaje “¡Felicitaciones! Has encontrado el tesoro.” y finaliza el juego. 

Si el tesoro no es encontrado, muestra el mensaje “Inténtalo de nuevo” y permite al jugador ingresar nuevas coordenadas. 

Llevar un conteo de la cantidad de intentos realizados por el jugador. 
Al final del juego, muestra la cantidad total de intentos realizados por el jugador. 

    
