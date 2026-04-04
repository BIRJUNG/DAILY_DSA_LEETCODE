# 283. Move Zeroes

## 🔗 Problem Link
https://leetcode.com/problems/move-zeroes/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Two Pointers

---

## 🧩 Problem Summary

Given an integer array `nums`, move all `0`s to the end of the array **while maintaining the relative order of non-zero elements**.

### 📌 Constraints
- Must be done **in-place**
- Do not create a copy of the array

---

## 💭 Intuition

The key idea is:

👉 Move all non-zero elements forward  
👉 Fill the remaining positions with `0`

This ensures:
- Order of non-zero elements stays the same ✅
- All zeros shift to the end naturally ✅

---

## ⚡ Approach 1 — Two Pass (Position Pointer)

### 🧠 Idea

- Maintain a pointer `position` to place non-zero elements
- First pass → copy all non-zero elements forward
- Second pass → fill remaining indices with `0`

---

## 💻 Code

```python
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        position = 0

        # First pass: move non-zero elements forward
        for num in nums:
            if num != 0:
                nums[position] = num
                position += 1

        # Second pass: fill remaining with zeros
        while position < len(nums):
            nums[position] = 0
            position += 1
```

---

## ⚡ Approach 2 — Cleaner Two Pointer Version

### 🧠 Idea

Same logic using index-based traversal:
- Pointer `i` → position for next non-zero
- Pointer `idx` → iterate through array

---

## 💻 Code

```python
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        i = 0

        # Move non-zero elements forward
        for idx in range(n):
            if nums[idx] != 0:
                nums[i] = nums[idx]
                i += 1

        # Fill remaining positions with zero
        for idx in range(i, n):
            nums[idx] = 0
```

---

## ⚡ Approach 3 — One Pass (Optimal Swap Method)

### 🧠 Idea

- Use two pointers
- Swap non-zero elements into correct position immediately
- Avoid second loop

---

## 💻 Code

```python
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0  # position for next non-zero

        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
```

---

## 🧠 Dry Run

### Input
```
nums = [0, 1, 0, 3, 12]
```

### Step 1 (move non-zero)
```
[1, 3, 12, _, _]
```

### Step 2 (fill zeros)
```
[1, 3, 12, 0, 0]
```

---

## ⏱️ Time Complexity

```
O(n)
```

- Single traversal (or two linear passes)

---

## 💾 Space Complexity

```
O(1)
```

- In-place modification

---

## ⚠️ Edge Cases

### All Zeros
```
[0, 0, 0] → [0, 0, 0]
```

### No Zeros
```
[1, 2, 3] → [1, 2, 3]
```

### Mixed Case
```
[0, 1, 0, 3, 12] → [1, 3, 12, 0, 0]
```

---

## 🎯 Interview Takeaways

- In-place array manipulation
- Two-pointer technique
- Maintaining relative order

👉 Key Insight:
**Avoid unnecessary swaps — overwrite first, clean up later**

---

## 📌 Key Pattern

👉 **"Shift valid elements forward, then fill the rest"**

---

## 🔁 Related Problems

- Remove Element
- Partition Array
- Move Negative Numbers

---

## 🚀 Final Thoughts

Simple problem, but extremely important pattern.

---

✨ **Rule to remember:**
> Move what you want to keep → then clean the rest
