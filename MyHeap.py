from typing import List


def heapify(array: List, i=0, key=lambda x: x) -> bool:
    if not type(array) == list:
        raise TypeError("First argument isn't list")

    array_size = len(array)

    while True:
        leftChild = i * 2 + 1
        rightChild = i * 2 + 2
        smallestChild = i

        if leftChild < array_size and key(array[leftChild]) < key(array[smallestChild]):
            smallestChild = leftChild
        if rightChild < array_size and key(array[rightChild]) < key(array[smallestChild]):
            smallestChild = rightChild

        if smallestChild == i:
            break

        ancestor_value = array[i]
        array[i] = array[smallestChild]
        array[smallestChild] = ancestor_value

        i = smallestChild

    return True


def build_heap(array: List, key=lambda x: x) -> bool:
    if not type(array) == list:
        raise TypeError("First argument isn't list")

    for i in range((len(array) // 2) - 1, -1, -1):
        heapify(array, i, key=key)

    return True


def heap_push(array: List, value, key=lambda x: x) -> bool:
    if not type(array) == list:
        raise TypeError("First argument isn't list")

    array.append(value)
    i = len(array) - 1
    ancestor = (i - 1) // 2

    while i > 0 and key(array[i]) < key(array[ancestor]):
        child_value = array[i]
        array[i] = array[ancestor]
        array[ancestor] = child_value

        i = ancestor
        ancestor = (i - 1) // 2

    return True


def heap_getTop(array: List, sorting=False, key=lambda x: x) -> int:
    if not type(array) == list:
        raise TypeError("First argument isn't list")

    top_element = array[0]
    array[0] = array[len(array) - 1]
    array[:] = array[:len(array) - 1]
    if not sorting:
        heapify(array, 0, key=key)

    return top_element


def heap_sort(array: List, key=lambda x: x, reverse=False) -> List:
    if not type(array) == list:
        raise TypeError("First argument isn't list")

    result = []
    current_heap = array[:]
    build_heap(current_heap, key=key)
    heap_print(current_heap)
    for i in range(len(current_heap) - 1, -1, -1):
        result.append(heap_getTop(current_heap, sorting=True, key=key))
        heapify(current_heap, 0, key=key)

    if reverse:
        result = result[::-1]

    return result


def heap_print(array: List, objects_size=2, gaps=True) -> None:
    if not type(array) == list:
        raise TypeError("First argument isn't list")

    heap_levels = 0
    size = len(array) - 1
    while size > 0:
        heap_levels += 1
        size //= 2

    i = 0
    indent = objects_size * " " * (2 ** heap_levels)
    sep = objects_size * " " * (2 * len(indent) - 1)
    missing_lines = heap_levels
    if not gaps:
        missing_lines = 1
    current_level = str()
    current_level_size = 1
    while True:
        for _ in range(current_level_size):
            if i == len(array):
                if current_level:
                    print(current_level)
                print("")
                return None
            if not current_level:
                current_level += indent
            else:
                current_level += sep
            current_level += str(array[i])
            i += 1
        print(current_level, end="\n" * missing_lines)
        current_level = str()
        current_level_size *= 2
        indent = indent[:len(indent) // 2]
        sep = " " * (2 * len(indent) - 1)
        missing_lines = max(1, missing_lines - 1)
