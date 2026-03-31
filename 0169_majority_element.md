
# 169. Majority Element

## 🔗 Problem Link
https://leetcode.com/problems/majority-element/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Hash Table, Sorting

---

## 🧩 Problem Summary

We are given an integer array `nums` of size `n`.

We need to return the element that appears **more than ⌊n / 2⌋ times**.

The problem guarantees that a majority element always exists.

---

## 💭 My Initial Thought

My first thought was simple:

👉 Count how many times each number appears  
👉 Then check which one appears more than `n // 2`

This felt like the most natural approach.

---

## 🐢 Brute Force Thinking

I didn’t directly write a nested loop solution, but conceptually:

- For each number → count its occurrences
- This would take `O(n²)`

So I avoided this and directly used a better method (dictionary).

---

## ⚡ Approach 1 — Manual Frequency Dictionary

### 🧠 Idea

- Create a dictionary
- Count frequency of each number
- Loop through dictionary and find element > `n // 2`

### 💻 Code

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}

        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        n = len(nums)

        for key, value in freq.items():
            if value > n // 2:
                return key
````

---

## ⚡ Approach 2 — Using Counter (Cleaner Version)

### 🧠 Idea

While solving, I realized:

👉 Python already has `Counter`
👉 It does the same frequency counting in one line

### 💻 Code

```python
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        n = len(nums)

        for key, value in freq.items():
            if value > n // 2:
                return key
```

---

## ⚡ Approach 3 — Sorting Trick

### 🧠 Key Insight

This was an interesting realization:

👉 If an element appears more than half the time
👉 It will always be at the middle after sorting

### 💻 Code

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]
```

---

## 🧠 Why Sorting Works

Example:

```
nums = [2,2,1,1,1,2,2]
sorted → [1,1,1,2,2,2,2]
```

Middle index = `7 // 2 = 3`

Element at index 3 = `2` → majority element

---

## ⏱️ Time Complexity

| Approach   | Time       |
| ---------- | ---------- |
| Dictionary | O(n)       |
| Counter    | O(n)       |
| Sorting    | O(n log n) |

---

## 💾 Space Complexity

| Approach   | Space                                 |
| ---------- | ------------------------------------- |
| Dictionary | O(n)                                  |
| Counter    | O(n)                                  |
| Sorting    | O(n) (Python sorted creates new list) |

---

## ⚠️ Edge Cases

### Single Element

```
[1]
```

Only one element → automatically majority

---

### All Elements Same

```
[5,5,5,5]
```

Clearly majority

---

### Majority Appears Later

```
[1,2,3,3,3]
```

Still correctly handled

---

## 🎯 Interview Takeaway

This problem tests:

* Frequency counting using hash maps
* Recognizing when `O(n²)` can be optimized to `O(n)`
* Using built-in tools like `Counter`
* Identifying patterns where sorting helps

👉 Always mention both:

* Basic solution (dictionary)
* Cleaner solution (Counter)
* Insight-based solution (sorting)

---

## 📌 What I Learned

* How to use dictionary for counting
* How `Counter` simplifies code
* Why sorting can solve frequency problems
* Comparing frequency with `n // 2`

---

## 🔥 Final Thought

My approach evolved like this:

1. First → dictionary counting (intuitive)
2. Then → Counter (cleaner)
3. Finally → sorting trick (insight-based)

👉 Same problem, multiple ways = better understanding

````
