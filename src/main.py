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
    "random": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [], "sorted_list": [], "unsorted_list": [] },
    "nearly_sorted": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [], "sorted_list": [], "unsorted_list": [] },
    "reverse": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [], "sorted_list": [], "unsorted_list": [] },
    "heavy_duplicate": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [], "sorted_list": [], "unsorted_list": [] },
    "empty_list": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [], "sorted_list": [], "unsorted_list": [] },
    "single_element": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [], "sorted_list": [], "unsorted_list": [] }
}

# QuickSort
quick_results = {
    "random": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [], "sorted_list": [], "unsorted_list": [] },
    "nearly_sorted": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [], "sorted_list": [], "unsorted_list": [] },
    "reverse": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [], "sorted_list": [], "unsorted_list": [] },
    "heavy_duplicate": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [], "sorted_list": [], "unsorted_list": [] },
    "empty_list": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [], "sorted_list": [], "unsorted_list": [] },
    "single_element": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [], "sorted_list": [], "unsorted_list": [] }
}

# MergeSort
merge_results = {
    "random": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [], "sorted_list": [], "unsorted_list": [] },
    "nearly_sorted": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [], "sorted_list": [], "unsorted_list": [] },
    "reverse": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [], "sorted_list": [], "unsorted_list": [] },
    "heavy_duplicate": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [], "sorted_list": [], "unsorted_list": [] },
    "empty_list": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [], "sorted_list": [], "unsorted_list": [] },
    "single_element": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [], "sorted_list": [], "unsorted_list": [] }
}

# InsertionSort
insertion_results = {
    "random": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [], "sorted_list": [], "unsorted_list": [] },
    "nearly_sorted": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [], "sorted_list": [], "unsorted_list": [] },
    "reverse": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [], "sorted_list": [], "unsorted_list": [] },
    "heavy_duplicate": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [], "sorted_list": [], "unsorted_list": [] },
    "empty_list": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [], "sorted_list": [], "unsorted_list": [] },
    "single_element": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [], "sorted_list": [], "unsorted_list": [] }
}

# SelectionSort
selection_results = {
    "random": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [], "sorted_list": [], "unsorted_list": [] },
    "nearly_sorted": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [], "sorted_list": [], "unsorted_list": [] },
    "reverse": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [], "sorted_list": [], "unsorted_list": [] },
    "heavy_duplicate": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [], "sorted_list": [], "unsorted_list": [] },
    "empty_list": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [], "sorted_list": [], "unsorted_list": [] },
    "single_element": { "sizes": [], "comparisons": [], "swaps": [], "recursive_calls": [], "execution_time": [], "current_memory": [], "peak_memory": [], "sorted_list": [], "unsorted_list": [] }
}

""" Driver Program """
if __name__ == "__main__":
    # Parse args
    if len(sys.argv) < 3:
        print("Usage: python src/main.py <num_lists> <list_size_increment>")
        sys.exit(1)

    num_lists = int(sys.argv[1])
    list_size_increment = int(sys.argv[2])

    # Loop num_lists times, list sizes in increments of list_size_increment
    for i in range (num_lists):

        # Create all lists
        rand_li = random_list((i + 1) * list_size_increment)
        heavy_dupe_li = heavy_duplicate_list((i + 1) * list_size_increment)
        rev_li = reverse_list((i + 1) * list_size_increment)
        near_li = nearly_sorted_list((i + 1) * list_size_increment, 2)
        empty_li = []
        single_ele_li = [5]

        """ Run all lists through all sorting algs """
        # HeapSort
        heap_metrics = {
            "random": heapSort(rand_li.copy())[1],
            "nearly_sorted": heapSort(near_li.copy())[1],
            "reverse": heapSort(rev_li.copy())[1],
            "heavy_duplicate": heapSort(heavy_dupe_li.copy())[1],
            "empty_list": heapSort(empty_li.copy())[1],
            "single_element": heapSort(single_ele_li.copy())[1]
        }

        # QuickSort
        quick_metrics = {
            "random": quickSort_tracked(rand_li.copy())[1],
            "nearly_sorted": quickSort_tracked(near_li.copy())[1],
            "reverse": quickSort_tracked(rev_li.copy())[1],
            "heavy_duplicate": quickSort_tracked(heavy_dupe_li.copy())[1],
            "empty_list": quickSort_tracked(empty_li.copy())[1],
            "single_element": quickSort_tracked(single_ele_li.copy())[1]
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
            "random": test_insertion_sort(rand_li.copy())[1],
            "nearly_sorted": test_insertion_sort(near_li.copy())[1],
            "reverse": test_insertion_sort(rev_li.copy())[1],
            "heavy_duplicate": test_insertion_sort(heavy_dupe_li.copy())[1],
            "empty_list": test_insertion_sort(empty_li.copy())[1],
            "single_element": test_insertion_sort(single_ele_li.copy())[1]
        }

        # SelectionSort
        selection_metrics = {
            "random": test_selection_sort(rand_li.copy())[1],
            "nearly_sorted": test_selection_sort(near_li.copy())[1],
            "reverse": test_selection_sort(rev_li.copy())[1],
            "heavy_duplicate": test_selection_sort(heavy_dupe_li.copy())[1],
            "empty_list": test_selection_sort(empty_li.copy())[1],
            "single_element": test_selection_sort(single_ele_li.copy())[1]
        }

        """ Push results from metrics dict to results dict """
        # HeapSort
        for key in heap_metrics:
            heap_results[key]["sizes"].append(heap_metrics[key]["sizes"])
            heap_results[key]["comparisons"].append(heap_metrics[key]["comparisons"])
            heap_results[key]["swaps"].append(heap_metrics[key]["swaps"])
            heap_results[key]["recursive_calls"].append(heap_metrics[key]["recursive_calls"])
            heap_results[key]["execution_time"].append(heap_metrics[key]["execution_time"])
            heap_results[key]["current_memory"].append(heap_metrics[key]["current_memory"])
            heap_results[key]["peak_memory"].append(heap_metrics[key]["peak_memory"])
            heap_results[key]["unsorted_list"] = heap_metrics[key]["unsorted_list"]
            heap_results[key]["sorted_list"] = heap_metrics[key]["sorted_list"]

        # QuickSort
        for key in quick_metrics:
            quick_results[key]["sizes"].append(quick_metrics[key]["sizes"])
            quick_results[key]["comparisons"].append(quick_metrics[key]["comparisons"])
            quick_results[key]["swaps"].append(quick_metrics[key]["swaps"])
            quick_results[key]["recursive_calls"].append(quick_metrics[key]["recursive_calls"])
            quick_results[key]["execution_time"].append(quick_metrics[key]["execution_time"])
            quick_results[key]["current_memory"].append(quick_metrics[key]["current_memory"])
            quick_results[key]["peak_memory"].append(quick_metrics[key]["peak_memory"])
            quick_results[key]["unsorted_list"] = quick_metrics[key]["unsorted_list"]
            quick_results[key]["sorted_list"] = quick_metrics[key]["sorted_list"]

        # MergeSort
        for key in merge_metrics:
            merge_results[key]["sizes"].append(merge_metrics[key]["sizes"])
            merge_results[key]["comparisons"].append(merge_metrics[key]["comparisons"])
            merge_results[key]["swaps"].append(merge_metrics[key]["swaps"])
            merge_results[key]["recursive_calls"].append(merge_metrics[key]["recursive_calls"])
            merge_results[key]["execution_time"].append(merge_metrics[key]["execution_time"])
            merge_results[key]["current_memory"].append(merge_metrics[key]["current_memory"])
            merge_results[key]["peak_memory"].append(merge_metrics[key]["peak_memory"])
            merge_results[key]["unsorted_list"] = merge_metrics[key]["unsorted_list"]
            merge_results[key]["sorted_list"] = merge_metrics[key]["sorted_list"]

        # InsertionSort
        for key in insertion_metrics:
            insertion_results[key]["sizes"].append(insertion_metrics[key]["sizes"])
            insertion_results[key]["comparisons"].append(insertion_metrics[key]["comparisons"])
            insertion_results[key]["swaps"].append(insertion_metrics[key]["swaps"])
            insertion_results[key]["recursive_calls"].append(insertion_metrics[key]["recursive_calls"])
            insertion_results[key]["execution_time"].append(insertion_metrics[key]["execution_time"])
            insertion_results[key]["current_memory"].append(insertion_metrics[key]["current_memory"])
            insertion_results[key]["peak_memory"].append(insertion_metrics[key]["peak_memory"])
            insertion_results[key]["unsorted_list"] = insertion_metrics[key]["unsorted_list"]
            insertion_results[key]["sorted_list"] = insertion_metrics[key]["sorted_list"]

        # SelectionSort
        for key in selection_metrics:
            selection_results[key]["sizes"].append(selection_metrics[key]["sizes"])
            selection_results[key]["comparisons"].append(selection_metrics[key]["comparisons"])
            selection_results[key]["swaps"].append(selection_metrics[key]["swaps"])
            selection_results[key]["recursive_calls"].append(selection_metrics[key]["recursive_calls"])
            selection_results[key]["execution_time"].append(selection_metrics[key]["execution_time"])
            selection_results[key]["current_memory"].append(selection_metrics[key]["current_memory"])
            selection_results[key]["peak_memory"].append(selection_metrics[key]["peak_memory"])
            selection_results[key]["unsorted_list"] = selection_metrics[key]["unsorted_list"]
            selection_results[key]["sorted_list"] = selection_metrics[key]["sorted_list"]

    """ Graph Metrics """
    SortingMetricsGrapher(heap_results).plot_all_pages("HeapSort")
    SortingMetricsGrapher(quick_results).plot_all_pages("QuickSort")
    SortingMetricsGrapher(merge_results).plot_all_pages("MergeSort")
    SortingMetricsGrapher(insertion_results).plot_all_pages("InsertionSort")
    SortingMetricsGrapher(selection_results).plot_all_pages("SelectionSort")

    import json
    # print(json.dumps(selection_results, indent=4))
    # print(json.dumps(insertion_results, indent=4))
    # print(json.dumps(merge_results, indent=4))
    # print(json.dumps(quick_results, indent=4))
    # print(json.dumps(heap_results, indent=4))

    # Print all the unsorted and sorted lists for each algorithm

    print(f"\nFirst 10 elements of last unsorted and sorted lists for HeapSort:\n")

    for key in heap_results:
        print(f"HeapSort - {key} unsorted:", heap_results[key]["unsorted_list"][:10])
        print(f"HeapSort - {key} sorted:", heap_results[key]["sorted_list"][:10])

    print(f"\n\nFirst 10 elements of last unsorted and sorted lists for QuickSort:\n")
    for key in quick_results:
        print(f"QuickSort - {key} unsorted:", quick_results[key]["unsorted_list"][:10])
        print(f"QuickSort - {key} sorted:", quick_results[key]["sorted_list"][:10])

    print(f"\n\nFirst 10 elements of last unsorted and sorted lists for MergeSort:\n")
    for key in merge_results:
        print(f"MergeSort - {key} unsorted:", merge_results[key]["unsorted_list"][:10])
        print(f"MergeSort - {key} sorted:", merge_results[key]["sorted_list"][:10])

    print(f"\n\nFirst 10 elements of last unsorted and sorted lists for InsertionSort:\n")
    for key in insertion_results:
        print(f"InsertionSort - {key} unsorted:", insertion_results[key]["unsorted_list"][:10])
        print(f"InsertionSort - {key} sorted:", insertion_results[key]["sorted_list"][:10])

    print(f"\n\nFirst 10 elements of last unsorted and sorted lists for SelectionSort:\n")
    for key in selection_results:
        print(f"SelectionSort - {key} unsorted:", selection_results[key]["unsorted_list"][:10])
        print(f"SelectionSort - {key} sorted:", selection_results[key]["sorted_list"][:10])