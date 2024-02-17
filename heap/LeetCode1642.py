"""

Problem:
1642. Furthest Building You Can Reach
Solved
Medium
Topics
Companies
Hint
You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

If the current building's height is greater than or equal to the next building's height, you do not need a ladder or
bricks.
If the current building's height is less than the next building's height, you can either use one ladder or
(h[i+1] - h[i]) bricks.
Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.



Example 1:


Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
Output: 4
Explanation: Starting at building 0, you can follow these steps:
- Go to building 1 without using ladders nor bricks since 4 >= 2.
- Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 < 7.
- Go to building 3 without using ladders nor bricks since 7 >= 6.
- Go to building 4 using your only ladder. You must use either bricks or ladders because 6 < 9.
It is impossible to go beyond building 4 because you do not have any more bricks or ladders.
Example 2:

Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
Output: 7
Example 3:

Input: heights = [14,3,19,3], bricks = 17, ladders = 0
Output: 3


Constraints:

1 <= heights.length <= 105
1 <= heights[i] <= 106
0 <= bricks <= 109
0 <= ladders <= heights.length


Constraints:

1 <= n <= 104

Time Complexity:
O(N * log N)

Space Complexity:
O(ladders)

"""
import math
from typing import List


import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                heapq.heappush(heap, diff)
                if len(heap) > ladders:
                    bricks -= heapq.heappop(heap)
                if bricks < 0:
                    return i
        return len(heights) - 1


if __name__ == "__main__":
    solution_instance = Solution()
    h = [4,12,2,7,3,18,20,3,19]
    b = 10
    l = 2
    print(solution_instance.furthestBuilding(h,b,l))

""""
Explanation:

Approach:

The approach used in this code is to iterate through the buildings, calculating the height difference between 
consecutive buildings. The code uses a min heap to keep track of the height differences that require ladders, 
prioritizing the smallest differences. It simulates the process of climbing buildings, using ladders for the smallest 
height differences and switching to bricks when necessary. The algorithm ensures efficient usage of ladders for taller 
buildings, maximizing the furthest reachable building with the given resources.

Time Complexity:

The time complexity of the code is primarily determined by the iteration through the given heights list, which has a 
time complexity of O(N), where N is the number of buildings. Within the loop, the operations involving the min heap 
(heapq.heappush and heapq.heappop) have a time complexity of O(log k), where k is the size of the heap (limited by the 
number of ladders). In the worst case, the size of the heap can be N, resulting in an additional O(N * log N) time 
complexity for heap operations.

Therefore, the overall time complexity is O(N * log N).

Space Complexity:

The space complexity is determined by the additional data structures used. The primary data structure is the min heap 
(heap), which can have a maximum size of ladders (if all height differences require ladders). Hence, the space 
complexity is O(ladders).

In addition to the min heap, there are constant space variables like diff, i, and the function parameters. Therefore, 
the overall space complexity is O(ladders), where ladders is the maximum number of ladders available.

In summary, the space complexity is linear in terms of the maximum number of ladders available.
"""
