# 657. Robot Return to Origin

## 🔗 Problem Link
https://leetcode.com/problems/robot-return-to-origin/

## ⚡ Difficulty
Easy

## 🏷️ Topics
String, Counting

---

## 🧩 Problem Summary

There is a robot starting at position `(0, 0)`.

You are given a string `moves` where:
- `'U'` = move up  
- `'D'` = move down  
- `'L'` = move left  
- `'R'` = move right  

Return `True` if the robot returns to the origin `(0,0)` after all moves.

---

## 💭 My Initial Thought

My thinking was:

👉 If the robot comes back to origin  
👉 Then total `'U'` must equal `'D'`  
👉 And total `'L'` must equal `'R'`  

So instead of tracking position, I can just count moves.

---

## ⚡ Approach — Counting Moves

### 🧠 Idea

- Count how many times `'U'` and `'D'` appear
- Count how many times `'L'` and `'R'` appear
- If both pairs are equal → robot returns to origin

---

## 💻 Code

```python
moves = "UUDD"

result = moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')

print(result)
```

---

## 🧠 Why This Works

Example:

```text
moves = "UUDD"
```

Counts:

* U = 2  
* D = 2  
* L = 0  
* R = 0  

👉 Up cancels Down  
👉 Left cancels Right  

Final position = (0, 0) → ✅ True

---

## ⚠️ Important Observation

The loop is actually **not needed**.

We are recalculating the same result in every iteration.

---

## ✅ Optimized Version (Cleaner)

```python
moves = "UUDD"

result = moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')

print(result)
```

---

## ⏱️ Time Complexity

`O(n)`  
Each `.count()` scans the string

---

## 💾 Space Complexity

`O(1)`  
No extra space used

---

## ⚠️ Edge Cases

### Empty String

```text
moves = ""
```

No movement → still at origin → True

---

### Only One Direction

```text
moves = "UUU"
```

Not balanced → False

---

### Mixed Moves

```text
moves = "UDLR"
```

All cancel out → True

---

## 🎯 Interview Takeaway

This problem tests:

* logical thinking (canceling movements)
* recognizing patterns instead of simulating positions
* simplifying problems using counting

👉 You can solve this in two ways:

1. Count moves (simple and clean)  
2. Track coordinates (x, y)  

---

## 📌 What I Learned

* Sometimes counting is enough instead of simulation  
* Avoid unnecessary loops if result doesn’t change  
* Think in terms of balancing conditions  

---

## 🔥 Final Thought

My approach was:

👉 Instead of tracking position step-by-step  
👉 Just check if movements cancel each other  

This makes the solution simple and efficient.

---

## 🚀 Key Pattern Learned

👉 **"If opposite actions cancel out, compare counts instead of simulating"**

Used in:

* Movement problems  
* Balance problems  
* Frequency comparison problems  
