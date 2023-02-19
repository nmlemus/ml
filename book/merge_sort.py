def mergeSort(array):
    # Si la longitud del array es menor o igual a 1, regresar el array tal cual.
    if len(array) <= 1:
        return array

    # Determinar la mitad del array.
    middle = len(array) // 2

    # Dividir el array en dos partes, la izquierda y la derecha.
    leftArray = array[:middle]
    rightArray = array[middle:]

    # Ordenar recursivamente ambas partes.
    leftArray = mergeSort(leftArray)
    rightArray = mergeSort(rightArray)

    # Fusionar las dos partes ordenadas.
    return merge(leftArray, rightArray)


def merge(leftArray, rightArray):
    # Crear un array vacío para almacenar el resultado de la fusión.
    result = []

    # Índices para recorrer las dos partes.
    leftIndex = 0
    rightIndex = 0

    # Mientras los índices estén dentro de sus respectivos arrays.
    while leftIndex < len(leftArray) and rightIndex < len(rightArray):
        # Si el elemento en el índice izquierdo es menor o igual al de la derecha.
        if leftArray[leftIndex] <= rightArray[rightIndex]:
            # Añadir el elemento de la izquierda al resultado y avanzar el índice izquierdo.
            result.append(leftArray[leftIndex])
            leftIndex += 1
        else:
            # Añadir el elemento de la derecha al resultado y avanzar el índice derecho.
            result.append(rightArray[rightIndex])
            rightIndex += 1

    # Agregar cualquier elemento restante en la parte izquierda al resultado.
    while leftIndex < len(leftArray):
        result.append(leftArray[leftIndex])
        leftIndex += 1

    # Agregar cualquier elemento restante en la parte derecha al resultado.
    while rightIndex < len(rightArray):
        result.append(rightArray[rightIndex])
        rightIndex += 1

    # Regresar el resultado de la fusión.
    return result
