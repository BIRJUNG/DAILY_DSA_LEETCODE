
# 9. Palindrome Number

## 🔗 Problem Link
https://leetcode.com/problems/palindrome-number/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Math

---

## 🧩 Problem Summary

Given an integer `x`, return `true` if it is a palindrome, otherwise return `false`.

A palindrome is a number that reads the same forward and backward.

---

## 💭 My Initial Thought

My first thought was:

👉 Convert the number into a string  
👉 Reverse the string  
👉 Compare with the original

This is the simplest and fastest way to check palindrome.

---

## ⚡ Approach — String Reversal

### 🧠 Idea

- Convert integer → string
- Reverse string using slicing `[::-1]`
- Compare both

If equal → palindrome  
If not → not palindrome

---

## 💻 Code

```python
class Solution(object):
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]
````

---

## 🧠 Why This Works

Example:

```
x = 121

str(x) = "121"
reverse = "121"

Both equal → True
```

---

## ⏱️ Time Complexity

`O(n)`
(where n = number of digits)

---

## 💾 Space Complexity

`O(n)`
(because we convert number to string)

---

## ⚠️ Edge Cases

### Negative Number

```
x = -121
```

"-121" != "121-" → False

Negative numbers are NOT palindrome

---

### Single Digit

```
x = 7
```

Always palindrome

---

### Number Ending with Zero

```
x = 10
```

"10" != "01" → False

---

## 🎯 Interview Takeaway

This problem tests:

* Basic understanding of palindrome
* Ability to simplify problem using string conversion
* Clean coding

👉 BUT in interviews, follow-up may be asked:

"Can you solve it without converting to string?"

So always be ready with a math-based approach as well.

---

## 📌 What I Learned

* Python slicing `[::-1]` is very powerful
* Sometimes simple solutions are the best
* Always think: can I solve this without extra space?

---

---
