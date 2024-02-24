"""

Problem:
6. Zigzag Conversion
Medium
Topics
Companies
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     d    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"


Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000

Time Complexity:
O(log n)

Space Complexity:
O(1)

"""
from itertools import count
from typing import List

from unicodedata import decimal


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        sum: int =numRows
        i: int = 1
        while sum<=len(s):
            print(sum)
            if  i%numRows==0:
                sum=sum+numRows
            else:
                sum+=1
            i+=1

        print(i)
        return ""


if __name__ == "__main__":
    solution_instance = Solution()
    s="PAYPALISHIRING"
    row = 3
    result = solution_instance.convert(s,row)
    print(result)

""""
Explanation:

This code implements the binary search algorithm to find the insertion position of a target value in a sorted list of 
integers. The goal is to return the index at which the target value should be inserted to maintain the sorted order of 
the list.

Here's the step-by-step explanation of the approach:

1. **Initialization:**
   - `left` is the starting index of the search space, initialized to 0.
   - `right` is the ending index of the search space, initialized to `len(nums) - 1`.

2. **Binary Search Loop:**
   - Use a `while` loop to continue the search until the search space is exhausted (`left > right`).
   - Inside the loop, calculate the middle index `mid` as `(left + right) // 2`.

3. **Comparison with Target:**
   - Check if the element at the middle index (`nums[mid]`) is equal to the target.
     - If yes, return `mid` as the index where the target is found.

   - If `nums[mid]` is less than the target, update `left` to `mid + 1`.
     - This means the target, if present, must be on the right side of the current middle element.

   - If `nums[mid]` is greater than the target, update `right` to `mid - 1`.
     - This means the target, if present, must be on the left side of the current middle element.

4. **Search Space Update:**
   - If the target is not found in the current iteration, the search space is updated based on whether the target is 
        greater or smaller than the middle element.
   - The search space is narrowed down to the left or right half in each iteration.

5. **Result:**
   - If the loop completes without finding the target, return the `left` index as the insertion position.
     - This is because `left` points to the position where the target should be inserted to maintain the sorted order.

The overall approach leverages the binary search technique to efficiently locate the insertion position of the target 
in the sorted list. The time complexity of this algorithm is O(log n), where n is the length of the input list `nums`.
The space complexity of the provided code is O(1), meaning it uses a constant amount of extra space regardless of the 
input size. The memory usage is constant because the algorithm only uses a fixed number of variables 
(left, right, mid, target) and does not use any data structures that scale with the input size.
"""
