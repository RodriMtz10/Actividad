def lru_replacement(paginas, marcos):
    """
    Simula el algoritmo de reemplazo de páginas LRU.
    
    :param paginas: Lista de referencias a páginas.
    :param marcos: Número de marcos disponibles en memoria.
    """
    memoria = []  # Lista para simular los marcos de páginas
    fallos = 0  # Contador de fallos de página

    for pagina in paginas:
        if pagina not in memoria:
            # Si la página no está en memoria, ocurre un fallo de página
            if len(memoria) < marcos:
                # Si hay espacio disponible, simplemente añadimos la página
                memoria.append(pagina)
            else:
                # Reemplazamos la página menos recientemente usada
                memoria.pop(0)
                memoria.append(pagina)
            fallos += 1
            print(f"Fallo de página: {pagina} cargada -> {memoria}")
        else:
            # Si la página está en memoria, la actualizamos como más recientemente usada
            memoria.remove(pagina)
            memoria.append(pagina)
            print(f"Acceso exitoso: {pagina} -> {memoria}")

    print(f"\nNúmero total de fallos de página: {fallos}")


# Simulación
if __name__ == "__main__":
    # Lista de referencias a páginas
    paginas = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    # Número de marcos disponibles
    marcos = 3

    print("Simulación del algoritmo LRU:\n")
    lru_replacement(paginas, marcos)