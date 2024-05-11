# Реализовать функцию, которая находит сумму
# элементов на главной диагонали и сумму элементов на
# побочной диагонали (матрица M x N)

def diagonal_sums(matrix):
    diagonal_1_sum = sum(matrix[i][i] for i in range(min(len(matrix), len(matrix))))
    diagonal_2_sum = sum(matrix[i][len(matrix) - i - 1] for i in range(min(len(matrix), len(matrix))))
    return diagonal_1_sum, diagonal_2_sum
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
diagonal_1_sum, diagonal_2_sum = diagonal_sums(matrix)
print("1 diagonal sum:", diagonal_1_sum)
print("2 diagonal sum:", diagonal_2_sum)