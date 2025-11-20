import matplotlib.pyplot as plt

class SortingMetricsGrapher:
    def __init__(self, results, list_types=None):
        """
        results: dictionary of list types -> metric arrays
        list_types: readable names for legend labels
        """
        self.results = results
        self.list_types = list_types or {
            "random": "Random",
            "nearly_sorted": "Nearly Sorted",
            "reverse": "Reverse",
            "heavy_duplicate": "Heavy Duplicates"
            "empty_list": "Empty List",
            "single_element": "Single Element"
        }

    def plot_algorithm_page(self, algorithm_name):
        """
        Generates ONE PAGE (one figure) for ONE algorithm.
        6 metrics in a 2x3 layout.
        """
        metrics_to_plot = [
            ("comparisons", "Comparisons"),
            ("swaps", "Swaps"),
            ("recursive_calls", "Recursive Calls"),
            ("execution_time", "Execution Time (s)"),
            ("current_memory", "Current Memory (KB)"),
            ("peak_memory", "Peak Memory (KB)")
        ]

        fig, axes = plt.subplots(2, 3, figsize=(18, 10))
        axes = axes.flatten()

        for ax, (metric_name, readable) in zip(axes, metrics_to_plot):
            for key, label in self.list_types.items():
                ax.plot(
                    self.results[key]["sizes"],
                    self.results[key][metric_name],
                    marker="o",
                    linestyle="--",
                    label=label
                )
            ax.set_title(readable)
            ax.set_xlabel("List Size")
            ax.set_ylabel(readable)
            ax.grid(True)

        # Only add one legend for the whole page
        handles, labels = axes[0].get_legend_handles_labels()
        fig.legend(handles, labels, loc="upper left", ncol=4)

        fig.suptitle(f"{algorithm_name} Metrics Overview", fontsize=18)
        fig.tight_layout(rect=[0, 0, 1, 0.95])
        plt.show()

    def plot_all_pages(self, algorithm_name):
        self.plot_algorithm_page(algorithm_name)
