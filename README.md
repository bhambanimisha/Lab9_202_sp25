# Lab 9: Graphs

Welcome to **Lab 9 on Graphs**!
This is a **3-day lab** focused on graph representations and traversal algorithms.

---

## 🔹 Day 1: Adjacency Lists

We learned in class how to represent a graph using an **adjacency list**.

* You’ve been given a PDF file containing two graphs.

* The **top graph** corresponds to `graph_1`.

* The **bottom graph** corresponds to `graph_2`.

* Implement each graph as a **Python dictionary** in `lab9_p1.py` with the format:

  ```python
  {int: list[int]}
  ```

* Keep the neighbor lists in **numerical order**.

* `graph_1` is **undirected**, and `graph_2` is **directed**.

---

## 🔹 Day 2: Breadth-First Search (BFS)

In `lab9_p2.py`, you will implement **BFS traversal** for graphs.

* Use a **Python list as a queue** (`.pop(0)` to dequeue, `.append()` to enqueue).
* Track visited nodes with a **visited list**.
* You must **tie break numerically**, visiting lower-numbered neighbors first.

**Pseudocode Reference:**

```
Create empty visited list
Create queue initialized with start node

While queue is not empty:
    Dequeue current node
    If not visited:
        Add to visited
        For each neighbor of current node (in sorted order):
            If not visited and not in queue:
                Enqueue neighbor
```

---

## 🔹 Day 3: Dijkstra's Algorithm Tests

In `lab9_p3.py`, we have given you:

* A **weighted directed graph** named `graph_3`
* A working `dijkstra(graph, start)` function

Your job in `test_3.py` is to:

* Write at least **3 meaningful unit tests**
* Use Python’s `unittest` framework


---

## ✅ Submission Checklist

Submit the following files when finished:

* `lab9_p1.py`
* `lab9_p2.py`
* `test_3.py`

