"""

Problem:
2769. Find the Maximum Achievable Number
Solved
Easy
Topics
Companies
Hint
You are given two integers, num and t.

An integer x is called achievable if it can become equal to num after applying the following operation no more than t times:

Increase or decrease x by 1, and simultaneously increase or decrease num by 1.
Return the maximum possible achievable number. It can be proven that there exists at least one achievable number.



Example 1:

Input: num = 4, t = 1
Output: 6
Explanation: The maximum achievable number is x = 6; it can become equal to num after performing this operation:
1- Decrease x by 1, and increase num by 1. Now, x = 5 and num = 5.
It can be proven that there is no achievable number larger than 6.

Example 2:

Input: num = 3, t = 2
Output: 7
Explanation: The maximum achievable number is x = 7; after performing these operations, x will equal num:
1- Decrease x by 1, and increase num by 1. Now, x = 6 and num = 4.
2- Decrease x by 1, and increase num by 1. Now, x = 5 and num = 5.
It can be proven that there is no achievable number larger than 7.


Constraints:

1 <= num, t <= 50

Constraints:
0 <= num <= 106

Time Complexity:
O(1)

Space Complexity:
O(1)

"""


class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num+t*2


if __name__ == "__main__":
    solution_instance = Solution()
    num = 4
    t= 1
    result = solution_instance.theMaximumAchievableX(num,t)
    print(result)

""""
Explanation:

**Approach:**

The approach of the given code is straightforward. The `theMaximumAchievableX` method takes two parameters, `num` and 
`t`, and returns the result of the expression `num + t * 2`. The code simply adds twice the value of `t` to the initial 
value of `num`. This expression represents a linear operation that increases the value of `num` by a multiple of 2 times
the value of `t`.

**Time Complexity:**

The time complexity of this code is constant (O(1)). Regardless of the values of `num` and `t`, the execution time 
remains the same. The code performs a fixed number of operations, and the time required for its execution is not 
dependent on the input size.

**Space Complexity:**

The space complexity is also constant (O(1)). The code does not use any additional data structures or variables whose 
space requirements depend on the input size. The space needed for the parameters `num` and `t` and the local variable 
storing the result is constant regardless of the input values.

In summary, both the time and space complexity of this code are constant, making it an efficient and straightforward 
operation.
"""
