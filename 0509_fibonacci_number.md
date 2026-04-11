# 509. Fibonacci Number

## 🔗 Problem Link
https://leetcode.com/problems/fibonacci-number/

##  Difficulty
Easy

##  Topics
Math, Dynamic Programming, Recursion

---

##  Problem Summary

The Fibonacci sequence is defined as:

- F(0) = 0  
- F(1) = 1  
- F(n) = F(n-1) + F(n-2)

Given an integer `n`, return the value of `F(n)`.

---

##  Intuition

👉 Follow the definition directly  
👉 Then optimize to avoid repeated work

---

##  Approach 1 — Pure Recursion

###  Idea

- Base case: if `n == 0` or `n == 1`, return `n`
- Otherwise → compute recursively

---

##  Code

```python
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)
```

---

##  Problem with This Approach

- Recomputes same values many times
- Leads to exponential growth

Example:
- `fib(5)` → `fib(4)` + `fib(3)`
- `fib(4)` → again computes `fib(3)` 

---

## ⏱️ Time Complexity

```
O(2^n)
```

---

##  Space Complexity

```
O(n)
```

(recursive stack)

---

## ⚡ Approach 2 — Iterative (Optimized)

###  Idea

👉 Keep track of last two numbers  
👉 Build result step by step

---

##  Code

```python
class Solution:
    def fib(self, n: int) -> int:
        fno = 0
        sno = 1

        for _ in range(n):
            tno = fno + sno
            fno = sno
            sno = tno

        return fno
```

---

##  Dry Run

### Input
```
n = 5
```

### Steps
```
fno = 0, sno = 1
→ 1
→ 1
→ 2
→ 3
→ 5
```

---

##  Time Complexity

```
O(n)
```

---

##  Space Complexity

```
O(1)
```

---

## ⚡ Approach 3 — Recursion + Memoization (DP)

###  Idea

👉 Store computed values  
👉 Avoid recomputation

---

##  Code

```python
from functools import cache

class Solution:
    @cache
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)
```

---

##  Why This Works

- First call → computes values
- Next calls → reuse cached results

 Converts exponential → linear

---

##  Time Complexity

```
O(n)
```

---

## 💾 Space Complexity

```
O(n)
```

(cache + recursion stack)

---

##  Edge Cases

### n = 0
```
Output: 0
```

### n = 1
```
Output: 1
```

### Small Values
```
n = 2 → 1
n = 3 → 2
```

---

##  Interview Takeaways

- Understand recursion clearly
- Identify overlapping subproblems
- Apply dynamic programming
- Optimize step-by-step

---

##  Key Pattern

 **"Overlapping subproblems → use DP"**

---

## 🔁 Related Problems

- Climbing Stairs
- House Robber
- DP Basics

---

##  Final Thoughts

Progression to remember:

1. Recursion (simple but slow)
2. Memoization (optimize)
3. Iterative (best practical solution)

---

✨ **Rule to remember:**
> If you're recomputing → cache it or iterate
