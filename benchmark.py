import time
import random
import statistics
from typing import List

from abr_normal import ABRNormal
from abr_flag import ABRFlag
from abr_list import ABRList


def generate_data(n, with_duplicates=False):
    values = [random.randint(1, n // 2 if with_duplicates else 10 * n) for _ in range(n)]
    random.shuffle(values)
    return values


def measure_time(abr_class, input_data, n_repeats=5):
    insertion_times = []
    search_times = []

    for _ in range(n_repeats):
        abr = abr_class()
        t0 = time.time()
        for value in input_data:
            abr.insert(value)
        t1 = time.time()
        insertion_times.append(t1 - t0)

        keys_to_search = random.sample(input_data, max(1, len(input_data) // 5))
        t0 = time.time()
        for key in keys_to_search:
            abr.search(key)
        t1 = time.time()
        search_times.append(t1 - t0)

    return statistics.mean(insertion_times), statistics.mean(search_times)


def generate_graph(title_insert, title_search, results_dict, filename):
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
    plt.title(title_insert, color='blue')
    plt.xlabel("Numero di Operazioni", color='red')
    plt.ylabel("Tempo (s)", color='red')
    plt.grid(True)
    plt.legend()

    # Search graph
    plt.subplot(1, 2, 2)
    plt.plot(input_sizes, search_normal, 'o-', label='Normal', color='gold')
    plt.plot(input_sizes, search_flag, 'o-', label='Flag', color='orangered')
    plt.plot(input_sizes, search_list, 'o-', label='List', color='crimson')
    plt.title(title_search, color='blue')
    plt.xlabel("Numero di Operazioni", color='red')
    plt.ylabel("Tempo (s)", color='red')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.show()


if __name__ == "__main__":
    sizes = [1000, 5000, 10000, 20000, 50000]
    test_classes = [
        ("Normal", ABRNormal),
        ("Flag", ABRFlag),
        ("List", ABRList)
    ]

    # CON DUPLICATI
    results_with = {
        "N": sizes,
        "ins_normal": [], "search_normal": [],
        "ins_flag": [], "search_flag": [],
        "ins_list": [], "search_list": []
    }

    for name, cls in test_classes:
        for size in sizes:
            data = generate_data(size, with_duplicates=True)
            ins_time, search_time = measure_time(cls, data)
            results_with[f"ins_{name.lower()}"].append(ins_time)
            results_with[f"search_{name.lower()}"].append(search_time)

    # SENZA DUPLICATI
    results_without = {
        "N": sizes,
        "ins_normal": [], "search_normal": [],
        "ins_flag": [], "search_flag": [],
        "ins_list": [], "search_list": []
    }

    for name, cls in test_classes:
        for size in sizes:
            data = generate_data(size, with_duplicates=False)
            ins_time, search_time = measure_time(cls, data)
            results_without[f"ins_{name.lower()}"].append(ins_time)
            results_without[f"search_{name.lower()}"].append(search_time)

    # STAMPA RISULTATI
    print("\n--- TEMPI MEDI CON DUPLICATI ---")
    print("N\tNormal\t\tFlag\t\tList\t\t(N: Inserimento / Ricerca)")
    for i, N in enumerate(sizes):
        print(f"{N}\t{results_with['ins_normal'][i]:.4f}/{results_with['search_normal'][i]:.4f}\t"
              f"{results_with['ins_flag'][i]:.4f}/{results_with['search_flag'][i]:.4f}\t"
              f"{results_with['ins_list'][i]:.4f}/{results_with['search_list'][i]:.4f}")

    print("\n--- TEMPI MEDI SENZA DUPLICATI ---")
    for i, N in enumerate(sizes):
        print(f"{N}\t{results_without['ins_normal'][i]:.4f}/{results_without['search_normal'][i]:.4f}\t"
              f"{results_without['ins_flag'][i]:.4f}/{results_without['search_flag'][i]:.4f}\t"
              f"{results_without['ins_list'][i]:.4f}/{results_without['search_list'][i]:.4f}")

    # GENERAZIONE GRAFICI
    generate_graph(
        "Inserimento con Duplicati", "Ricerca con Duplicati",
        results_with, "graph_with_duplicates.png"
    )

    generate_graph(
        "Inserimento senza Duplicati", "Ricerca senza Duplicati",
        results_without, "graph_without_duplicates_measured.png"
    )