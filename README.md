# Algorithm Analysis Project
## Authors:
Jack Brunswik

Kenneth Burke

Nick Constantine

Tal Grinberg

### Input data requirements
Creation of arrays - plan to use JSON organized arrays to feed into separate sorting algorithms
Requires:
- Variable input size
- Random
- Nearly sorted
- Reverse
- Duplicate heavy

### Sorting Algorithm Requirements
Sorting Algorithm must handle edge cases
- Empty Lists
- Single-Element Lists
- Large Datasets

Gathering of metrics
- Execution Time
- Number of element comparisons
- Number of swaps
- Number of recursive calls

### System Structure
```
│   README.md
│   requirements.txt
│
├───data
├───notebooks
│       alg_analysis.ipynb
│       heapsort.ipynb
│       test.ipynb
│
└───src
    │   list_gen.py
    │   main.py
    │   plot_helper.py
    │   __init__.py
    │
    ├───sorting_algs
    │   │   heapsort.py
    │   │   insertion.py
    │   │   mergesort.py
    │   │   quicksort.py
    │   │   selection.py
    │   └── __init__.py
```

### Installation and usage
```
git clone https://github.com/Baesiann/algorithm-analysis
cd algorithm-analysis
pip install -r requirements.txt
python src/main.py <num_lists> <list_size_increment>
```