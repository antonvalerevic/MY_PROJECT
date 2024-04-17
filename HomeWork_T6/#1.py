# 1 бинарный поиск

def binary_search(arr, n):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == n:
            return mid
        elif arr[mid] < n:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Пример использования
arr = [1, 3, 5, 7, 9, 11, 13]
n = 12
result = binary_search(arr, n)

if result != -1:
    print(f"Искомый элемент {n} находится на позиции {result} в исходном списке.")
else:
    print("Искомый элемент не найден в исходном списке.")
