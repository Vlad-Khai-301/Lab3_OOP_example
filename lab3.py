# підключення необхідних бібліотек
import numpy as np


def power_a3(a):
    """a - ціле число. Повертає A^3"""
    return a ** 3


def power_a3_for_list(list_of_a):
    """Функція для обробки списку вхідних даних відповідно до функції за варіантом"""
    out_data = []
    for a in list_of_a:  # Для кожного елемента вхідного списку
        out_data.append(power_a3(a))
    return out_data


def task1_standart():
    """Введення вхідних даних, виклик функції за варіантом,
    виведення результатів"""
    in_data = []
    try:
        in_num = int(input("Введіть кількість вхідних елементів: "))
        for i in range(in_num):
            temp = int(input(f"{i+1} element: "))
            in_data.append(temp)
    except ValueError:
        print("Помилка при введенні вхідних даних!")
    else:
        print("Numbers, raised in 3 power: ", power_a3_for_list(in_data))


def task1_list_comprehension():
    """Введення вхідних даних, виклик функції за варіантом,
    виведення результатів"""
    try:
        in_num = int(input("Введіть кількість вхідних елементів: "))
        in_data = [int(input(f"{i+1} element: ")) for i in range(in_num)]
        # in_data = [int(element) for element in input("Enter numbers: ").split()]
    except ValueError:
        print("Помилка при введенні вхідних даних!")
    else:
        out_data = [power_a3(a) for a in in_data]
        print("Numbers, raised in 3 power: ", out_data)


def task1_lambda():
    """Введення вхідних даних, виклик функції за варіантом,
    виведення результатів"""
    try:
        in_data = list(map(lambda e: int(e), input("Enter numbers: ").split()))
    except ValueError:
        print("Помилка при введенні вхідних даних!")
    else:
        out_data = list(map(lambda a: power_a3(a), in_data))
        print("Numbers, raised in 3 power: ", out_data)


def matrix1(filename):
    """Зчитування матриці з файлу, підрахунок параметрів
    та виконання операції над матрицею"""
    M = N = K = 0
    with open(filename, 'r') as f:
        param_line = f.readline().split(" ")  # "3 4 3" ["3", "4", "3"]
        try:
            M = int(param_line[0])
            N = int(param_line[1])
            K = int(param_line[2])
            if K < 1 or K > M:
                raise ValueError
        except ValueError:
            print("Wrong file data")
        else:
            input = np.loadtxt(filename, skiprows=1, max_rows=M)
            print(input)
            # Підрахунок параметрів задачі
            sum_K = np.sum(input, axis=1)[K - 1]  # [[1, 2], [3, 1]] -> [3, 4]
            prod_K = np.prod(input, axis=1)[K - 1]
            ones = np.ones((M, N))
            changed_matrix = input - ones
        
            means = np.mean(input, axis=1).reshape(-1, 1)
            print(means)
            tmp_matr = np.where(input - means > 0, 1, 0)
            print(tmp_matr)
            elements_amount = np.sum(tmp_matr, axis=1)
            print(elements_amount)
        
            return sum_K, prod_K, changed_matrix
    
    return 0, 0, np.zeros((M, N))


def task2():
    """Введення імені вхідного файлу, виклик функції для зчитування
    і обробки матриці, виведення результатів"""
    filename = input("Enter filename (.txt): ")
    sum_K, prod_K, changed_matrix = matrix1(filename)
    print(f"Сума K-го рядка: {sum_K}\nДобуток K-го рядка: {prod_K}\nЗмінена матриця:\n{changed_matrix}")
