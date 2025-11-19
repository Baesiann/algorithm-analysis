import time
import random
import tracemalloc

# -----------------------------
#   SELECTION SORT FUNCTION
# -----------------------------
def selection_sort(arr):
    n = len(arr)

    comparisons = 0
    swaps = 0

    # Go through each position in the list
    for i in range(n):

        # Start by assuming the current element is the smallest
        min_index = i

        # Look through the remaining unsorted part of the list
        for j in range(i + 1, n):

            # Count each comparison
            comparisons += 1

            # Check if a smaller value is found
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the smallest item into position i
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1

    return arr, comparisons, swaps

# -----------------------------
#   TESTING FUNCTION
# -----------------------------
def test_selection_sort(arr):
    # Keep a copy to show before/after
    unsorted_list = arr.copy()

    start = time.time()
    tracemalloc.start()

    sorted_arr, comparisons, swaps = selection_sort(arr)

    end = time.time()
    current, peak = tracemalloc.get_traced_memory()

    # Always show standard decimal format (no scientific notation)
    exec_time = format(end - start, ".6f")

    # # Print only the first few elements so output isn't massive
    # print("\nUnsorted list:", unsorted_list[:20],)
    # print("Sorted list:", sorted_arr[:20], )

    # print("Comparisons:", comparisons)
    # print("Swaps:      ", swaps)
    # print("Time:       ", exec_time, "seconds")

    metrics = {
        "sizes": len(arr),
        "comparisons": comparisons,
        "swaps": swaps,
        "recursive_calls": 0,
        "execution_time": exec_time,
        "current_memory": current,
        "peak_memory": peak
    }
    return metrics

# -----------------------------
#   EXAMPLE USAGE
# -----------------------------
if __name__ == "__main__":
    arr = [random.randint(0, 15000) for _ in range(100)]
    metrics = test_selection_sort(arr)

    import json
    print(json.dumps(metrics, indent=4))
