"""

Problem:

228. Summary Ranges

You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums
 is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b


Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"


Constraints:

0 <= nums.length <= 20
-231 <= nums[i] <= 231 - 1
All the values of nums are unique.
nums is sorted in ascending order.

Time Complexity:
O(n)

Space Complexity:
O(n)

"""
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        res = []
        start = end = nums[0]

        for num in nums[1:]:
            if num == end + 1:
                end = num
            else:
                res.append(f"{start}->{end}" if start != end else str(start))
                start = end = num

        res.append(f"{start}->{end}" if start != end else str(start))

        return res


if __name__ == "__main__":
    solution_instance = Solution()
    nums = [0,1,2,4,5,7]

    print(solution_instance.summaryRanges(nums))

""""
Explanation:

**Approach:**

The `summaryRanges` method iterates through the given list of numbers (`nums`) to identify consecutive ranges and 
summarizes them. It uses two pointers, `start` and `end`, to keep track of the current range. If the next number in the 
list is consecutive to the current range, the `end` pointer is updated. If the next number is not consecutive, the 
current range is appended to the result (`res`), and the pointers are reset to the new number. The process continues 
until all numbers are processed.

**Time Complexity:**

The time complexity of this algorithm is O(N), where N is the number of elements in the input list `nums`. The algorithm
 iterates through the list once, and for each element, it performs constant-time operations.

**Space Complexity:**

The space complexity is O(1) because the algorithm uses a constant amount of additional space to store variables 
(`res`, `start`, `end`). The space required does not scale with the size of the input list; it remains constant 
regardless of the input size.
"""
