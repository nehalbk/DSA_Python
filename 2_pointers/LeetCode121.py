"""

Problem:
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104

Time Complexity:
O(n)

Space Complexity:
O(1)

"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        maxProf = 0

        while r < len(prices):
            if prices[l]<prices[r]:
                maxProf=max(maxProf,prices[r]-prices[l])
            else:
                l=r
            r+=1
        return maxProf



if __name__ == "__main__":
    solution_instance = Solution()
    prices = [7,6,4,3,1]

    print(solution_instance.maxProfit(prices))

""""
Explanation:

1. Initialization:

    i is the pointer for the last element in nums1.
    j is the pointer for the last element in nums2.
    k is the pointer for the position in the merged result array (nums1).

2. Merging in Reverse Order:

    We start from the end of both arrays-lists (nums1 and nums2) and compare elements.
    The larger element is placed at the end of the merged array (nums1).
    We move the pointers accordingly.

3. Copying Remaining Elements:

    After merging, if there are remaining elements in nums2, we copy them to the merged array (nums1).
    We continue updating pointers and copying until both arrays-lists are fully merged.
    
"""
