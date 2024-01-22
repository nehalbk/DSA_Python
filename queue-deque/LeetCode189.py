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
O(m + n)

Space Complexity:
O(1)

"""
from typing import List
from collections import deque


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotate the list to the right by k steps in-place using deque.
        :param nums: List of integers to be rotated.
        :param k: Number of steps to rotate to the right.
        :return: None (modifies nums in-place).
        """

        # Use deque for efficient rotation
        dq = deque(nums)

        # Perform rotation k times by popping the last element and appending it to the left
        for i in range(k):
            element = dq.pop()
            dq.appendleft(element)

        # Update the original list with the rotated values
        nums[:] = list(dq)


if __name__ == "__main__":
    # Example usage
    solution_instance = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]

    # Rotate the list by 3 steps to the right
    solution_instance.rotate(nums, 3)

    # Print the modified list
    print(nums)

""""
Explanation:

1.Using Deque for Efficient Rotation:

    The code uses a deque (double-ended queue) to efficiently rotate the list.
    A deque supports O(1) time complexity for adding and removing elements from both ends.
    
2.Rotating Elements:

    The code initializes a deque with the elements of the input list.
    It then performs a rotation by popping the last element from the deque and appending it to the left side.
    This process is repeated k times to achieve the desired right rotation.
    
3.Updating Original List:

    After the rotation operations on the deque, the original list is updated with the rotated values.
    This step ensures that the modifications are reflected in the original list, as the deque is used 
        for efficient rotation but is not the final result.

4.Time Complexity:

    The overall time complexity is O(n) due to the deque operations and list update.
    The for loop performs k rotations, each taking constant time.
    
5. Space Complexity:

    The space complexity is O(n) due to the use of a deque to store the elements of the input list.
    The algorithm uses a constant amount of extra space for the deque, regardless of the size of the input list.
    In summary, the approach efficiently leverages a deque to perform right rotations in O(n) time and O(n) space, 
        and the original list is updated in-place to reflect the rotated values.
    





    
"""
