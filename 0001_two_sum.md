# 1. Two Sum

## 🔗 Problem Link
https://leetcode.com/problems/two-sum/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Hash Table

---

## 🧩 Problem Summary

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

- Each input has exactly one solution
- You may not use the same element twice
- You can return the answer in any order

---

## 💭 My Initial Thought

My first thought was:

👉 For each element, find the remaining value needed to reach the target  
👉 Then check if that remaining value exists in the rest of the array  

This felt like a straightforward and natural approach.

---

## 🐢 Approach 1 — Brute Force (Slicing + Search)

### 🧠 Idea

- Loop through each index
- Compute `rem = target - nums[idx]`
- Check if `rem` exists in the remaining array (`nums[idx+1:]`)
- If yes → return indices

---

## 💻 Code

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        for idx in range(n):
            rem = target - nums[idx]

            if rem in nums[idx + 1:]:
                return [idx, idx + 1 + nums[idx + 1:].index(rem)]
```

---

## ⚠️ Problem with This Approach

* `rem in nums[idx+1:]` → takes O(n)
* `.index(rem)` → again O(n)

👉 Overall Time Complexity = **O(n²)**

This will be slow for large inputs.

---

## ⚡ Approach 2 — Hash Map (Optimal)

### 🧠 Key Insight

Instead of searching again and again:

👉 Store numbers we have already seen  
👉 Check if the required value already exists  

---

## 💻 Code

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            rem = target - num

            if rem in seen:
                return [seen[rem], i]

            seen[num] = i
```

---

## 🧠 Why This Works

Example:

```
nums = [2, 7, 11, 15]
target = 9
```

Step-by-step:

* i = 0 → num = 2 → rem = 7 → not in seen → store {2: 0}
* i = 1 → num = 7 → rem = 2 → FOUND in seen

👉 return [0, 1]

---

## ⏱️ Time Complexity

| Approach    | Time  |
| ----------- | ----- |
| Brute Force | O(n²) |
| Hash Map    | O(n)  |

---

## 💾 Space Complexity

| Approach    | Space |
| ----------- | ----- |
| Brute Force | O(1)  |
| Hash Map    | O(n)  |

---

## ⚠️ Edge Cases

### Negative Numbers

```
nums = [-3, 4, 3, 90], target = 0
```

---

### Same Number Twice

```
nums = [3, 3], target = 6
```

---

### Guaranteed Solution

The problem guarantees one solution, so no need to handle "no solution" cases.

---

## 🎯 Interview Takeaway

This problem tests:

* recognizing brute force vs optimized
* using hash maps for fast lookup
* reducing time complexity from O(n²) → O(n)

👉 Always explain both approaches:

1. Brute force (baseline thinking)
2. Hash map (optimized solution)

---

## 📌 What I Learned

* How to reduce time complexity using a dictionary
* Importance of trading space for speed
* Thinking in terms of "what value do I need?"

---

## 🔥 Final Thought

My thinking evolved like this:

1. First → check remaining array (works but slow)
2. Then → store values and check instantly using hash map

👉 This shift from searching → storing is a key DSA pattern

---

## 🚀 Key Pattern Learned

👉 **Store what you have seen, so you don’t search again**

Used in:

* Two Sum
* Subarray Sum
* Pair problems
* Frequency problems
