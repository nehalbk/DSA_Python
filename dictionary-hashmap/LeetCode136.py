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
        temp = {}
        for i in nums:
            if i in temp:
                temp[i] = temp[i] + 1
            else:
                temp[i] = 1
        for key, value in temp.items():
            if temp[key] == 1:
                return key
        return 0


if __name__ == "__main__":
    solution_instance = Solution()
    inNums = [2, 2, 1]
    result = solution_instance.singleNumber(inNums)
    print(result)

'''
Explanation:

1. Create an empty dictionary temp to store the count of each number.
2. Iterate through the input list nums:
    If a number is already in the dictionary, increment its count.
    If not, add the number to the dictionary with a count of 1.
3. Iterate through the dictionary:
    Return the first number with a count of 1.
4. If no such number is found, return 0.
'''
