"""

Problem:

13. Roman to Integer
Solved
Easy
Topics
Companies
Hint
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X
+ II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same
principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.



Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].

Time Complexity:
O(n)

Space Complexity:
O(n)

"""
from typing import List


class Solution:
    def romanToInt(self, s: str) -> int:
        bag={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        last=0
        res=0
        for i in s[::-1]:
            if(bag[i]>=last):
                res +=bag[i]
            else:
                res-=bag[i]
            last=bag[i]
        return res


if __name__ == "__main__":
    solution_instance = Solution()
    s="MIV"

    print(solution_instance.romanToInt(s))

""""
Explanation:

**Approach:**
The approach of the code is to iterate through the input Roman numeral string in reverse order. For each character, it 
compares its corresponding value in the dictionary `bag` with the value of the previous character (`last`). Based on 
this comparison, it either adds or subtracts the current value from the result (`res`). The `last` variable is updated 
to keep track of the previous numeral value.

**Space Complexity:**
The space complexity of this code is O(1) since it uses a constant amount of extra space regardless of the size of the 
input string. The dictionary `bag` has a fixed number of entries corresponding to the Roman numerals, and the variables 
`last` and `res` are scalars.

**Time Complexity:**
The time complexity is O(n), where n is the length of the input string. The code iterates through each character in the 
input string once, performing constant-time operations for each character. Therefore, the time complexity is linear with
respect to the size of the input.
    
"""
