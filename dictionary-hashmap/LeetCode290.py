"""

Problem:

290. Word Pattern
Solved
Easy
Topics
Companies
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.



Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false


Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.

Time Complexity:
O(n)

Space Complexity:
O(n)

"""
from typing import List


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = {}
        s = s.split()
        if len(pattern) != len(s):return False
        for char, word in zip(pattern, s):
            if char in dic:
                if dic[char] != word: return False
            else:
                if word in dic.values():return False
                dic[char] = word
        return True



if __name__ == "__main__":
    solution_instance = Solution()
    pattern = "abba"
    s = "dog cat cat dog"

    print(solution_instance.wordPattern(pattern,s))

""""
Explanation:

Approach:

The approach of the wordPattern method is to check whether a given pattern matches a string. It uses a dictionary (dic) 
to map each character in the pattern to its corresponding word in the string. The code iterates through the pattern and 
string simultaneously, updating the dictionary with new mappings and checking for mismatches. The code also ensures that
 the lengths of the pattern and string are equal before proceeding with the comparison.

Time Complexity:

The time complexity of this code is O(N), where N is the length of the input pattern or string. The iteration through 
the pattern and string has a linear time complexity. Additionally, dictionary operations, such as checking for the 
existence of a key (char in dic) and retrieving the value associated with a key (dic[char]), have constant time 
complexity on average.

Space Complexity:

The space complexity of this code is O(M), where M is the size of the dictionary dic. In the worst case, where all 
characters in the pattern have distinct mappings to words, the size of the dictionary could be equal to the length of 
the pattern. The space used for the split string (s.split()) is O(N), where N is the length of the input string.

In summary, the space complexity is dominated by the size of the dictionary, and the overall space complexity is 
O(M + N). The time complexity is linear, making the code efficient for the given problem.
    
"""
