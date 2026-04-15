# 53. Maximum Subarray

##  Problem Link
https://leetcode.com/problems/maximum-subarray/

##  Difficulty
Medium

## 🏷️ Topics
Array, Dynamic Programming

---

## 🧩 Problem Summary

Given an integer array `nums`, find the subarray with the largest sum and return that sum.

---

##  My Approach (Kadane’s Algorithm)

- Traverse the array while maintaining a running sum (`cur_sum`)
- If the running sum becomes negative, reset it to 0
- Keep track of the maximum sum seen so far

---

## Code

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -float('inf')
        cur_sum = 0

        for val in nums:
            cur_sum += val
            if cur_sum > max_sum:
                max_sum = cur_sum
            if cur_sum < 0:
                cur_sum = 0

        return max_sum
```

---

##  Why This Works

- Negative sum will only reduce future results → reset it
- Always keep track of the best (maximum) sum
- Efficient and optimal solution

---

## ⏱️ Time Complexity

`O(n)` — Single pass through the array

---

## 💾 Space Complexity

`O(1)` — Constant space

---

## 🎯 Key Takeaway

👉 **Drop negative sums, keep building positive streaks**

---

## 🚀 What I Learned

- How to optimize subarray problems using Kadane’s Algorithm
- Importance of handling negative values efficiently
