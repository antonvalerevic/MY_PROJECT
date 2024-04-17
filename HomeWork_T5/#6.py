# Уникальные числа

def check_unique_elements(nums):
    unique_nums = set(nums)
    if len(unique_nums) == len(nums):
        print("Все числа в списке уникальны")
    else:
        duplicated_nums = {}
        for num in nums:
            if num in duplicated_nums:
                duplicated_nums[num] += 1
            else:
                duplicated_nums[num] = 1

        print("Не все числа в списке уникальны")
        print("Дублирующиеся элементы и количество их повторений:")
        for num, count in duplicated_nums.items():
            if count > 1:
                print(f"Число {num} встречается {count} раз(а)")


numbers = [1, 2, 3, 4, 5, 1, 2, 6, 7, 8, 9, 1]
check_unique_elements(numbers)
