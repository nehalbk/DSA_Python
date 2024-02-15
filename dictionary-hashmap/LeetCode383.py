"""

Problem:

383. Ransom Note
Easy
Topics
Companies
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from
magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.



Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true


Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.

Time Complexity:
O(n)

Space Complexity:
O(n)

"""
from collections import Counter
from typing import List


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran = Counter(ransomNote)
        mag = Counter(magazine)

        for i in ran:
            if mag[i] < ran[i]:
                return False
        return True


if __name__ == "__main__":
    solution_instance = Solution()
    ransomNote = "aa"
    magazine = "aab"

    print(solution_instance.canConstruct(ransomNote, magazine))

""""
Explanation:

**Approach:**
The approach of the code is to determine if a ransom note can be constructed from a given magazine. 
It uses the Counter class from the collections module to create dictionaries that count the occurrences of each 
character in the ransom note and magazine. It then iterates through the characters in the ransom note and checks if 
there are enough occurrences of each character in the magazine to construct the ransom note.

**Time Complexity:**
Let m be the length of the ransomNote and n be the length of the magazine. The time complexity of this code is O(m + n).
This is because constructing the Counters for both ransomNote and magazine takes O(m +n) time, and the subsequent loop 
through the ransomNote characters has a time complexity of (O(m).

**Space Complexity:**
The space complexity is also O(m + n). This is due to the space required to store the Counters for ransomNote and 
magazine, each of which can have at most (m + n) unique characters (assuming all characters in the ransomNote and 
magazine are distinct).

In summary, the code is efficient in terms of time and space complexity for determining if a ransom note can be 
constructed from a given magazine.
"""
