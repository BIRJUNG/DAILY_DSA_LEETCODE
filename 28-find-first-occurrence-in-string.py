````md
# 28. Find the Index of the First Occurrence in a String

## 🔗 Problem Link
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

## ⚡ Difficulty
Easy

## 🏷️ Topics
String, Two Pointers

---

## 🧩 Problem Summary

Given two strings:

- `haystack` → main string  
- `needle` → substring  

Return the **index of the first occurrence** of `needle` in `haystack`.

If `needle` is not found → return `-1`.

---

## 💭 My Initial Thought

My thinking was:

👉 Check if `needle` exists in `haystack`  
👉 If yes, then find where it starts  

So I used slicing to compare parts of the string.

---

## ⚡ Approach 1 — Manual Sliding Window

### 🧠 Idea

- Loop through `haystack`
- Take substring of length `needle`
- Compare with `needle`
- If match → return index

---

## 💻 Code

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
````

---

## ⚠️ Observation

👉 The check `if needle not in haystack` is optional

Because:

* If no match is found, loop will automatically end
* And function can return `-1`

---

## ⚡ Improved Version (Cleaner)

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

Python already provides a direct method:

👉 `find()` returns the index
👉 Returns `-1` if not found

---

## 💻 Code

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
```

---

## 🧠 Why This Works

Example:

```text
haystack = "sadbutsad"
needle = "sad"
```

* First occurrence starts at index `0`

---

## ⏱️ Time Complexity

| Approach | Time                        |
| -------- | --------------------------- |
| Manual   | O(n * m)                    |
| Built-in | O(n) (optimized internally) |

---

## 💾 Space Complexity

`O(1)`

---

## ⚠️ Edge Cases

### Needle Not Present

```text
haystack = "hello"
needle = "world"
```

Output → `-1`

---

### Empty Needle

```text
haystack = "abc"
needle = ""
```

Output → `0` (by definition)

---

### Same String

```text
haystack = "abc"
needle = "abc"
```

Output → `0`

---

## 🎯 Interview Takeaway

This problem tests:

* string traversal
* substring comparison
* sliding window idea

👉 Important:

* Always mention manual approach first
* Then mention built-in optimization

---

## 📌 What I Learned

* How substring matching works
* Importance of limiting loop to `n - m + 1`
* Built-in functions can simplify solutions

---

## 🔥 Final Thought

My thinking:

1. First → check substring manually
2. Then → optimize loop range
3. Finally → use built-in `.find()`

👉 Always good to know both manual and built-in solutions

---

## 🚀 Key Pattern Learned

👉 **"Sliding window on strings for substring matching"**

Used in:

* String search problems
* Pattern matching
* Text processing

```
```
