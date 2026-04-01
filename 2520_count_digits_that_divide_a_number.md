
# 🔢 2520. Count the Digits That Divide a Number

🔗 Problem Link: https://leetcode.com/problems/count-the-digits-that-divide-a-number/  
⚡ Difficulty: Easy  
🏷️ Topics: Math  

---

## 🧩 Problem Summary

Given an integer `num`, return the number of digits in `num` that divide `num`.

A digit `d` divides `num` if:

```
num % d == 0
```

⚠️ Each digit should be checked individually.

---

## 💭 My Initial Thought

- Convert the number to a string
- Loop through each digit
- Convert it back to integer
- Check if it divides the original number

---

## 🐢 Brute Force Approach (String Conversion)

### 💡 Idea
- Convert number to string
- Iterate each character
- Convert back to integer and check divisibility

### 💻 Code

```python
class Solution:
    def countDigits(self, num: int) -> int:
        ans = 0
        org = num
        
        for v in str(num):
            if org % int(v) == 0:
                ans += 1
                
        return ans
```

---

## ⚡ Optimized Approach (Math / Modulo)

### 💡 Idea
- Extract digits using `% 10`
- Remove last digit using `// 10`
- Avoid string conversion → more efficient

### 💻 Code

```python
class Solution:
    def countDigits(self, num: int) -> int:
        ans = 0
        org = num
        
        while num != 0:
            digit = num % 10
            
            if org % digit == 0:
                ans += 1
                
            num //= 10
            
        return ans
```

---

## ⏱️ Time Complexity

- Both approaches: **O(d)**  
  where `d = number of digits`

---

## 💾 Space Complexity

- String approach: **O(d)** (extra space for string)
- Math approach: **O(1)** (no extra space)

---

## ⚠️ Edge Cases

- `num` contains digit `0` → division by zero error  
  (Given constraints usually avoid this, but good to remember)

- Single digit number → always divides itself

---

## 🎯 Interview Takeaway

- Prefer **math-based digit extraction** over string conversion
- Pattern:  
  👉 “Process digits of a number” → use `% 10` and `// 10`

---

## 📌 What I Learned

- Two ways to iterate digits:
  - String conversion (easy)
  - Modulo method (better)
- Always keep original number safe (`org`)
- Recognized a common pattern for digit problems

---

## 🔁 Pattern Recognition

This problem is part of:

- Digit extraction problems
- Math-based iteration
- Basic modulo logic

---

## 🚀 Final Thought

Simple problem, but important for:

- building number manipulation skills
- reinforcing `%` and `//` usage
- recognizing reusable patterns in DSA
