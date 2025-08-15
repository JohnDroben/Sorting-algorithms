# Sorting-algorithms
# Коллекция алгоритмов сортировки на Python

Этот проект содержит реализации различных алгоритмов сортировки на Python с подробными комментариями и тестовым примером. Проект идеально подходит для изучения принципов работы алгоритмов сортировки и их сравнения.

## Реализованные алгоритмы

1. **Пузырьковая сортировка (Bubble Sort)**
2. **Сортировка выбором (Selection Sort)**
3. **Сортировка вставками (Insertion Sort)**
4. **Быстрая сортировка (Quick Sort)**
5. **Сортировка слиянием (Merge Sort)**
6. **Пирамидальная сортировка (Heap Sort)**
7. **Сортировка Шелла (Shell Sort)**
8. **Сортировка подсчетом (Counting Sort)**
9. **Блочная сортировка (Bucket Sort)**

## Как использовать

1. Скопируйте весь код в файл `sorting_algorithms.py`
2. Запустите файл с помощью Python:

```bash
python sorting_algorithms.py
```

3. В выводе вы увидите результаты работы всех алгоритмов сортировки на одних и тех же тестовых данных

## Подробное описание алгоритмов

### 1. Пузырьковая сортировка (Bubble Sort)
```python
def bubble_sort(arr):
    n = len(arr)
    for run in range(n-1):
        for i in range(n-1-run):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
```
- **Принцип работы**: Последовательно сравнивает соседние элементы и меняет их местами, если они расположены в неправильном порядке
- **Сложность**: O(n²) в худшем и среднем случае
- **Особенности**: Простая реализация, но неэффективна для больших массивов

### 2. Сортировка выбором (Selection Sort)
```python
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
```
- **Принцип работы**: На каждом проходе находит минимальный элемент в неотсортированной части и помещает его в конец отсортированной части
- **Сложность**: O(n²)
- **Особенности**: Минимальное количество перестановок (O(n))

### 3. Сортировка вставками (Insertion Sort)
```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
```
- **Принцип работы**: Элементы поочередно вставляются в отсортированную часть массива на правильную позицию
- **Сложность**: O(n²) в худшем случае, O(n) для почти отсортированных массивов
- **Особенности**: Эффективен для небольших массивов и почти отсортированных данных

### 4. Быстрая сортировка (Quick Sort)
```python
def quick_sort(s):
    if len(s) <= 1:
        return s
    element = s[0]
    left = [i for i in s if i < element]
    center = [i for i in s if i == element]
    right = [i for i in s if i > element]
    return quick_sort(left) + center + quick_sort(right)
```
- **Принцип работы**: Разделяй и властвуй. Выбирается опорный элемент, массив делится на три части: элементы меньше опорного, равные и больше
- **Сложность**: O(n log n) в среднем, O(n²) в худшем случае
- **Особенности**: Один из самых эффективных алгоритмов на практике

### 5. Сортировка слиянием (Merge Sort)
```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        
        merge_sort(left)
        merge_sort(right)
        
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
```
- **Принцип работы**: Рекурсивно разделяет массив на две части, сортирует их и объединяет
- **Сложность**: O(n log n) во всех случаях
- **Особенности**: Гарантированное время выполнения, требует дополнительной памяти

### 6. Пирамидальная сортировка (Heap Sort)
```python
def heapify(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)
    
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
```
- **Принцип работы**: Строит max-heap и последовательно извлекает корень
- **Сложность**: O(n log n)
- **Особенности**: Сортировка на месте, не требует дополнительной памяти

### 7. Сортировка Шелла (Shell Sort)
```python
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap //= 2
```
- **Принцип работы**: Улучшенная версия сортировки вставками, сортирует элементы на определенных интервалах
- **Сложность**: Зависит от выбора интервалов, O(n²) в худшем случае
- **Особенности**: Эффективен для средних по размеру массивов

### 8. Сортировка подсчетом (Counting Sort)
```python
def counting_sort(arr):
    if not arr:
        return []
    
    min_val = min(arr)
    max_val = max(arr)
    range_size = max_val - min_val + 1
    
    count = [0] * range_size
    for num in arr:
        count[num - min_val] += 1
    
    sorted_arr = []
    for i in range(range_size):
        sorted_arr.extend([i + min_val] * count[i])
    
    return sorted_arr
```
- **Принцип работы**: Подсчитывает количество каждого элемента и формирует отсортированный массив
- **Сложность**: O(n + k), где k - диапазон значений
- **Особенности**: Эффективен, когда диапазон значений небольшой

### 9. Блочная сортировка (Bucket Sort)
```python
def bucket_sort(arr, bucket_size=5):
    if not arr:
        return []
    
    min_val = min(arr)
    max_val = max(arr)
    
    bucket_count = (max_val - min_val) // bucket_size + 1
    buckets = [[] for _ in range(bucket_count)]
    
    for num in arr:
        index = (num - min_val) // bucket_size
        buckets[index].append(num)
    
    sorted_arr = []
    for bucket in buckets:
        insertion_sort(bucket)
        sorted_arr.extend(bucket)
    
    return sorted_arr
```
- **Принцип работы**: Распределяет элементы по "ведрам", сортирует каждое ведро и объединяет результаты
- **Сложность**: O(n + k) в среднем случае
- **Особенности**: Эффективен, когда входные данные равномерно распределены

## Тестирование алгоритмов

В проекте реализован единый тест для всех алгоритмов:

```python
test_data = [64, 34, 25, 12, 22, 11, 90]
algorithms = [
    ("Bubble Sort", bubble_sort),
    ("Selection Sort", selection_sort),
    # ... другие алгоритмы ...
]

for name, func in algorithms:
    data = test_data.copy()
    
    if name in ["Quick Sort", "Counting Sort", "Bucket Sort"]:
        result = func(data)
    else:
        func(data)
        result = data
    
    print(f"{name}: {result}")
```

## Результаты тестирования

При запуске теста все алгоритмы должны выдать одинаковый результат:

```
Original data: [64, 34, 25, 12, 22, 11, 90]
Bubble Sort: [11, 12, 22, 25, 34, 64, 90]
Selection Sort: [11, 12, 22, 25, 34, 64, 90]
Insertion Sort: [11, 12, 22, 25, 34, 64, 90]
Merge Sort: [11, 12, 22, 25, 34, 64, 90]
Heap Sort: [11, 12, 22, 25, 34, 64, 90]
Shell Sort: [11, 12, 22, 25, 34, 64, 90]
Counting Sort: [11, 12, 22, 25, 34, 64, 90]
Bucket Sort: [11, 12, 22, 25, 34, 64, 90]
Quick Sort: [11, 12, 22, 25, 34, 64, 90]
```

## Рекомендации по изучению

1. Начните с простых алгоритмов (пузырьковая, выбором, вставками)
2. Изучите принцип "разделяй и властвуй" на примере быстрой сортировки и сортировки слиянием
3. Разберитесь с специализированными алгоритмами (подсчетом, блочная) для специфических задач
4. Сравните производительность алгоритмов на больших массивах данных
5. Попробуйте модифицировать алгоритмы для работы с разными типами данных

## Лицензия

Этот проект распространяется под лицензией MIT. Вы можете свободно использовать код в образовательных и коммерческих целях.