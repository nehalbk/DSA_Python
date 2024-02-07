"""

Problem:

387. First Unique Character in a String

451. Sort Characters By Frequency
Medium
Topics
Companies
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is
the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.



Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.


Constraints:

1 <= s.length <= 5 * 105
s consists of uppercase and lowercase English letters and digits.

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
    #     def frequencySort(self, s: str) -> str:
    #         char_count = Counter(s)
    #         sorted_chars = sorted(char_count, key=lambda ch: char_count[ch], reverse=True)
    #         res = ''.join(ch * char_count[ch] for ch in sorted_chars)
    #         return res

    # Highly Efficient 👇
    # ------------------------------------------------------------------------------------------------------------------
    def frequencySort(self, s: str) -> str:
        char_count = Counter(s)
        sorted_chars = char_count.most_common()
        res = ''.join(ch * count for ch, count in sorted_chars)
        return res


if __name__ == "__main__":
    solution_instance = Solution()
    s = "tree"

    print(solution_instance.frequencySort(s))

""""
Explanation:

Approach:
The code uses the Counter class from the collections module to count the occurrences of each character in the input 
string s.
It then uses the most_common() method to obtain a list of character-frequency pairs sorted by frequency in descending 
order.
Finally, it creates a new string by concatenating characters based on their frequencies in the sorted list.

Time Complexity:
Creating the Counter object takes O(n) time, where n is the length of the input string s.
Sorting the character-frequency pairs using most_common() takes O(c * log(c)) time, where c is the number of unique 
characters.
Constructing the result string by joining characters based on their frequencies takes O(c) time.
Therefore, the overall time complexity is O(n + c * log(c)), where n is the length of the input string and c is the 
number of unique characters.

Space Complexity:
The space complexity is dominated by the Counter object, which stores the count of each unique character. In the worst 
case, where all characters are unique, the space complexity is O(c).
The sorted character-frequency pairs and the result string also contribute to the space complexity, but their combined 
space is O(c).

Overall, the space complexity is O(c).
In summary, the time complexity is O(n + c * log(c)), and the space complexity is O(c), where n is the length of the 
input string, and c is the number of unique characters.    

"""
