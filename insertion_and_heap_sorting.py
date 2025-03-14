# -*- coding: utf-8 -*-
"""insertion_heap_sorting.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WdaM2tIVcy3jale2IXKdA0b9fB5VV7Mz
"""
#heap sort

import random
import time
import matplotlib.pyplot as plt


def heapify(arr, n, i):
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


sizes = [100, 200, 400, 800, 1600, 3200]
heap_sort_times = []

for size in sizes:
    arr = random.sample(range(1, size*10), size)
    start_time = time.time()
    heap_sort(arr.copy())
    heap_sort_times.append(time.time() - start_time)


plt.figure(figsize=(10, 6))
plt.plot(sizes, heap_sort_times, label="Heap Sort (O(n log n))", marker='o')
plt.xlabel("Input Size")
plt.ylabel("Time (seconds)")
plt.title("Heap Sort Time Complexity")
plt.legend()
plt.grid(True)
plt.show()

#insertion sort

import random
import time
import matplotlib.pyplot as plt


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


sizes = [100, 200, 400, 800, 1600, 3200]
insertion_times = []

for size in sizes:
    arr = random.sample(range(1, size*10), size)
    start_time = time.time()
    insertion_sort(arr.copy())
    insertion_times.append(time.time() - start_time)


plt.figure(figsize=(10, 6))
plt.plot(sizes, insertion_times, label="Insertion Sort (O(n²))", marker='o')
plt.xlabel("Input Size")
plt.ylabel("Time (seconds)")
plt.title("Insertion Sort Time Complexity")
plt.legend()
plt.grid(True)
plt.show()
