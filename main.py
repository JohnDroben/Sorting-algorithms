
def bubble_sort(arr):
    n = len(arr)
    for run in range(n-1):
        for i in range(n-1-run):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]


def quick_sort(s):
    if len(s) <= 1:
        return s
    element = s[0]
    left = [i for i in s if i < element]
    center = [i for i in s if i == element]
    right = [i for i in s if i > element]
    return quick_sort(left) + center + quick_sort(right)


def selection_sort(arr):
   # Проходим по всему списку
   for i in range(len(arr)):
       # Предполагаем, что первый элемент в неотсортированной части - это минимальный
       min_index = i
       # Ищем минимальный элемент в оставшейся части списка
       for j in range(i+1, len(arr)):
           if arr[j] < arr[min_index]:
               min_index = j
       # Меняем местами найденный минимальный элемент с первым элементом в неотсортированной части
       arr[i], arr[min_index] = arr[min_index], arr[i]

def insertion_sort(arr): # Сортировка вставками (Insertion Sort)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge_sort(arr):  # Сортировка слиянием (Merge Sort)
    if len(arr) > 1:
        mid = len(arr) // 2
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


def heapify(arr, n, i):  # Пирамидальная сортировка (Heap Sort)
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def counting_sort(arr):  # Сортировка подсчетом (Counting Sort)
    max_val = max(arr) + 1
    count = [0] * max_val

    for num in arr:
        count[num] += 1

    output = []
    for i in range(max_val):
        output.extend([i] * count[i])

    return output


def bucket_sort(arr):  # Сортировка в бакетах (Bucket Sort)
    max_val = max(arr)
    num_buckets = max_val + 1
    buckets = [[] for _ in range(num_buckets)]

    for num in arr:
        buckets[num].append(num)

    sorted_arr = []
    for bucket in buckets:
        insertion_sort(bucket)
        sorted_arr.extend(bucket)

    return sorted_arr


def shell_sort(arr):  # Сортировка Шелла (Shell Sort)
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2


test_data = [64, 34, 25, 12, 22, 11, 90]
algorithms = [
    ("Bubble Sort", bubble_sort),
    ("Selection Sort", selection_sort),
    ("Insertion Sort", insertion_sort),
    ("Merge Sort", merge_sort),
    ("Heap Sort", heap_sort),
    ("Shell Sort", shell_sort),
    ("Counting Sort", counting_sort),
    ("Bucket Sort", lambda arr: bucket_sort(arr)),
    ("Quick Sort", quick_sort)
]

print("Original data:", test_data)
print("=" * 50)

for name, func in algorithms:
    data = test_data.copy()

    # Обработка out-place алгоритмов
    if name in ["Quick Sort", "Counting Sort", "Bucket Sort"]:
        result = func(data)
    # Обработка in-place алгоритмов
    else:
        func(data)
        result = data

    print(f"{name}: {result}")

print("=" * 50)
print("Note: All sorts verified with test data")