Sure! Here's the full `README.md` translated and polished in English — ready to copy and paste into your GitHub repository:

```markdown
# ABR Key Management Benchmark

This project compares three variants of **Binary Search Trees (BST)** for handling **duplicate keys**, analyzing their performance in terms of insertion and search time:

- `ABRNormal`: ignores duplicates
- `ABRFlag`: uses a boolean flag to mark duplicates
- `ABRList`: keeps a list of occurrences for each duplicated key

## Project Structure

```

├── abr\_normale.py           # Standard BST (ignores duplicates)
├── abr\_flag.py              # BST with a duplicate flag
├── abr\_lista.py             # BST storing duplicates in a list
├── benchmark.py             # Runs experiments and generates graphs
├── test\_abr.py              # Unit tests for the three implementations
├── graph\_with\_duplicates.png
├── graph\_without\_duplicates.png
└── report.pdf               # LaTeX report describing the project

````

## Requirements

Make sure you are using **Python 3.7+**. Required libraries:

- `matplotlib`
- `pandas`
- `seaborn`
- `statistics` (standard Python library)

You can install the missing packages using:

```bash
pip install matplotlib pandas seaborn
````

## How to Run

Run the benchmark script with:

```bash
python benchmark.py
```

This will automatically:

* run tests **with duplicates** (values drawn from a narrow range),
* run tests **without duplicates** (values from a wide range),
* compute average times across multiple repetitions.

The following charts will be generated:

* `graph_with_duplicates.png`
* `graph_without_duplicates.png`

## Unit Testing

To check the correctness of each implementation, run:

```bash
python test_abr.py
```

This validates insertions, searches, and duplicate handling for all three BST variants.

## 📊 Expected Output

The generated charts compare average insertion and search times across different input sizes, both **with** and **without duplicates**. In scenarios with duplicates, `Flag` and `List` variants typically show more stable and reliable behavior.

---

## Author

Lorenzo Fedi
Computer Engineering Student
University of Florence — 2025
