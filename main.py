def combinar_listas(lista1, lista2):
    """
    Combina dos listas intercalando sus elementos. Si una lista es más larga,
    sus elementos restantes se añaden al final de la lista resultado.
    """
    lista_resultado = []
    
    # 1. Determinar la longitud de la lista más corta
    #    Esto define cuántas veces podemos hacer la intercalación (recorrido sucesivo)
    longitud_minima = min(len(lista1), len(lista2))
    
    # 2. Intercalar elementos hasta la longitud_minima
    for i in range(longitud_minima):
        # Añade el elemento de la Lista 1
        lista_resultado.append(lista1[i])
        # Añade el elemento de la Lista 2
        lista_resultado.append(lista2[i])
        
    # 3. Añadir los elementos restantes 
    #    Los elementos restantes comienzan desde el índice longitud_minima
    
    # Si Lista1 es más larga, añade los restantes de Lista1
    if len(lista1) > longitud_minima:
        # Se añade la sublista desde el índice 'longitud_minima' hasta el final
        lista_resultado.extend(lista1[longitud_minima:])
        
    # Si Lista2 es más larga, añade los restantes de Lista2
    elif len(lista2) > longitud_minima:
        # Se añade la sublista desde el índice 'longitud_minima' hasta el final
        lista_resultado.extend(lista2[longitud_minima:])
        
    return lista_resultado

# --- Ejemplo de Ejecución ---
lista1_ejemplo = ["Hola", "nombre", "Oliver", "García"]
lista2_ejemplo = ["mi", "es"]

lista_combinada = combinar_listas(lista1_ejemplo, lista2_ejemplo)

print(f"Lista 1: {lista1_ejemplo}")
print(f"Lista 2: {lista2_ejemplo}")
print(f"Lista Resultado: {lista_combinada}")
