"""

Problem:

58. Length of Last Word

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
O(n)

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
