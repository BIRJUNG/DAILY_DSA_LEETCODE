# 🔍 28. Find the Index of the First Occurrence in a String

## 🔗 Problem Link
[LeetCode Problem](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

---

## ⚡ Difficulty
**Easy**

## 🏷️ Topics
- String  
- Two Pointers  

---

## 🧩 Problem Summary

Given two strings:

- `haystack` → main string  
- `needle` → substring  

Return the **index of the first occurrence** of `needle` in `haystack`.

If `needle` is not found → return `-1`.

---

## 💭 Initial Thought Process

My approach:

- Check if `needle` exists in `haystack`
- If yes, find where it starts

Used **string slicing** to compare substrings.

---

## ⚡ Approach 1 — Sliding Window (Manual)

### 🧠 Idea

- Traverse `haystack`
- Extract substring of length `needle`
- Compare with `needle`
- Return index if match is found

---

### 💻 Code

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1

        n = len(haystack)
        m = len(needle)

        for i in range(n):
            if haystack[i:i+m] == needle:
                return i
```

---

## ⚠️ Observation

The check:

```python
if needle not in haystack:
```

is **optional** because:

- If no match is found, loop naturally ends
- We can return `-1` afterward

---

## ⚡ Improved Version (Optimized Loop)

### ✅ Key Improvement
Limit loop range to avoid unnecessary checks.

---

### 💻 Code

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        for i in range(n - m + 1):
            if haystack[i:i+m] == needle:
                return i

        return -1
```

---

## ⚡ Approach 2 — Built-in Function

### 🧠 Idea

Python provides:

- `str.find()` → returns index of first match  
- Returns `-1` if not found  

---

### 💻 Code

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
```

---

## 🧠 Example

```text
haystack = "sadbutsad"
needle = "sad"
```

**Output:** `0`  
(First occurrence starts at index 0)

---

## ⏱️ Time Complexity

| Approach   | Complexity |
|-----------|-----------|
| Manual     | O(n × m)  |
| Built-in   | O(n)      |

---

## 💾 Space Complexity

**O(1)**

---

## ⚠️ Edge Cases

### ❌ Needle Not Present
```text
haystack = "hello"
needle = "world"
```
Output → `-1`

---

### ⚠️ Empty Needle
```text
haystack = "abc"
needle = ""
```
Output → `0` (by definition)

---

### ✅ Same String
```text
haystack = "abc"
needle = "abc"
```
Output → `0`

---

## 🎯 Interview Takeaways

This problem tests:

- String traversal  
- Substring comparison  
- Sliding window technique  

👉 Best practice:
1. Explain manual approach first  
2. Then mention built-in optimization  

---

## 📌 Key Learnings

- Substring matching using slicing  
- Importance of `n - m + 1` boundary  
- Built-in methods can simplify code  

---

## 🚀 Final Thought

Approach evolution:

1. Start with brute-force (manual check)  
2. Optimize loop bounds  
3. Use built-in functions when appropriate  

---

## 🔥 Key Pattern

👉 **Sliding Window on Strings**

Used in:

- Substring search  
- Pattern matching  
- Text processing  
