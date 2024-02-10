"""

Problem:

645. Set Mismatch
Easy
Topics
Companies
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error,
one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss
of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.



Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]


Constraints:

2 <= nums.length <= 104
1 <= nums[i] <= 104

Time Complexity:
O(n)

Space Complexity:
O(n)

"""
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        sum_c=int(len(nums)*(len(nums)+1)/2)
        bas={}
        sum_a=sum(nums)
        for i in nums:
            if i in bas:
                rep=i
            else:
                bas[i]=0
        return [rep,sum_c-(sum_a-rep)]


if __name__ == "__main__":
    solution_instance = Solution()
    s=[1,2,3,3,5,6]

    print(solution_instance.findErrorNums(s))

""""
Explanation:

### Approach:
1. `sum_c` is calculated as the sum of the first `n` positive integers (where `n` is the length of the `nums` array) 
    using the formula `n * (n + 1) / 2`. This represents the sum of all elements if there were no repeating or missing 
    elements.
2. `bas` is initialized as an empty dictionary to keep track of seen elements.
3. `sum_a` is calculated as the sum of all elements in the `nums` array.
4. The loop iterates through each element `i` in `nums`.
   - If `i` is already in `bas`, it means it is a repeating element, and `rep` is set to the repeated element.
   - Otherwise, `i` is added to `bas`.
5. The result is a list containing the repeating element (`rep`) and the missing element calculated using the expected 
    sum (`sum_c`) and the actual sum (`sum_a`).

### Time Complexity:
- The `sum` function takes O(n) time, where n is the length of the `nums` array.
- The loop iterates through each element in `nums`, and the operations inside the loop take constant time.
- Overall, the time complexity is O(n).

### Space Complexity:
- The space complexity is primarily determined by the size of the `bas` dictionary.
- In the worst case, all elements are distinct, and `bas` would store all elements of `nums`, resulting in a space 
    complexity of O(n).
- Additional space is used for integer variables (`sum_c`, `sum_a`, `rep`).
- Overall, the space complexity is O(n).

In summary, the code aims to find the repeating and missing elements in the `nums` array and has a time complexity of 
O(n) and a space complexity of O(n).
    
"""
