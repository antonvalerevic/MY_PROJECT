import numpy as np
# создаем рандомную матрицу 5*5
def random_matrix(rows, cols):
    return np.round(np.random.rand(rows, cols), 2)

matrix = random_matrix(5, 5)
print(matrix)

# миниммум и максимум матрицы с индексами
def min_matrix():
    return np.min(matrix), np.unravel_index(np.argmin(matrix), matrix.shape)

def max_matrix():
    return np.max(matrix), np.unravel_index(np.argmax(matrix), matrix.shape)

min_val, min_idx = min_matrix()
print("min value:", min_val)
print("min index:", min_idx)

max_val, max_idx = max_matrix()
print("max value:", max_val)
print("max index:", max_idx)

# сумма матрицы
def sum_matrix():
    return sum(sum(matrix))
sum_m = sum_matrix()
print("summa", sum_m)

# Определить, какую долю
# в общей сумме (процент) составляет сумма элементов
# каждого столбца, столбцы A, B, C, D, E

def A_sum_m():
    return np.round(sum(([1]), 1) / sum_m * 100, 2)
def B_sum_m():
    return np.round(sum(([2]), 1) / sum_m * 100, 2)
def C_sum_m():
    return np.round(sum(([3]), 1) / sum_m * 100, 2)
def D_sum_m():
    return np.round(sum(([4]), 1) / sum_m * 100, 2)
def E_sum_m():
    return np.round(sum(([5]), 1) / sum_m * 100, 2)
A = A_sum_m()
B = B_sum_m()
C = C_sum_m()
D = D_sum_m()
E = E_sum_m()
print("Доля кажого столбца от общей суммы матрицы в %:")
print(A, B, C, D, E, sep = "%, ")



