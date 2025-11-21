import time          # Used to measure execution time of the sorting algorithm
import random        # Used to generate random test input values
import tracemalloc   # Used to track memory usage during execution (current + peak)


# ---------------------------
# Insertion Sort
# ---------------------------
class RecursiveInsertionSort:
    """
    Encapsulates the logic for recursive insertion sort
    and tracks performance metrics such as:
    - number of comparisons
    - number of swaps/shifts
    - number of recursive calls
    """

    def __init__(self):
        # Initialize counters for performance analysis
        self.comparisons = 0       # Counts every value comparison
        self.swaps = 0             # Counts every time a value is shifted
        self.recursive_calls = 0   # Counts how many times _recursive_sort() is called

    def sort(self, arr):
        """
        Public method called by external code.
        Starts the recursive sorting process.

        Parameters:
            arr (list): list of numbers to sort

        Returns:
            arr (list): the same list, now sorted
        """
        # Start recursion on full array length
        self._recursive_sort(arr, len(arr))
        return arr

    def _recursive_sort(self, arr, n):
        """
        Private method that performs the recursive insertion sort.

        This works by:
        1. Recursively sorting the sub-array arr[0 : n-1]
        2. Inserting arr[n-1] into the sorted portion

        Parameters:
            arr (list): array to sort
            n (int): number of elements currently being considered
        """

        # Count this recursive function call
        self.recursive_calls += 1

        # Base Case:
        # If n is 1 or less, the array is trivially sorted
        if n <= 1:
            return

        # Recursively sort the first n-1 elements
        # This ensures arr[0 : n-2] is sorted before insertion step
        self._recursive_sort(arr, n - 1)

        # Now insert arr[n-1] into the already-sorted first n-1 elements
        key = arr[n - 1]   # The element we need to insert
        j = n - 2          # Start comparing backward from the element before key

        # Shift elements that are greater than key one position to the right
        while j >= 0:
            # Every time we check arr[j] in a condition, it's a comparison
            self.comparisons += 1

            # If current element is greater than key, shift it right
            if arr[j] > key:
                arr[j + 1] = arr[j]   # Move arr[j] to the next position
                self.swaps += 1       # Count as a shift/swap
                j -= 1                # Move leftwards in array
            else:
                # When arr[j] <= key, correct position found — stop shifting
                break

        # Insert key into correct position after all necessary shifts
        arr[j + 1] = key


# ------------------------------------------------------------
# Runs recursive insertion sort and collects performance metrics
# ------------------------------------------------------------
def test_insertion_sort(arr):
    """
    Takes an array, performs recursive insertion sort,
    and measures performance statistics.

    Returns a dictionary with:
    - array size
    - comparisons
    - swaps
    - recursive calls
    - total execution time
    - current memory usage
    - peak memory usage
    """

    # Copy array so original is not modified
    a = arr.copy()

    # Create the sorter object that tracks metrics
    sorter = RecursiveInsertionSort()

    # Record start time BEFORE sorting
    start = time.time()

    # Start tracing memory BEFORE sorting begins
    tracemalloc.start()

    # Perform recursive insertion sort
    sorter.sort(a)

    # Stop timing AFTER sorting completes
    end = time.time()

    # Collect memory info: current usage + peak during execution
    current, peak = tracemalloc.get_traced_memory()

    # Stop tracemalloc to free resources
    tracemalloc.stop()

    # Compute readable execution time string
    exec_time = format(end - start, ".6f")

    # Return dictionary containing all collected metrics
    metrics = {
        "sizes": len(arr),
        "comparisons": sorter.comparisons,
        "swaps": sorter.swaps,
        "recursive_calls": sorter.recursive_calls,
        "execution_time": exec_time,
        "current_memory": current / 1024,   # Convert bytes → KB
        "peak_memory": peak / 1024          # Convert bytes → KB
    }
    return metrics


# ---------------------------
# Main Execution
# ---------------------------
if __name__ == "__main__":

    # Define array size for testing
    ARRAY_SIZE = 500

    # Generate 500 random integers from 0 to 50,000
    arr = [random.randint(0, 50000) for _ in range(ARRAY_SIZE)]

    # Run test and retrieve performance metrics
    metrics = test_insertion_sort(arr)

    # Print metrics as formatted JSON for readability
    import json
    print(json.dumps(metrics, indent=4))
