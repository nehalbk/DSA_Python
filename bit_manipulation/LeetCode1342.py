"""

Problem:
1342. Number of Steps to Reduce a Number to Zero

Link:
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/description/

Description:
Given an integer num, return the number of steps to reduce it to zero.
In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

Example:

Example 1:

Input: num = 14
Output: 6
Explanation:
Step 1) 14 is even; divide by 2 and obtain 7.
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3.
Step 4) 3 is odd; subtract 1 and obtain 2.
Step 5) 2 is even; divide by 2 and obtain 1.
Step 6) 1 is odd; subtract 1 and obtain 0.
Example 2:

Input: num = 8
Output: 4
Explanation:
Step 1) 8 is even; divide by 2 and obtain 4.
Step 2) 4 is even; divide by 2 and obtain 2.
Step 3) 2 is even; divide by 2 and obtain 1.
Step 4) 1 is odd; subtract 1 and obtain 0.
Example 3:

Input: num = 123
Output: 12

Constraints:
0 <= num <= 106

Time Complexity:
O(log n)

Space Complexity:
O(log n)

"""


class Solution:
    def numberOfSteps(self, num: int) -> int:
        return 2*(bin(num).count('1')) + bin(num).count('0') - 2 if num > 0 else 0


if __name__ == "__main__":
    solution_instance = Solution()
    num = 8
    result = solution_instance.numberOfSteps(num)
    print(result)

""""
Explanation:

1. `bin(num).count('1')`: Count the number of '1' bits in the binary representation of `num`. This represents the steps needed for odd numbers (subtract 1 and then right shift).
  
2. `bin(num).count('0')`: Count the number of '0' bits in the binary representation of `num`. This represents the steps needed for even numbers (only right shift).

3. `2 * bin(num).count('1')`: Multiply the count of '1' bits by 2 to account for the two steps needed for each '1' bit.

4. `- 2`: Subtract 2 to adjust for the fact that the rightmost '0' bit doesn't require an additional step.

5. `if num > 0 else 0`: If `num` is greater than 0, return the computed result; otherwise, return 0 (as there are no steps needed for 0).

Overall, this modified solution provides the correct result for the given problem and has a time and space complexity of O(log n).
"""
