"""

Problem:
136. Single Number

Link:
https://leetcode.com/problems/single-number/description/

Description:
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example:

Example 1:

Input: nums = [2,2,1]
Output: 1

Example 2:

Input: nums = [4,1,2,1,2]
Output: 4

Example 3:

Input: nums = [1]
Output: 1

Constraints:
1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.

Time Complexity:
O(n)

Space Complexity:
O(k)

"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res ^= i
        return res


if __name__ == "__main__":
    solution_instance = Solution()
    inNums = [2, 2, 1]
    result = solution_instance.singleNumber(inNums)
    print(result)

'''
Explanation:

1. Initialize result to 0.
2. Iterate through each element in nums:
    First iteration: result ^ 4 (0 XOR 4) → result = 4
    Second iteration: result ^ 2 (4 XOR 2) → result = 6
    Third iteration: result ^ 1 (6 XOR 1) → result = 7
    Fourth iteration: result ^ 2 (7 XOR 2) → result = 5
    Fifth iteration: result ^ 1 (5 XOR 1) → result = 4
3. After the loop, result contains the non-duplicated element, which is 4 in this example.

Why it works:

The XOR operation is associative and commutative, meaning the order of XOR operations doesn't matter.
XORing a number with itself results in 0.
XORing a number with 0 gives the number itself.
When you XOR all elements in the array, the duplicates cancel each other out, and the only remaining element is the non-duplicated one.

This solution has a linear runtime complexity of O(n) since it iterates through the array once, and it uses only constant extra space
'''
