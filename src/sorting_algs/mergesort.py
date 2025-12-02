import time
import tracemalloc

# merge two lists
def merge(left, right, m):
    res = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        m["comparisons"] += 1

        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    # leftovers
    res.extend(left[i:])
    res.extend(right[j:])
    return res

# merge sort recursion
def merge_sort(arr, m):
    m["recursive_calls"] += 1

    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = merge_sort(arr[:mid], m)
    right = merge_sort(arr[mid:], m)

    return merge(left, right, m)

# tracks metrics + timing
def run_merge_sort(arr):
    m = {
        "unsorted_list": arr.copy(),
        "sorted_list": [],
        "sizes": len(arr),
        "comparisons": 0,
        "swaps": 0,   # merge sort never swaps, included to match group style
        "recursive_calls": 0,
        "execution_time": 0,
        "current_memory": 0,
        "peak_memory": 0
    }

    tracemalloc.start() # Start mem-use tracker
    start = time.perf_counter()
    out = merge_sort(arr, m)
    # Store the sorted list
    m["sorted_list"] = out.copy()
    m["execution_time"] = time.perf_counter() - start
    current, peak = tracemalloc.get_traced_memory()
    m["current_memory"] = current / 1024
    m["peak_memory"] = peak / 1024
    tracemalloc.stop() # End mem-use tracker

    return out, m

# prints metrics
def print_metrics(m):
    print("Comparisons:", m["comparisons"])
    print("Swaps:", m["swaps"])
    print("Recursive calls:", m["recursive_calls"])
    print(f"Execution time: {m['execution_time']:.8f} seconds")

if __name__ == "__main__":
    # arr = [33, 12, 77, 5, 29, 41, 8, 64, 19, 2]  # Random list
    # arr = [1, 2, 3, 4, 6, 5, 7, 8, 10, 9]  # Nearly sorted list
    # arr = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2]  # Reverse sorted list
    # arr = [4, 4, 4, 3, 3, 7, 7, 7, 3, 4]  # Heavy duplicate list

    # Default quick check
    # arr = [12, 7, 25, 3, 18, 9, 31, 4, 22, 15, 1, 28]
    import random
    arr = [random.randint(0, 15000) for _ in range(100)]

    # Run Merge Sort

    print("Unsorted:", arr)
    sorted_arr, m = run_merge_sort(arr)
    print("Sorted:", sorted_arr)
    print_metrics(m)
    import json
    print(json.dumps(m, indent=4))


    # Uncomment to test large dataset of size n

    # size = 15000
    # arr = [random.randint(0, 15000) for _ in range(size)]
    # sorted_arr, metrics = run_merge_sort(arr)
    # print("Comparisons:", metrics["comparisons"])
    # print("Swaps:", metrics["swaps"])
    # print("Recursive calls:", metrics["recursive_calls"])
    # print(f"Execution time: {metrics['execution_time']:.8f} seconds")
