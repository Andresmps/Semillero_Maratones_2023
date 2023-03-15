def binarySearch(array, left_index, right_index, element):
    """
    Function to find the index of the element in the array.
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """

    # Caso base
    while left_index <= right_index:

        # Forma alternativa de calcular el punto medio para
        # evitar que haya un error de calculo para valores muy grandes
        mid = left_index + (right_index - left_index) // 2

        # Si el elemento esta en la mitad
        if array[mid] == element:
            return mid

        # Si el elemento esta en la parte derecha de la mitad
        elif array[mid] < element:
            left_index = mid + 1

        # Si el elemento esta en la parte izquierda de la mitad
        else:
            right_index = mid - 1

    # El elemento no esta en el arreglo
    return -1


# https://www.geeksforgeeks.org/binary-search/
# -----------------------------------------------------
# Ejemplo
arr = [2, 3, 4, 10, 40]
x = 10

result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")

# Out:
# Element is present at index  3
# -----------------------------------------------------
