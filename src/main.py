# Import the sorting algorithms
from sorting_algs.heapsort import heapSort
from sorting_algs.quicksort import quickSort_tracked
from sorting_algs.mergesort import merge_sort
from sorting_algs.insertion import insertion_sort
from sorting_algs.selection import selection_sort

# Import the list generation
from list_gen import *

""" Dictionary for each algorithm's metrics """
# HeapSort
heap_results = {
    "random": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [] },
    "nearly_sorted": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [] },
    "reverse": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [] },
    "heavy_duplicate": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [] }
}

# QuickSort
quick_results = {
    "random": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [] },
    "nearly_sorted": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [] },
    "reverse": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [] },
    "heavy_duplicate": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [] }
}

# MergeSort

# InsertionSort

# SelectionSort

""" Driver Program """
if __name__ == "__main__":
    # Loop 6 times, list sizes in increments of 2500
    for i in range (6):

        # Create all lists
        rand_li = random_list((i + 1) * 2500)
        heavy_dupe_li = heavy_duplicate_list((i + 1) * 2500)
        rev_li = reverse_list((i + 1) * 2500)
        near_li = nearly_sorted_list((i + 1) * 2500, 2)

        """ Run all lists through all sorting algs """
        # HeapSort
        heap_metrics = {
            "random": heapSort(rand_li),
            "nearly_sorted": heapSort(near_li),
            "reverse": heapSort(rev_li),
            "heavy_duplicate": heapSort(heavy_dupe_li)
        }

        # QuickSort
        quick_metrics = {
            "random": quickSort_tracked(rand_li),
            "nearly_sorted": quickSort_tracked(near_li),
            "reverse": quickSort_tracked(rev_li),
            "heavy_duplicate": quickSort_tracked(heavy_dupe_li)
        }

        # MergeSort

        # InsertionSort

        # SelectionSort

        """ Push results from metrics dict to results dict """
        # HeapSort
        for key in heap_metrics:
            heap_results[key]["sizes"].append((i + 1) * 2500)
            heap_results[key]["comparisons"].append(heap_metrics[key]["comparisons"])
            heap_results[key]["swaps"].append(heap_metrics[key]["swaps"])
            heap_results[key]["recursive_calls"].append(heap_metrics[key]["recursive_calls"])
            heap_results[key]["execution_time"].append(heap_metrics[key]["execution_time"])

        # QuickSort

        # MergeSort

        # InsertionSort

        # SelectionSort

