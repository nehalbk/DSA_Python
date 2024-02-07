"""

Problem:

387. First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.



Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1


Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.

Time Complexity:
O(n)

Space Complexity:
O(k)

"""
from typing import List
from collections import Counter


class Solution:

    # Slightly Efficient 👇
    # ------------------------------------------------------------------------------------------------------------------
    # def firstUniqChar(self, s: str) -> int:
    #     dic={}
    #     for i in list(s):
    #         if i in dic:
    #             dic[i]=dic[i]+1
    #         else:
    #             dic[i] = 1
    #
    #     for i in range(len(s)):
    #         if dic[s[i]]==1:
    #             return i
    #     return -1

    # Highly Efficient 👇
    # ------------------------------------------------------------------------------------------------------------------
    def firstUniqChar(self, s: str) -> int:
        char_count = Counter(s)
        print(char_count)

        for i, char in enumerate(s):
            if char_count[char] == 1:
                return i

        return -1


if __name__ == "__main__":
    solution_instance = Solution()
    s = "aaabbb"

    print(solution_instance.firstUniqChar(s))

""""
Explanation:

Approach:

The firstUniqChar method aims to find the index of the first unique character in the given string s. 
The approach involves using the Counter class from the collections module to efficiently count the occurrences of each 
character in the string. After obtaining the character counts, the method iterates through the string using the 
enumerate function, and it returns the index of the first character with a count of 1. If no such character is found, 
it returns -1.

Time Complexity:

The time complexity of this algorithm is O(N), where N is the length of the input string s. The Counter class builds a 
dictionary with counts for each character in linear time, and the subsequent loop iterates through the string once. 
Each operation within the loop, such as accessing the count of a character in the dictionary or returning the index, 
takes constant time.

Space Complexity:

The space complexity is O(K), where K is the number of unique characters in the string s. The Counter class creates a 
dictionary with counts for each unique character. In the worst case, when all characters are unique, the dictionary 
will have a size proportional to the length of the string. The additional space used for variables like char_count, i, 
and char within the loop is constant and does not depend on the input size.
    
"""
