````md
# 2481. Minimum Cuts to Divide a Circle

## 🔗 Problem Link
https://leetcode.com/problems/minimum-cuts-to-divide-a-circle/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Math

---

## 🧩 Problem Summary

Given an integer `n`, we need to divide a circle into `n` equal slices.

Each cut must go through the center of the circle.

Return the **minimum number of cuts** required.

---

## 💭 My Initial Thought

My thinking was:

👉 If there is only 1 slice → no cuts needed  
👉 If slices are even → we can divide efficiently using opposite cuts  
👉 If slices are odd → we need one cut per slice  

So I formed conditions based on whether `n` is even or odd.

---

## ⚡ Approach 1 — One Line Logic

### 🧠 Idea

- If `n == 1` → 0 cuts  
- If `n` is even → `n // 2` cuts  
- If `n` is odd → `n` cuts  

---

## 💻 Code

```python
class Solution:
    def numberOfCuts(self, n: int) -> int:
        return 0 if n == 1 else n // 2 if n % 2 == 0 else n
````

---

## ⚡ Approach 2 — If-Else Version

### 🧠 Idea

Same logic, just written step-by-step for clarity.

---

## 💻 Code

```python
class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n == 1:
            return 0
        elif n % 2 == 0:
            return n // 2
        else:
            return n
```

---

## 🧠 Why This Works

### Case 1: n = 1

```text
No cuts needed → 0
```

---

### Case 2: n = 4 (Even)

```text
We can cut through the center and divide into 2 parts
Then cut again → total = 2 cuts (n/2)
```

---

### Case 3: n = 3 (Odd)

```text
Each slice needs its own cut
Total cuts = 3
```

---

## ⏱️ Time Complexity

`O(1)`
Constant time — no loops

---

## 💾 Space Complexity

`O(1)`

---

## ⚠️ Edge Cases

### n = 1

```text
Output → 0
```

---

### n = 2

```text
Output → 1
```

---

### n = 3

```text
Output → 3
```

---

## 🎯 Interview Takeaway

This problem tests:

* mathematical pattern recognition
* handling edge cases
* simplifying logic using conditions

👉 Key idea:
**Even → n/2, Odd → n, Special case → n = 1**

---

## 📌 What I Learned

* Not all problems need loops — some are pure math
* Always check even vs odd patterns
* Writing compact vs readable code

---

## 🔥 Final Thought

My approach:

👉 Instead of simulating cuts
👉 I identified a pattern based on `n`

This made the solution constant time and very clean.

---

## 🚀 Key Pattern Learned

👉 **"Look for mathematical patterns instead of simulation"**

Used in:

* math problems
* optimization problems
* pattern-based questions

```
```
