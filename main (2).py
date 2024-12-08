# Функция для восстановления кучи
def heapify(arr, n, i):
    largest = i  # Изначально считаем, что корень самый большой
    left = 2 * i + 1  # Левый дочерний элемент
    right = 2 * i + 2  # Правый дочерний элемент

    # Проверка, если левый дочерний элемент больше
    if left < n and arr[largest] < arr[left]:
        largest = left

    # Проверка, если правый дочерний элемент больше
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Если нужно, меняем элементы местами и восстанавливаем кучу рекурсивно
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Обмен значениями
        heapify(arr, n, largest)  # Рекурсивный вызов для восстановления


# Функция для построения кучи
def build_heap(arr):
    n = len(arr)
    # Проходим с последнего внутреннего узла к корню
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


# Импортируем библиотеки
import random  # Для генерации случайных чисел
import time  # Для замера времени
import matplotlib.pyplot as plt  # Для построения графиков


# Функция для измерения времени построения кучи
def measure_build_heap_time(array_size):
    arr = [random.randint(0, 100000) for _ in range(array_size)]  # Генерация массива
    start_time = time.time()  # Начало отсчета времени
    build_heap(arr)  # Строим кучу
    end_time = time.time()  # Окончание отсчета времени
    return end_time - start_time  # Возвращаем время выполнения


# Список размеров массивов для тестирования
sizes = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
times = []  # Список для хранения времени выполнения

# Тестируем построение кучи для каждого размера массива
for size in sizes:
    time_taken = measure_build_heap_time(size)  # Замер времени
    times.append(time_taken)  # Сохраняем результат
    print(f"Размер массива: {size}, Время: {time_taken:.6f} секунд")  # Выводим время

# Строим график зависимости времени от размера массива
plt.plot(sizes, times, marker='o')  # Строим график
plt.xlabel('Размер массива')  # Подпись оси X
plt.ylabel('Время (секунды)')  # Подпись оси Y
plt.title('Время построения кучи в зависимости от размера массива')  # Заголовок
plt.xscale('log')  # Логарифмическая шкала для оси X
plt.yscale('log')  # Логарифмическая шкала для оси Y
plt.grid(True)  # Сетка на графике
plt.show()  # Показываем график
