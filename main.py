import numpy as np

def find_s_special_elements(matrix):
    rows, cols = matrix.shape
    special_elements = []

    for i in range(rows):
        row_sum = np.sum(matrix[i, :])
        for j in range(cols):
            if matrix[i, j] > row_sum - matrix[i, j]:
                special_elements.append((matrix[i, j], i, j))

    return special_elements

def find_max_s_special_elements(matrix):
    special_elements = find_s_special_elements(matrix)
    if not special_elements:
        return []

    max_value = max(special_elements, key=lambda x: x[0])[0]
    max_elements = [(value, row, col) for value, row, col in special_elements if value == max_value]
    return max_elements

# Приклад використання
matrix = np.array([
    [50, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 50],
    [13, 14, 15, 16]
])

max_elements = find_max_s_special_elements(matrix)

if max_elements:
    print("Максимальні S-особливі елементи:")
    for element in max_elements:
        value, row, col = element
        print(f"Елемент: {value}, Рядок: {row + 1}, Індекси: ({row+1}, {col+1})")
else:
    print("Таких нема!")
