def bubble_sort(arr):
    n = len(arr)
    # Внешний цикл отвечает за количество проходов
    for i in range(n):
        # Внутренний цикл сравнивает соседние элементы
        # С каждым проходом последний элемент уже на своем месте, поэтому n-i-1
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Меняем элементы местами
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers)
print(f"Отсортированный список: {sorted_numbers}")