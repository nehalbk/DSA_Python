"""

Problem:

49. Group Anagrams
Medium
Topics
Companies
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the
original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]


Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

Time Complexity:
O(K * log(K))

Space Complexity:
O(N * K)

"""
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for i in strs:
            sr= "".join(sorted(i))
            if sr in dic:
                dic[sr]=dic[sr]+[i]
            else:
                dic[sr]=[i]
        return(list(dic.values()))


if __name__ == "__main__":
    solution_instance = Solution()
    s=["eat","tea","tan","ate","nat","bat"]

    print(solution_instance.groupAnagrams(s))

""""
Explanation:

**Approach:**

The `groupAnagrams` method aims to group anagrams from a given list of strings (`strs`). It uses a dictionary (`dic`) 
to store anagrams, where the keys are sorted versions of the strings (anagrams will have the same sorted version). 
The method iterates through each string in the input list, sorts its characters, and then checks whether the sorted 
version already exists in the dictionary. If it does, the current string is appended to the existing list of anagrams; 
otherwise, a new entry is created with the sorted string as the key.

After processing all strings, the method returns a list containing the grouped anagrams.

**Time Complexity:**

The time complexity of this algorithm is O(N * K * log(K)), where N is the number of strings in the input list `strs`, 
and K is the maximum length of any string in `strs`. The dominant factor is the sorting operation, which takes 
O(K * log(K)) time for each string.

**Space Complexity:**

The space complexity is O(N * K), where N is the number of strings in the input list `strs`, and K is the maximum length
of any string in `strs`. The additional space is used for the dictionary (`dic`), where each entry requires O(K) space 
for the sorted string key and the list of anagrams. The final list of grouped anagrams is also included in the space 
complexity.
"""
