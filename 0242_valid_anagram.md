md
# 242. Valid Anagram

## 🔗 Problem Link
https://leetcode.com/problems/valid-anagram/

## ⚡ Difficulty
Easy

## 🏷️ Topics
String, Hash Table, Sorting

---

## 🧩 Problem Summary

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, otherwise return `false`.

An anagram means both strings contain the **same characters with the same frequency**, just possibly in a different order.

---

## 💭 My Initial Thought

My thinking was:

👉 If both strings have same characters  
👉 And same frequency of each character  
👉 Then they are anagrams  

So I tried comparing frequency first.

---

## ⚡ Approach 1 — Using Counter (Best)

### 🧠 Idea

- Count frequency of characters in both strings
- Compare both dictionaries
- If equal → anagram

---

## 💻 Code

```python
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
````

---

## 🧠 Why This Works

Example:

```text
s = "anagram"
t = "nagaram"
```

Counts:

* a: 3
* n: 1
* g: 1
* r: 1
* m: 1

Both match → ✅ True

---

## ⏱️ Time Complexity

`O(n)`

---

## 💾 Space Complexity

`O(n)`

---

## ⚡ Approach 2 — Sorting

### 🧠 Idea

* Sort both strings
* If equal → anagram

---

## 💻 Code

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
```

---

## 🧠 Why This Works

Example:

```text
s = "rat"
t = "tar"

sorted(s) = ['a','r','t']
sorted(t) = ['a','r','t']
```

👉 Both equal → True

---

## ⏱️ Time Complexity

`O(n log n)`

---

## 💾 Space Complexity

`O(n)`

---

## ⚠️ Edge Cases

### Different Length

```text
s = "a"
t = "ab"
```

Return False

---

### Same Characters Different Count

```text
s = "aacc"
t = "ccac"
```

Return False

---

### Empty Strings

```text
s = ""
t = ""
```

Return True

---

## 🎯 Interview Takeaway

This problem tests:

* frequency counting
* comparing data structures
* understanding string properties

👉 Best answer:

* Counter → O(n) (preferred)
* Sorting → simpler but slower

---

## 📌 What I Learned

* Counter is very powerful for frequency problems
* Sorting is an easy fallback solution
* Always check frequency, not just characters

---

## 🔥 Final Thought

My approach:

1. First → use Counter (clean and efficient)
2. Then → sorting (simple backup)

👉 Both valid, but Counter is optimal

---

## 🚀 Key Pattern Learned

👉 **"Compare frequency of elements instead of order"**

Used in:

* Anagram problems
* Frequency comparison problems
* Hash map problems

