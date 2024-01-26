"""

Problem:

1637. Widest Vertical Area Between Two Points Containing No Points

Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that
no points are inside the area.

A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest
vertical area is the one with the maximum width.

Note that points on the edge of a vertical area are not considered included in the area.



Example 1:

​
Input: points = [[8,7],[9,9],[7,4],[9,7]]
Output: 1
Explanation: Both the red and the blue area are optimal.
Example 2:

Input: points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
Output: 3


Constraints:

n == points.length
2 <= n <= 105
points[i].length == 2
0 <= xi, yi <= 109

Time Complexity:
O(nlog(n)

Space Complexity:
O(1)

"""
from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = sorted([x[0] for x in points])
        return max(points[i + 1] - points[i] for i in range(len(points) - 1))



if __name__ == "__main__":
    solution_instance = Solution()
    s=[[8,7],[9,9],[7,4],[9,7]]

    print(solution_instance.maxWidthOfVerticalArea(s))

""""
Explanation:

The approach involves sorting the x-coordinates and then finding the maximum gap between consecutive x-coordinates. 
This effectively determines the maximum width of the vertical area formed by the points along the x-axis.

Sorting X-coordinates:

    Extract the x-coordinates from the given list of points using a list comprehension: [x[0] for x in points].
    Sort these x-coordinates in ascending order using sorted().
    The sorted list is assigned to the variable points.

Calculating Maximum Gap:

    Iterate through the sorted list of x-coordinates using a generator expression.
    For each pair of consecutive x-coordinates, calculate the difference: points[i + 1] - points[i].
    Use the max() function to find the maximum difference among all consecutive pairs.

Returning Result:

    The calculated maximum difference represents the maximum width of the vertical area along the x-axis.
    Return this maximum width as the final result.

Time Complexity:

    Sorting the x-coordinates in-place using sorted() takes O(n log n) time, where n is the number of points.
    Calculating the differences between consecutive x-coordinates in the sorted list takes O(n) time.
    The max() function also takes O(n) time to find the maximum difference.
    The dominant factor is the sorting operation, so the overall time complexity remains O(n log n).

Space Complexity:

    The space used to store the sorted x-coordinates is O(1) because the sorting is done in-place, 
        and no additional list is created.
    The space used for the generator expression to calculate differences is O(1).
    The space used for variables (e.g., i) and the final result is O(1).

Therefore, with the modification to sort the list in-place, the overall space complexity is reduced to O(1). 
This is an improvement in terms of space efficiency compared to the previous version that created a new list for 
the sorted x-coordinates.
    
"""
