"""

Problem:

41. First Missing Positive
Hard
Topics
Companies
Hint
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.



Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.


Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1

Time Complexity:
O(n)

Space Complexity:
O(1)

"""
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i]<=0 or nums[i]> len(nums):
                nums[i] =len(nums)+1
        for i in range(len(nums)):
            if abs(nums[i]) > 0 and abs(nums[i]) <(len(nums)+1):
                nums[abs(nums[i])-1] =-abs(nums[abs(nums[i])-1])
        for i in range(len(nums)):
            if nums[i] >= 0 :
                return i +1
        return len(nums)+1


if __name__ == "__main__":
    solution_instance = Solution()
    nums= [1,1]

    print(solution_instance.firstMissingPositive(nums))

""""

"""
