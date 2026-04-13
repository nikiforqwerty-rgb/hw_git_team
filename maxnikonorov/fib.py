def fibonacci(n):
    first_num, second_num = 0, 1
    for _ in range(n):
        first_num, second_num = second_num, first_num + second_num
    return first_num


print(fibonacci(10))
