"""

Problem:
28. Find the Index of the First Occurrence in a String
Solved
Easy
Topics
Companies
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle
is not part of haystack.



Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.


Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.

Time Complexity:
O(n)

Space Complexity:
O(1)

"""
from typing import List


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if not needle:
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            match = True
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    match = False
                    break
            if match:
                return i

        return -1


if __name__ == "__main__":
    solution_instance = Solution()
    haystack = "leetcode"
    needle = "leeto"

    print(solution_instance.strStr(haystack,needle))

""""
Explanation:

**Approach:**
The provided code implements a simple string matching algorithm to find the first occurrence of a needle within a 
haystack. It uses a nested loop to compare characters, checking for a match at each possible starting position in the 
haystack.

**Time Complexity:**
The time complexity of this code is O((n-m+1) * m), where n is the length of the haystack and m is the length of the 
needle. The outer loop iterates through all possible starting positions in the haystack, and for each starting position,
 the inner loop compares characters up to the length of the needle.

**Space Complexity:**
The space complexity is O(1) because the algorithm uses a constant amount of extra space regardless of the input size. 
The memory usage is mainly for the loop indices and the boolean variable `match`. The algorithm does not use any data 
structures that scale with the input size.

**Optimization:**
This algorithm is a straightforward implementation, and while it works, it may not be the most efficient for large 
inputs. For improved efficiency, especially for longer needles, algorithms like the Knuth-Morris-Pratt (KMP) algorithm c
an be employed. KMP reduces the number of character comparisons by precomputing a prefix table, leading to a linear time
complexity for string matching.    
"""
