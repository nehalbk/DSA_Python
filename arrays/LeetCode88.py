"""

Problem:
88. Merge Sorted Array

Link:
https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

Description:
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example:

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

Constraints:
nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109

Time Complexity:
O(m + n)

Space Complexity:
O(1)

"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None :
        i,j,k=m-1,n-1,n+m-1
        while i>=0 and j>=0:
            if nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i-=1
            else:
                nums1[k]=nums2[j]
                j-=1
            k-=1

        while j>=0:
            nums1[k]=nums2[j]
            k-=1
            j-=1



if __name__ == "__main__":
    solution_instance = Solution()
    nums1 = [1,2,3,0,0,0]
    nums2=[2,5,6]
    n=3
    m=3
    solution_instance.merge(nums1,m,nums2,n)
    print(nums1)

""""
Explanation:

1. Initialization:

    i is the pointer for the last element in nums1.
    j is the pointer for the last element in nums2.
    k is the pointer for the position in the merged result array (nums1).

2. Merging in Reverse Order:

    We start from the end of both arrays (nums1 and nums2) and compare elements.
    The larger element is placed at the end of the merged array (nums1).
    We move the pointers accordingly.

3. Copying Remaining Elements:

    After merging, if there are remaining elements in nums2, we copy them to the merged array (nums1).
    We continue updating pointers and copying until both arrays are fully merged.
    
"""
