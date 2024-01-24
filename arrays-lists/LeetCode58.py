"""

Problem:

58. Length of Last Word
Solved
Easy
Topics
Companies
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal
substring
 consisting of non-space characters only.



Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.


Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.

Time Complexity:
O(m + n)

Space Complexity:
O(1)

"""
from typing import List


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c=0
        for i in range(len(s)):
            if c>0 and s[len(s)-i-1]==" ":
                return c
            if s[len(s)-i-1]!=" ":
                c+=1
        return c




if __name__ == "__main__":
    solution_instance = Solution()
    s="   fly me   to   the moon  "

    print(solution_instance.lengthOfLastWord(s))

""""
Explanation:

1. Initialization:

    i is the pointer for the last element in nums1.
    j is the pointer for the last element in nums2.
    k is the pointer for the position in the merged result array (nums1).

2. Merging in Reverse Order:

    We start from the end of both arrays-lists (nums1 and nums2) and compare elements.
    The larger element is placed at the end of the merged array (nums1).
    We move the pointers accordingly.

3. Copying Remaining Elements:

    After merging, if there are remaining elements in nums2, we copy them to the merged array (nums1).
    We continue updating pointers and copying until both arrays-lists are fully merged.
    
"""
