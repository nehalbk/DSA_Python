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

1. Initialize two pointers, l and r, to the first and second elements of the prices array.
2. Initialize maxProf to 0 to store the maximum profit.
3. Iterate through the prices array using the while loop.
4. If the price at l is less than the price at r, calculate the profit by selling at r and buying at l. 
    Update maxProf with the maximum of its current value and the calculated profit.
5. If the price at l is greater than or equal to the price at r, update the left pointer l to be equal to r. 
    This resets the potential buying position.
6. Move the right pointer r to the next index.
7. After the loop, return the maximum profit stored in maxProf.

The algorithm efficiently determines the maximum profit by maintaining a potential buying position and adjusting it 
based on potential selling positions. The time complexity is O(n), where n is the length of the prices array, as the 
algorithm iterates through the array once.
    
"""
