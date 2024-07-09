# Завдання 1
# Створіть функцію, яка повертає список з усіма простими
# числами від 0 до 1000.
# Використовуючи механізм декораторів, підрахуйте, скіль-
# ки секунд знадобилося для обчислення усіх простих чисел.
# Виведіть на екран кількість секунд та прості числа.

import math
import time

# class PrimeNumber:
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop
# # Здесь мне понадобилось очень много времени что бы понять что декоратор должен быть статическим методом
# # без этого никак не хотел работать
#     @staticmethod
#     def time_prime_number(func):
#         def wrapper(self, *args, **kwargs):
#             start_time = time.perf_counter()
#             result = func(self, *args, **kwargs)
#             stop_time = time.perf_counter()
#             print(f'Total time: {stop_time - start_time:6f} sec.')
#             return result
#         return wrapper
#
#     def prime_number(self, n):
#         for i in range(2, int(math.sqrt(n)) + 1):
#             if n % i == 0:
#                 return False
#         return True
#
#     @time_prime_number
#     def list_prime_number(self):
#         primes = []
#         for j in range(self.start, self.stop + 1):
#             if self.prime_number(j):
#                 primes.append(j)
#         return primes
#
# thousand = PrimeNumber(1, 1000)
# print(thousand.list_prime_number())

# Завдання 2
# Додайте до першого завдання можливість передавати
# межі діапазону для пошуку усіх простих чисел.

# Эту задачу я решил с помощью применения декоратора класса.

class Counter:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.perf_counter()
        result = self.func(*args, **kwargs)
        stop_time = time.perf_counter()
        print(f'Total time: {stop_time - start_time:6f} sec.')
        return result


def prime_number(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

@Counter
def list_prime_number(start, stop):
    primes = []
    for j in range(start, stop + 1):
        if prime_number(j):
            primes.append(j)
    return primes


start = int(input('Enter start number: ')) # проверки на валидацию значений я не делал, что бы не утяжелять код.
stop = int(input('Enter stop number: '))

thousand = list_prime_number(start, stop)
print(thousand)
