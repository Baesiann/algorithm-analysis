import time          # Used for measuring execution time
import random        # Used for generating random test data
import tracemalloc   # Used for tracking memory usage (current + peak)


# ------------------------------------------
#   Selection sort
# ------------------------------------------
def find_min_index(arr, left, right, counters):
    """
    Recursively returns the index of the smallest element
    in arr[left:right+1].
    """

    # Base case: if the range has only one element, it is the minimum
    if left == right:
        return left

    # Count every recursive comparison
    counters["comparisons"] += 1

    # Recursively find the minimum index from left to right-1
    min_idx = find_min_index(arr, left, right - 1, counters)

    # Compare arr[right] to the current minimum found
    # Return index of the smaller element
    return right if arr[right] < arr[min_idx] else min_idx


# ------------------------------------------
#   Recursive Selection Sort
# ------------------------------------------
def recursive_selection_sort(arr, start, counters):
    """
    Recursively sorts the array using the Selection Sort method.
    """

    n = len(arr)  # Total number of elements in array

    # Base case: when start reaches second-last index, array is sorted
    if start >= n - 1:
        return

    # Count how many times this recursive function is called
    counters["recursive_calls"] += 1

    # Find index of smallest element between start and end of array
    min_index = find_min_index(arr, start, n - 1, counters)

    # Swap smallest element into correct position
    if min_index != start:
        arr[start], arr[min_index] = arr[min_index], arr[start]
        counters["swaps"] += 1  # Track number of swaps performed

    # Recurse on the rest of the array (start+1 to end)
    recursive_selection_sort(arr, start + 1, counters)


# ------------------------------------------
#   Wrapper for Selection Sort
# ------------------------------------------
def selection_sort(arr):
    # Initialize counters for metrics
    counters = {
        "comparisons": 0,
        "swaps": 0,
        "recursive_calls": 0
    }

    # Perform recursive selection sort
    recursive_selection_sort(arr, 0, counters)

    # Return sorted array and metrics
    return arr, counters


# ------------------------------------------
#   Test & Metrics Collection
# ------------------------------------------
def test_selection_sort(arr):
    tracemalloc.start()           # Start memory tracking
    start_time = time.time()      # Record time before sorting

    # Perform sort and get metrics
    sorted_arr, counters = selection_sort(arr)

    end_time = time.time()        # Record time after sorting

    # Get memory snapshot (current usage, peak usage)
    current, peak = tracemalloc.get_traced_memory()

    # Return performance metrics in a dictionary
    metrics = {
        "unsorted_list": arr.copy(),
        "sorted_list": sorted_arr.copy(),
        "sizes": len(arr),
        "comparisons": counters["comparisons"],
        "swaps": counters["swaps"],
        "recursive_calls": counters["recursive_calls"],
        "execution_time": round(end_time - start_time, 6),
        "current_memory": round(current / 1024, 4),
        "peak_memory": round(peak / 1024, 4)
    }
    return arr, metrics


# ------------------------------------------
#   Main Execution
# ------------------------------------------
if __name__ == "__main__":

    # Generate a list of 100 random integers between 0 and 15000
    arr = [random.randint(0, 15000) for _ in range(100)]

    import json  # Used to print results in readable JSON format

    # Run test and print metrics nicely formatted
    print(json.dumps(test_selection_sort(arr), indent=4))
