import time
import random
import tracemalloc

# ---------------------------
# Insertion Sort
# ---------------------------
def insertion_sort(arr):
    # Make a copy so the original list remains unchanged
    a = arr.copy()

    comparisons = 0   # counts each comparison between two values
    swaps = 0         # counts shifts/moves in the array

    # Start at index 1 (index 0 is already "sorted" by itself)
    for i in range(1, len(a)):
        key = a[i]      # the value we want to insert
        j = i - 1       # start checking to the left

        # Move elements to the right until we find the correct spot
        while j >= 0:
            comparisons += 1  # each loop compares a[j] with key

            if a[j] > key:
                a[j + 1] = a[j]   # shift value to the right
                swaps += 1        # count this move as a swap
                j -= 1
            else:
                break

        # Insert the key in its correct position
        a[j + 1] = key
    return a, comparisons, swaps

# ------------------------------------------------------------
#   Runs insertion sort on a random list and displays metrics
# ------------------------------------------------------------
def test_insertion_sort(arr):
    # Keep a copy for printing before sorting
    unsorted_list = arr.copy()

    # Start timing/memory
    start = time.time()
    tracemalloc.start()

    # Perform the sort and retrieve metrics
    sorted_arr, comparisons, swaps = insertion_sort(arr)

    # End timing/memory
    end = time.time()
    current, peak = tracemalloc.get_traced_memory()

    # Force a readable decimal (not scientific notation)
    exec_time = end - start

    # Print previews (first 20 values only)
    # print("\nUnsorted list:", unsorted_list[:20])
    # print("Sorted list:", sorted_arr[:20])

    # # Print performance numbers
    # print("Comparisons:", comparisons)
    # print("Swaps:", swaps)
    # print("Time:", exec_time, "seconds")

    metrics = {
        "unsorted_list": unsorted_list,
        "sorted_list": sorted_arr,
        "sizes": len(arr),
        "comparisons": comparisons,
        "swaps": swaps,
        "recursive_calls": 0,
        "execution_time": exec_time,
        "current_memory": current / 1024,
        "peak_memory": peak / 1024
    }
    return arr, metrics

# ---------------------------
# Main
# ---------------------------
if __name__ == "__main__":
    arr = [random.randint(0, 15000) for _ in range(100)]
    metrics = test_insertion_sort(arr)

    import json
    print(json.dumps(metrics, indent=4))

