# Программа получает на вход число H. Реализовать
# функцию, которая определяет, какие столбцы имеют хотя бы
# одно такое же число, а какие не имеют (матрица M x N)

def find_columns_with_number(matrix, H):
    num_cols = len(matrix)
    columns_with_H = [False] * num_cols

    for row in matrix:
        for col_idx, elem in enumerate(row):
            if elem == H:
                columns_with_H[col_idx] = True

    columns_with_H_indices = [i for i, x in enumerate(columns_with_H) if x]
    columns_without_H_indices = [i for i, x in enumerate(columns_with_H) if not x]

    return columns_with_H_indices, columns_without_H_indices
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
H = 5
columns_with_H, columns_without_H = find_columns_with_number(matrix, H)
print("Columns with", H, ":", columns_with_H)
print("Columns without", H, ":", columns_without_H)