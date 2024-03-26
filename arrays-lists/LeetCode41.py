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
Explanation:

Approach:
    The function lengthOfLastWord is designed to find the length of the last word in a given string s. 
    The approach used is to iterate through the string from right to left and count the characters of the last word 
        until a space character is encountered.

Explanation:

    Initialize a counter c to 0.
    Iterate through the characters of the string s from right to left.
    Increment the counter c as long as non-space characters are encountered.
    When a space character is encountered and the counter c is already greater than 0, return the value of c as it 
        represents the length of the last word.
    If the loop completes and there is no space character, return the final value of the counter c.

Time Complexity:

    The time complexity of the program is O(n), where n is the length of the input string s.
    The loop iterates through the string once, and each iteration involves constant-time operations.

Space Complexity:

    The space complexity is O(1), as the program uses a constant amount of space regardless of the size of the input.
    The only variable used is c, and it does not depend on the length of the input string.
    
"""
