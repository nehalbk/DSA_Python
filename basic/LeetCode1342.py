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
O(1)

"""


class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num > 0:
            if num % 2 == 0:
                num = num/2
            else:
                num = num-1
            count=count+1
        return count


if __name__ == "__main__":
    solution_instance = Solution()
    num = 8
    result = solution_instance.numberOfSteps(num)
    print(result)

""""
Explanation:

1. **Initialization:** The method starts by initializing a variable `count` to 0. This variable will be used to keep track of the number of steps taken.

2. **While Loop:** The code enters a `while` loop, which continues until the value of `num` becomes zero.

3. **Checking Even or Odd:**
   - Inside the loop, there is a conditional statement (`if-else`) to check whether the current value of `num` is even or odd.
   - If `num` is even (`num % 2 == 0`), it is divided by 2 (`num = num / 2`).
   - If `num` is odd, 1 is subtracted from it (`num = num - 1`).

4. **Incrementing Count:** After each operation (either division by 2 or subtraction by 1), the `count` variable is incremented by 1.

5. **Returning Count:** Once the loop exits (when `num` becomes 0), the method returns the final value of `count`, which represents the total number of steps taken to reduce the original number to zero.

"""
