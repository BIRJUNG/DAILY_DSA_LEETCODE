# 13. Roman to Integer

## 🔗 Problem

LeetCode — Roman to Integer
https://leetcode.com/problems/roman-to-integer/

---

## ⚡ Difficulty

Easy

---

## 🏷️ Topics

* String
* Hash Table

---

## 🧩 Problem Summary

Roman numerals are represented by seven symbols:

| Symbol | Value |
| ------ | ----- |
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

### Special Rule (Subtraction Case)

If a smaller value appears before a larger one, subtract it:

* IV → 4
* IX → 9
* XL → 40

---

## 💡 Key Insight

👉 If current value < next value → subtract
👉 Otherwise → add

---

## 🧠 Approach

* Use a dictionary for value lookup
* Traverse the string
* Compare current and next character:

  * If smaller → subtract
  * Else → add
* Add the last character at the end

---

## 💻 Code (Approach 1)

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_num = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100,
            'D': 500, 'M': 1000
        }

        total = 0
        n = len(s)

        for i in range(n - 1):
            if roman_num[s[i]] < roman_num[s[i + 1]]:
                total -= roman_num[s[i]]
            else:
                total += roman_num[s[i]]

        return total + roman_num[s[n - 1]]
```

---

## 💻 Code (Cleaner Version)

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        total = 0

        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]

        return total
```

---

## 🧪 Example

### Input

```
s = "MCMXCIV"
```

### Walkthrough

```
M  → +1000
C<M → -100
M  → +1000
X<C → -10
C  → +100
I<V → -1
V  → +5
```

### Output

```
1994
```

---

## ⏱️ Complexity

* Time: O(n)
* Space: O(1)

---

## ⚠️ Edge Cases

* `"I"` → 1
* `"III"` → 3
* `"IX"` → 9

---

## 🎯 Interview Takeaway

Instead of memorizing all subtraction pairs:

👉 Just compare adjacent values
👉 Reduces multiple conditions into one simple rule

---

## 🚀 Pattern

👉 Compare current element with next to decide operation

Used in:

* Sequence problems
* Greedy traversal
* Pattern-based parsing

---

## 📌 What I Learned

* Handling subtraction logic in Roman numerals
* Comparing adjacent elements efficiently
* Using hash maps for constant-time lookup

---

## 🔥 Final Thought

👉 Don’t overcomplicate with special cases
👉 One rule solves everything:

**"If current < next → subtract, else add"**
