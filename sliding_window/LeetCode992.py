"""

Problem:
992. Subarrays with K Different Integers
Solved
Hard
Topics
Companies
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.



Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
Example 2:

Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].


Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i], k <= nums.length

"""
from collections import defaultdict
from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        count =defaultdict(int)
        res=0
        lfar=0
        lnear=0
        for i in range(len(nums)):
            count[nums[i]] +=1
            while len(count)>k:
                count[nums[lnear]]-=1
                if count[nums[lnear]] ==0:
                    count.pop(nums[lnear])
                lnear+=1
                lfar=lnear
            while count[nums[lnear]]>1:
                count[nums[lnear]]-=1
                lnear+=1
            if len(count) ==k:
                res+=lnear-lfar+1
        return res

if __name__ == "__main__":
    solution_instance = Solution()
    num = [1,2,1,2,3]
    result = solution_instance.subarraysWithKDistinct(num,2)
    print(result)

