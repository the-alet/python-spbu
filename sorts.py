from random import randint
from time import *

def bubble_sort(arr, n):
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

e = 256
def radix_sort(arr, n):
    # Находим максимальное число для определения разрядов
    max_num = max(arr)

    exp = 1
    while max_num // exp > 0:
        output = [0 for _ in range(n)]  # выходной массив
        count = [0 for _ in range(e)]  # массив для подсчета частоты

        # Подсчет частоты появления цифр
        for i in range(n):
            index = arr[i] // exp
            count[index % e] += 1

        # Преобразование count[i] так, чтобы он содержал
        # позицию этого разряда в выходном массиве
        for i in range(1, e):
            count[i] += count[i - 1]

        # Построение выходного массива
        for i in range(n - 1, -1, -1):
            index = arr[i] // exp
            output[count[index % e] - 1] = arr[i]
            count[index % e] -= 1

        # Копирование выходного массива обратно в arr
        for i in range(n):
            arr[i] = output[i]

        exp *= e

f = open('gen1.txt', 'r')
a = list(map(int, f.readline().split()))
f.close()

t1 = time()
radix_sort(a, len(a))
t2 = time()

f = open('sorted.txt', 'w')
for _ in range(len(a)):
    f.write(str(a[_]) + ' ')
f.close()
c = [2,3,7,4,1,2,8,9]
bubble_sort(c, 8)
print(t2 - t1)