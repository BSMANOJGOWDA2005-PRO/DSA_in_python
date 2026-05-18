# Binary Tree

A **Binary Tree** is a hierarchical data structure in which each node can have **at most two children**.

These children are called:

- **Left Child**
- **Right Child**

It is called a **tree** because the structure looks like an upside-down tree.

---

# Structure of Binary Tree

```text
        Root
          A
         / \
        B   C
       / \   \
      D   E   F
```

---

# Terminologies

| Term | Explanation |
|---|---|
| Root Node | Top node of the tree |
| Parent Node | Node having child nodes |
| Child Node | Node connected below a parent |
| Leaf Node | Node with no children |
| Left Child | Child present on left side |
| Right Child | Child present on right side |
| Subtree | Smaller tree inside a tree |

---

# Classification of Binary Tree

## 1. Full Binary Tree

A binary tree in which every node has either:
- **0 children**, or
- **2 children**

No node has only one child.

```text
        1
       / \
      2   3
     / \
    4   5
```

---

## 2. Complete Binary Tree

A binary tree where:
- All levels are completely filled
- Last level may not be full
- Nodes are filled from left to right

```text
        1
       / \
      2   3
     / \  /
    4  5 6
```

---

## 3. Perfect Binary Tree

A binary tree where:
- All internal nodes have 2 children
- All leaf nodes are at the same level

```text
         1
       /   \
      2     3
     / \   / \
    4  5  6  7
```

---

## 4. Degenerate Binary Tree

A tree where every parent has only one child.

It behaves like a linked list.

```text
    1
     \
      2
       \
        3
         \
          4
```

---

## 5. Balanced Binary Tree

A tree where height difference between left and right subtrees is small.

This improves searching efficiency.

```text
        4
       / \
      2   6
     / \ / \
    1 3 5 7
```

---

## 6. Binary Search Tree (BST)

A special binary tree where:

- Left subtree contains smaller values
- Right subtree contains larger values

```text
        50
       /  \
     30    70
    / \    / \
   20 40  60 80
```

---

# Advantages of Binary Tree

- Fast searching and insertion
- Hierarchical data representation
- Efficient memory usage
- Used in databases and compilers

---

# Applications of Binary Tree

- Binary Search
- Expression Trees
- Heaps
- File Systems
- Databases
- Routing Tables

---

# Conclusion

A binary tree is an important non-linear data structure where each node can have at most two children. Different classifications of binary trees are used for different purposes like searching, sorting, and data organization.