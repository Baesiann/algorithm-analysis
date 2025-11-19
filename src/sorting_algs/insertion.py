import time
import random

# ---------------------------
# Insertion Sort
# ---------------------------
def insertion_sort(arr):
    a = arr[:]  # keep original intact
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

# ---------------------------
# Timing helper
# ---------------------------
def measure(func, arr):
    start = time.time()
    sorted_arr = func(arr)
    end = time.time()
    return sorted_arr, end - start

# ---------------------------
# Generate datasets
# ---------------------------
def generate(n):
    unsorted_data = [random.randint(0, n) for _ in range(n)]
    sorted_data = sorted(unsorted_data)
    reversed_data = sorted_data[::-1]
    return unsorted_data, sorted_data, reversed_data

# ---------------------------
# Main
# ---------------------------
def run(n=2000):
    unsorted_data, sorted_data, reversed_data = generate(n)

    # Best case (sorted)
    _, best_time = measure(insertion_sort, sorted_data)

    # Average case (random)
    _, avg_time = measure(insertion_sort, unsorted_data)

    # Worst case (reverse)
    _, worst_time = measure(insertion_sort, reversed_data)

    print("\n=== INSERTION SORT METRICS ===")
    print(f"Unsorted (Random) Time:      {avg_time:.6f} s")
    print(f"Sorted (Best Case) Time:     {best_time:.6f} s")
    print(f"Reverse-Sorted (Worst) Time: {worst_time:.6f} s")
    print("==============================\n")

run()
