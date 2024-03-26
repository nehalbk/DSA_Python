"""

Problem:
242. Valid Anagram
Easy
Topics
Companies
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the
original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.


Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

Time Complexity:
O(log n)

Space Complexity:
O(1)

"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dictS={}
        dictT={}
        for i in range(len(s)):
            dictS[s[i]] = dictS.get(s[i],0)+1
            dictT[t[i]] = dictT.get(t[i],0) + 1
        for c in dictS:
            if dictS[c] != dictT.get(c,0):
                return False
        return True


if __name__ == "__main__":
    solution_instance = Solution()
    s="Hello"
    t="olleh"
    result = solution_instance.isAnagram(s,t)
    print(result)

""""

"""
