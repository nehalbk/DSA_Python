"""

Problem:

1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

Time Complexity:
O(n)

Space Complexity:
O(n)

"""
from typing import List


class Solution:
    def two_sum(self, nums: List[int],target:int) -> List[int]:
        dic={}
        for i in range(len(nums)):
            if nums[i] in dic:
                return dic[nums[i]],i
            else:
                dic[target-nums[i]]=i


if __name__ == "__main__":
    solution_instance = Solution()
    s=[2,7,11,15]

    print(solution_instance.two_sum(s,17))

""""
Explanation:

Initialization: 
Initialize an empty dictionary dic. This dictionary will store the elements from the input array nums
as keys and their corresponding indices as values.

Iteration through the array: 
Use a for loop to iterate through each element in the input array nums.

Checking if complement exists:
For each element nums[i], check if its complement (i.e., target - nums[i]) is already 
present in the dictionary dic. If it is, return the indices of the two elements that add up to the target.

Updating the dictionary: 
If the complement is not found in the dictionary, update the dictionary by adding the current 
element's complement as a key with the current index as its value.
    
"""
