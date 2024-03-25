"""

Problem:

442. Find All Duplicates in an Array
Solved
Medium
Topics
Companies
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears
once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.



Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
Example 2:

Input: nums = [1,1,2]
Output: [1]
Example 3:

Input: nums = [1]
Output: []


Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
Each element in nums appears once or twice.

Time Complexity:
O(n)

Space Complexity:
O(1)

"""
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            num = abs(num)
            if nums[num - 1] < 0:
                result.append(num)
            nums[num - 1] *= -1
        return result


if __name__ == "__main__":
    solution_instance = Solution()
    nums =    [4, 3, 2, 7, 8, 2, 3, 1]

    print(solution_instance.findDuplicates(nums))

""""

    
"""
