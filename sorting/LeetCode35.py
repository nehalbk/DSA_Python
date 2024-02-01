"""

Problem:
35. Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return
the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104

Time Complexity:
O(log n)

Space Complexity:
O(1)

"""
from itertools import count
from typing import List

from unicodedata import decimal


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


if __name__ == "__main__":
    solution_instance = Solution()
    num = [1,3,5,6]
    target = 2
    result = solution_instance.searchInsert(num,target)
    print(result)

""""
Explanation:

This code implements the binary search algorithm to find the insertion position of a target value in a sorted list of 
integers. The goal is to return the index at which the target value should be inserted to maintain the sorted order of 
the list.

Here's the step-by-step explanation of the approach:

1. **Initialization:**
   - `left` is the starting index of the search space, initialized to 0.
   - `right` is the ending index of the search space, initialized to `len(nums) - 1`.

2. **Binary Search Loop:**
   - Use a `while` loop to continue the search until the search space is exhausted (`left > right`).
   - Inside the loop, calculate the middle index `mid` as `(left + right) // 2`.

3. **Comparison with Target:**
   - Check if the element at the middle index (`nums[mid]`) is equal to the target.
     - If yes, return `mid` as the index where the target is found.

   - If `nums[mid]` is less than the target, update `left` to `mid + 1`.
     - This means the target, if present, must be on the right side of the current middle element.

   - If `nums[mid]` is greater than the target, update `right` to `mid - 1`.
     - This means the target, if present, must be on the left side of the current middle element.

4. **Search Space Update:**
   - If the target is not found in the current iteration, the search space is updated based on whether the target is 
        greater or smaller than the middle element.
   - The search space is narrowed down to the left or right half in each iteration.

5. **Result:**
   - If the loop completes without finding the target, return the `left` index as the insertion position.
     - This is because `left` points to the position where the target should be inserted to maintain the sorted order.

The overall approach leverages the binary search technique to efficiently locate the insertion position of the target 
in the sorted list. The time complexity of this algorithm is O(log n), where n is the length of the input list `nums`.
The space complexity of the provided code is O(1), meaning it uses a constant amount of extra space regardless of the 
input size. The memory usage is constant because the algorithm only uses a fixed number of variables 
(left, right, mid, target) and does not use any data structures that scale with the input size.
"""
