# Import the sorting algorithms
from sorting_algs.heapsort import heapSort
from sorting_algs.quicksort import quickSort_tracked
from sorting_algs.mergesort import run_merge_sort
from sorting_algs.insertion import insertion_sort, test_insertion_sort
from sorting_algs.selection import selection_sort, test_selection_sort

# Import the list generation
from list_gen import *

# Import graph helper
from plot_helper import *

# Increase recursion limit because quicksort reversed
import sys
sys.setrecursionlimit(5000)

""" Dictionary for each algorithm's metrics """
# HeapSort
heap_results = {
    "random": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [] },
    "nearly_sorted": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [] },
    "reverse": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [] },
    "heavy_duplicate": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [] },
    "empty_list": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [] },
    "single_element": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [] }
}

# QuickSort
quick_results = {
    "random": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [] },
    "nearly_sorted": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [] },
    "reverse": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [] },
    "heavy_duplicate": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [] },
    "empty_list": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [] },
    "single_element": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [] }
}

# MergeSort
merge_results = {
    "random": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [] },
    "nearly_sorted": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [] },
    "reverse": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [] },
    "heavy_duplicate": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [] },
    "empty_list": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [] },
    "single_element": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [] }
}

# InsertionSort
insertion_results = {
    "random": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [] },
    "nearly_sorted": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [] },
    "reverse": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [] },
    "heavy_duplicate": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [] },
    "empty_list": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [] },
    "single_element": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [] }
}

# SelectionSort
selection_results = {
    "random": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [] },
    "nearly_sorted": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [] },
    "reverse": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [] },
    "heavy_duplicate": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [] },
    "empty_list": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [] },
    "single_element": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [] }
}

""" Driver Program """
if __name__ == "__main__":
    # Loop 6 times, list sizes in increments of 250
    for i in range (6):

        # Create all lists
        rand_li = random_list((i + 1) * 250)
        heavy_dupe_li = heavy_duplicate_list((i + 1) * 250)
        rev_li = reverse_list((i + 1) * 250)
        near_li = nearly_sorted_list((i + 1) * 250, 2)
        empty_li = []
        single_ele_li = [5]

        """ Run all lists through all sorting algs """
        # HeapSort
        heap_metrics = {
            "random": heapSort(rand_li.copy()),
            "nearly_sorted": heapSort(near_li.copy()),
            "reverse": heapSort(rev_li.copy()),
            "heavy_duplicate": heapSort(heavy_dupe_li.copy()),
            "empty_list": heapSort(empty_li.copy()),
            "single_element": heapSort(single_ele_li.copy())
        }

        # QuickSort
        quick_metrics = {
            "random": quickSort_tracked(rand_li.copy()),
            "nearly_sorted": quickSort_tracked(near_li.copy()),
            "reverse": quickSort_tracked(rev_li.copy()),
            "heavy_duplicate": quickSort_tracked(heavy_dupe_li.copy()),
            "empty_list": quickSort_tracked(empty_li.copy()),
            "single_element": quickSort_tracked(single_ele_li.copy())
        }

        # MergeSort
        merge_metrics = {
            "random": run_merge_sort(rand_li.copy())[1],
            "nearly_sorted": run_merge_sort(near_li.copy())[1],
            "reverse": run_merge_sort(rev_li.copy())[1],
            "heavy_duplicate": run_merge_sort(heavy_dupe_li.copy())[1],
            "empty_list": run_merge_sort(empty_li.copy())[1],
            "single_element": run_merge_sort(single_ele_li.copy())[1]
        }

        # InsertionSort
        insertion_metrics = {
            "random": test_insertion_sort(rand_li.copy()),
            "nearly_sorted": test_insertion_sort(near_li.copy()),
            "reverse": test_insertion_sort(rev_li.copy()),
            "heavy_duplicate": test_insertion_sort(heavy_dupe_li.copy()),
            "empty_list": test_insertion_sort(empty_li.copy()),
            "single_element": test_insertion_sort(single_ele_li.copy())
        }

        # SelectionSort
        selection_metrics = {
            "random": test_selection_sort(rand_li.copy()),
            "nearly_sorted": test_selection_sort(near_li.copy()),
            "reverse": test_selection_sort(rev_li.copy()),
            "heavy_duplicate": test_selection_sort(heavy_dupe_li.copy()),
            "empty_list": test_selection_sort(empty_li.copy()),
            "single_element": test_selection_sort(single_ele_li.copy())
        }

        """ Push results from metrics dict to results dict """
        # HeapSort
        for key in heap_metrics:
            heap_results[key]["sizes"].append((i + 1) * 250)
            if key == "empty_list":
                heap_metrics[key]["size"] = 0
            if key == "single_element":
                heap_metrics[key]["size"] = 1
            heap_results[key]["comparisons"].append(heap_metrics[key]["comparisons"])
            heap_results[key]["swaps"].append(heap_metrics[key]["swaps"])
            heap_results[key]["recursive_calls"].append(heap_metrics[key]["recursive_calls"])
            heap_results[key]["execution_time"].append(heap_metrics[key]["execution_time"])
            heap_results[key]["current_memory"].append(heap_metrics[key]["current_memory"])
            heap_results[key]["peak_memory"].append(heap_metrics[key]["peak_memory"])

        # QuickSort
        for key in quick_metrics:
            quick_results[key]["sizes"].append((i + 1) * 250)
            if key == "empty_list":
                quick_metrics[key]["size"] = 0
            if key == "single_element":
                quick_metrics[key]["size"] = 1
            quick_results[key]["comparisons"].append(quick_metrics[key]["comparisons"])
            quick_results[key]["swaps"].append(quick_metrics[key]["swaps"])
            quick_results[key]["recursive_calls"].append(quick_metrics[key]["recursive_calls"])
            quick_results[key]["execution_time"].append(quick_metrics[key]["execution_time"])
            quick_results[key]["current_memory"].append(quick_metrics[key]["current_memory"])
            quick_results[key]["peak_memory"].append(quick_metrics[key]["peak_memory"])

        # MergeSort
        for key in merge_metrics:
            merge_results[key]["sizes"].append((i + 1) * 250)
            if key == "empty_list":
                merge_metrics[key]["size"] = 0
            if key == "single_element":
                merge_metrics[key]["size"] = 1
            merge_results[key]["comparisons"].append(merge_metrics[key]["comparisons"])
            merge_results[key]["swaps"].append(merge_metrics[key]["swaps"])
            merge_results[key]["recursive_calls"].append(merge_metrics[key]["recursive_calls"])
            merge_results[key]["execution_time"].append(merge_metrics[key]["execution_time"])
            merge_results[key]["current_memory"].append(merge_metrics[key]["current_memory"])
            merge_results[key]["peak_memory"].append(merge_metrics[key]["peak_memory"])

        # InsertionSort
        for key in insertion_metrics:
            insertion_results[key]["sizes"].append(insertion_metrics[key]["sizes"])
            insertion_results[key]["comparisons"].append(insertion_metrics[key]["comparisons"])
            insertion_results[key]["swaps"].append(insertion_metrics[key]["swaps"])
            insertion_results[key]["recursive_calls"].append(insertion_metrics[key]["recursive_calls"])
            insertion_results[key]["execution_time"].append(insertion_metrics[key]["execution_time"])
            insertion_results[key]["current_memory"].append(insertion_metrics[key]["current_memory"])
            insertion_results[key]["peak_memory"].append(insertion_metrics[key]["peak_memory"])

        # SelectionSort
        for key in selection_metrics:
            selection_results[key]["sizes"].append(selection_metrics[key]["sizes"])
            selection_results[key]["comparisons"].append(selection_metrics[key]["comparisons"])
            selection_results[key]["swaps"].append(selection_metrics[key]["swaps"])
            selection_results[key]["recursive_calls"].append(selection_metrics[key]["recursive_calls"])
            selection_results[key]["execution_time"].append(selection_metrics[key]["execution_time"])
            selection_results[key]["current_memory"].append(selection_metrics[key]["current_memory"])
            selection_results[key]["peak_memory"].append(selection_metrics[key]["peak_memory"])

    """ Graph Metrics """
    SortingMetricsGrapher(heap_results).plot_all_pages("HeapSort")
    SortingMetricsGrapher(quick_results).plot_all_pages("QuickSort")
    SortingMetricsGrapher(merge_results).plot_all_pages("MergeSort")
    SortingMetricsGrapher(insertion_results).plot_all_pages("InsertionSort")
    SortingMetricsGrapher(selection_results).plot_all_pages("SelectionSort")

    import json
    print(json.dumps(selection_results, indent=4))
    print(json.dumps(insertion_results, indent=4))
    print(json.dumps(merge_results, indent=4))
    print(json.dumps(quick_results, indent=4))
    print(json.dumps(heap_results, indent=4))