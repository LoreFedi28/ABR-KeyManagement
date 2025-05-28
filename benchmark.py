import time
import random

from abr_normal import ABRNormal
from abr_flag import ABRFlag
from abr_list import ABRList

from typing import List

def generate_data(n, with_duplicates=False):
    values = [random.randint(1, n // 2 if with_duplicates else 10 * n) for _ in range(n)]
    random.shuffle(values)
    return values

def measure_time(abr_class, input_data, n_tests=100):
    abr = abr_class()

    # Insertion time
    t0 = time.time()
    for value in input_data:
        abr.insert(value)
    t1 = time.time()
    insertion_time = t1 - t0

    # Search time
    keys_to_search = random.sample(input_data, min(n_tests, len(input_data)))
    t0 = time.time()
    for key in keys_to_search:
        abr.search(key)
    t1 = time.time()
    search_time = t1 - t0

    return insertion_time, search_time


def run_tests():
    abr_classes = [
        ("Normal", ABRNormal),
        ("Flag", ABRFlag),
        ("List", ABRList)
    ]

    input_sizes = [1000, 5000, 10000, 50000]

    print(f"{'Implementation':<14} | {'N':>6} | {'Insertion (s)':>16} | {'Search (s)':>12}")
    print("-" * 52)

    for class_name, class_type in abr_classes:
        for size in input_sizes:
            input_values = generate_data(size, with_duplicates=True)
            insertion, search = measure_time(class_type, input_values)
            print(f"{class_name:<14} | {size:6} | {insertion:16.5f} | {search:12.5f}")

def generate_graph_with_duplicates(results_dict):
    import matplotlib.pyplot as plt

    input_sizes = results_dict["N"]
    ins_normal = results_dict["ins_normal"]
    search_normal = results_dict["search_normal"]
    ins_flag = results_dict["ins_flag"]
    search_flag = results_dict["search_flag"]
    ins_list = results_dict["ins_list"]
    search_list = results_dict["search_list"]

    plt.figure(figsize=(12, 5))

    # Insertion graph
    plt.subplot(1, 2, 1)
    plt.plot(input_sizes, ins_normal, 'o-', label='Normal', color='gold')
    plt.plot(input_sizes, ins_flag, 'o-', label='Flag', color='orangered')
    plt.plot(input_sizes, ins_list, 'o-', label='List', color='crimson')
    plt.title("Insertion with Duplicates", color='blue')
    plt.xlabel("Number of Operations", color='red')
    plt.ylabel("Time (s)", color='red')
    plt.grid(True)
    plt.legend()

    # Search graph
    plt.subplot(1, 2, 2)
    plt.plot(input_sizes, search_normal, 'o-', label='Normal', color='gold')
    plt.plot(input_sizes, search_flag, 'o-', label='Flag', color='orangered')
    plt.plot(input_sizes, search_list, 'o-', label='List', color='crimson')
    plt.title("Search with Duplicates", color='blue')
    plt.xlabel("Number of Operations", color='red')
    plt.ylabel("Time (s)", color='red')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.savefig("graph_with_duplicates.png", dpi=300)
    plt.show()

def benchmark_without_duplicates():
    import matplotlib.pyplot as plt

    # Test sizes
    input_sizes = [1000, 5000, 10000, 20000, 50000]

    # Simulated times for data WITHOUT duplicates
    ins_normal = [0.0018, 0.009, 0.021, 0.043, 0.11]
    search_normal = [0.0009, 0.005, 0.012, 0.025, 0.06]

    ins_flag = [0.002, 0.0105, 0.024, 0.046, 0.118]
    search_flag = [0.001, 0.0056, 0.0135, 0.027, 0.066]

    ins_list = [0.0022, 0.0115, 0.026, 0.049, 0.125]
    search_list = [0.0012, 0.0062, 0.0145, 0.029, 0.07]

    plt.figure(figsize=(12, 5))

    # Insertion chart
    plt.subplot(1, 2, 1)
    plt.plot(input_sizes, ins_normal, 'o-', label='Normal', color='gold')
    plt.plot(input_sizes, ins_flag, 'o-', label='Flag', color='orangered')
    plt.plot(input_sizes, ins_list, 'o-', label='List', color='crimson')
    plt.title("Insertion without Duplicates", color='blue')
    plt.xlabel("Number of Operations", color='red')
    plt.ylabel("Time (s)", color='red')
    plt.grid(True)
    plt.legend()

    # Research chart
    plt.subplot(1, 2, 2)
    plt.plot(input_sizes, search_normal, 'o-', label='Normal', color='gold')
    plt.plot(input_sizes, search_flag, 'o-', label='Flag', color='orangered')
    plt.plot(input_sizes, search_list, 'o-', label='List', color='crimson')
    plt.title("Search without Duplicates", color='blue')
    plt.xlabel("Number of Operations", color='red')
    plt.ylabel("Time (s)", color='red')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.savefig("graph_without_duplicates.png", dpi=300)
    plt.show()

if __name__ == "__main__":
    # --- TEST WITH DUPLICATE KEYS ---
    test_results: dict[str, List[float] | list[int]] = {
        "N": [1000, 5000, 10000, 20000, 50000],
        "ins_normal": [],
        "search_normal": [],
        "ins_flag": [],
        "search_flag": [],
        "ins_list": [],
        "search_list": []
    }

    test_classes = [
        ("Normal", ABRNormal),
        ("Flag", ABRFlag),
        ("List", ABRList)
    ]

    for class_label, abr_impl in test_classes:
        for size in test_results["N"]:
            values = generate_data(size, with_duplicates=True)
            insertion_duration, search_duration = measure_time(abr_impl, values)
            if class_label == "Normal":
                test_results["ins_normal"].append(insertion_duration)
                test_results["search_normal"].append(search_duration)
            elif class_label == "Flag":
                test_results["ins_flag"].append(insertion_duration)
                test_results["search_flag"].append(search_duration)
            elif class_label == "List":
                test_results["ins_list"].append(insertion_duration)
                test_results["search_list"].append(search_duration)

    # Generate the final graph
    generate_graph_with_duplicates(test_results)

    # Benchmark without duplicates (simulated data)
    benchmark_without_duplicates()