"""

Problem:
202. Happy Number
Easy
Topics
Companies
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.



Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false


Constraints:

1 <= n <= 231 - 1

Time Complexity:
O(log n)

Space Complexity:
O(log n)

"""
from itertools import count
from typing import List

from unicodedata import decimal


# Brute Force Method:
# class Solution:
#     def isHappy(self, n: int) -> bool:
#         sum =0
#         s=set()
#         print(n)
#         while sum!=1 and (sum not in s):
#             print(s)
#             s.add(sum)
#             sum=0
#             while(n>0):
#                 # print(n)
#                 sum=sum+ (n%10)**2
#                 n=n//10
#             print(sum)
#             n=sum
#         if(sum==1):
#             return True
#         else:
#             return False

# Optimized Method:
class Solution:
    def isHappy(self, n: int) -> bool:
        s=set()
        while n!=1:
            if n in s:
                return False
            s.add(n)
            n=sum(int(i)**2 for i in str(n))


        return True

if __name__ == "__main__":
    solution_instance = Solution()
    num = 89
    result = solution_instance.isHappy(num)
    print(result)

""""
**Approach:**

The code determines whether a given number is a "happy number" or not. A happy number is a number which, when repeatedly
replaced by the sum of the squares of its digits, eventually reaches the number 1. The code uses a set (`s`) to keep 
track of the numbers encountered during this process. It iteratively calculates the sum of the squares of the digits 
until either the sum becomes 1 (indicating a happy number) or a cycle is detected in the set (indicating an unhappy 
number).

**Time Complexity:**

The time complexity of this code depends on the number of iterations needed to reach either the happy state 
(sum equals 1) or detect a cycle. In the worst case, the algorithm will run until a cycle is found, which is generally 
considered as O(log N), where N is the given number. This is because the process tends to reduce the number of digits 
with each iteration.

The `sum(int(i)**2 for i in str(n))` part contributes O(log N) time complexity since the number of digits in `n` is 
proportional to log N.

**Space Complexity:**

The space complexity is determined by the set `s`, which stores the numbers encountered during the process. In the worst
case, the set can contain all distinct numbers from the sequence until reaching either the happy state or detecting a 
cycle. Therefore, the space complexity is also O(log N) in the worst case.

In summary, the code has a time complexity of O(log N) and a space complexity of O(log N), where N is the given number.
"""
