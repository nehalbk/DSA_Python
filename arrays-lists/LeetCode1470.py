"""

Problem:

1470. Shuffle the Array

Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].



Example 1:

Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7]
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
Example 2:

Input: nums = [1,2,3,4,4,3,2,1], n = 4
Output: [1,4,2,3,3,2,4,1]
Example 3:

Input: nums = [1,1,2,2], n = 2
Output: [1,2,1,2]


Constraints:

1 <= n <= 500
nums.length == 2n
1 <= nums[i] <= 10^3

Time Complexity:
O(n)

Space Complexity:
O(1)

"""
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res=[]
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i+n])
        return res


if __name__ == "__main__":
    solution_instance = Solution()
    s=[2,5,1,3,4,7]
    n=3

    print(solution_instance.shuffle(s,n))

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
