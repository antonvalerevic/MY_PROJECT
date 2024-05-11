# Дана матрица M x N. Исходная матрица состоит из
# нулей и единиц. Реализовать функцию, которая добавит к
# матрице ещё один столбец, элементы которого делает
# количество единиц в соответствующей строке чётным.


import numpy as np

matrix = np.array([[0, 1, 0], [1, 0, 1], [0, 0, 0]])
new_column = np.array([sum(row) % 2 for row in matrix]).reshape(-1, 1)
result = np.concatenate((matrix, new_column), axis=1)

print(result)