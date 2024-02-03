"""

Problem:
217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every
element is distinct.


Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109

Time Complexity:
O(n)

Space Complexity:
O(min(n, m))

"""
from itertools import count
from typing import List

from unicodedata import decimal


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dist = set()
        for i in range(len(nums)):
            if nums[i] in dist:
                return True
            else:
                dist.add(nums[i])
        return False


if __name__ == "__main__":
    solution_instance = Solution()
    num = [1,3,5,6]
    result = solution_instance.containsDuplicate(num)
    print(result)

""""
Explanation:

The code is checking for the presence of duplicate elements in the given list nums by using a set (dist) to keep track 
of unique elements encountered so far. It iterates through the list, and at each step, it checks whether the current 
element (nums[i]) is already in the set. If it is, then a duplicate is found, and the function returns True. Otherwise, 
the element is added to the set. If the loop completes without finding any duplicates, the function returns False.

Time Complexity:
The time complexity of this code is O(n), where n is the length of the input list nums. In the worst case, it may need 
to iterate through all elements in the list once, and each set operation (in check or add) takes constant time on 
average.

Space Complexity:
The space complexity is O(min(n, m)), where n is the length of the input list nums, and m is the number of unique 
elements in nums. In the worst case, when all elements are unique, the set (dist) will have to store all elements, 
resulting in O(n) space complexity. However, if there are fewer unique elements than the length of the list, the space 
complexity will be closer to O(m).


Special Note:

Using list would make time complexity O(n^2) as searching in list is O(n).
For sets and dictionaries it is O(1).
"""
