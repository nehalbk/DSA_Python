"""

Problem:
189. Rotate Array

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105


Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?

Time Complexity:
O(n)

Space Complexity:
O(1)

"""

from typing import List


class Solution:
    def reverse(self, nums: List[int], left: int, right: int) -> None:
        """
        Reverse a portion of the list in-place using a two-pointer approach.
        """
        while left < right:
            # Swap elements at left and right indices
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            # Move towards the center of the range
            left += 1
            right -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotate the list in-place to the right by k steps.
        """
        n = len(nums)
        k = k % n  # Calculate the effective rotation value

        # Reverse the entire list
        self.reverse(nums, 0, n - 1)

        # Reverse the first k elements
        self.reverse(nums, 0, k - 1)

        # Reverse the remaining elements
        self.reverse(nums, k, n - 1)


if __name__ == "__main__":
    # Example usage
    solution_instance = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    solution_instance.rotate(nums, 3)
    print(nums)

""""
Explanation:

This algorithm first reverses the entire list, then reverses the first k elements, and finally reverses the remaining 
elements. The combination of these operations effectively rotates the list to the right by k steps, all done in-place 
with O(1) extra space.
    
"""
