# 🧩 Daily Algorithm Patterns

A daily commitment to algorithmic problem solving — one problem per day, organized by pattern.

---

## 📌 About

This repository tracks my journey of solving algorithmic problems every day. Each solution is written in Python, tested with `unittest`, and grouped by the underlying problem-solving pattern rather than by problem source. The goal is to build deep intuition for recognizing and applying patterns across different problems.

---

## 📁 Repository Structure

```
daily-algo-patterns/
│
├── two_pointers/
│   ├── two_sum_sorted_array.py
│   ├── container_with_most_water.py
│   └── ...
│
├── sliding_window/
│   ├── max_subarray_sum.py
│   ├── longest_substring_no_repeat.py
│   └── ...
│
├── binary_search/
│   ├── search_rotated_array.py
│   └── ...
│
├── fast_slow_pointers/
│   ├── linked_list_cycle.py
│   └── ...
│
├── merge_intervals/
│   └── ...
│
├── dynamic_programming/
│   └── ...
│
└── README.md
```

---

## 🗂️ Patterns Covered

| Pattern | Description |
|---|---|
| Two Pointers | Problems solved by moving two indices toward each other or in the same direction |
| Sliding Window | Subarray/substring problems with a moving window of fixed or variable size |
| Binary Search | Search problems on sorted arrays or monotonic functions |
| Fast & Slow Pointers | Cycle detection and midpoint finding in linked lists |
| Merge Intervals | Overlapping interval problems |
| Dynamic Programming | Optimization problems with overlapping subproblems |
| BFS / DFS | Graph and tree traversal problems |
| Backtracking | Constraint satisfaction and combinatorial problems |

---

## ✅ How Each Solution Is Structured

Every file follows this consistent format:

```python
# Pattern   : Two Pointers
# Problem   : Two Sum - Sorted Array
# Leetcode Difficulty Level : Easy
# Date      : YYYY-MM-DD

def solution(args):
    # implementation
    pass

# ---------- Tests ----------
import unittest

class TestSolution(unittest.TestCase):
    def test_basic(self):
        ...
    def test_edge_cases(self):
        ...

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(unittest.TestLoader().loadTestsFromTestCase(TestSolution))
```

---

## 📅 Progress Log

| Day | Pattern | Problem | Difficulty | Date |
|---|---|---|---|---|
| Day 1 | Two Pointers | Two Sum - Sorted Array | Easy | 2026-10-03 |

---

## 🚀 Running a Solution

```bash
# Run a single file with tests
python two_pointers/two_sum_sorted_array.py

# Run tests explicitly
python -m unittest two_pointers/two_sum_sorted_array.py -v
```

---

## 🛠️ Requirements

- Python 3.8+
- No external dependencies — only Python's built-in `unittest` module

---

## 💡 Motivation

> Consistency beats intensity. One problem a day, every day, builds pattern recognition faster than grinding 10 problems in a weekend.

The focus here is not just on solving problems but on understanding *why* a pattern works, testing edge cases rigorously, and writing clean, readable code.

---

## 📬 Connect

Feel free to follow along, suggest problems, or share feedback!
