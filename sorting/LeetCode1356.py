"""

Problem:
1356. Sort Integers by The Number of 1 Bits

Link:
https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/description/

Description:
You are given an integer array arr. Sort the integers in the array in ascending order by the number of 1's in their
binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending
order.
Return the array after sorting it.

Example:

Example 1:

Input: arr = [0,1,2,3,4,5,6,7,8]
Output: [0,1,2,4,8,3,5,6,7]
Explantion: [0] is the only integer with 0 bits.
[1,2,4,8] all have 1 bit.
[3,5,6] have 2 bits.
[7] has 3 bits.
The sorted array by bits is [0,1,2,4,8,3,5,6,7]

Example 2:

Input: arr = [1024,512,256,128,64,32,16,8,4,2,1]
Output: [1,2,4,8,16,32,64,128,256,512,1024]
Explantion: All integers have 1 bit in the binary representation, you should just sort them in ascending order.

Constraints:
1 <= arr.length <= 500
0 <= arr[i] <= 104

Time Complexity:
O(log n)

Space Complexity:
O(log n)

"""
from itertools import count
from typing import List

from unicodedata import decimal


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))


if __name__ == "__main__":
    solution_instance = Solution()
    num = [1024,512,256,128,64,32,16,8,4,2,1]
    result = solution_instance.sortByBits(num)
    print(result)

""""
Explanation:

The given code sorts an array of integers based on two criteria:
    The count of set bits (1's) in the binary representation of each integer.
    The numeric value of the integers.
    
sorted(arr, key=lambda x: (x.bit_count(), x)): 
    The sorted function is used to sort the array arr. 
    The key parameter is a lambda function that defines the sorting criteria. 

The lambda function returns a tuple containing two elements:

x.bit_count(): This represents the count of set bits (1's) in the binary representation of the integer x. 
    The bit_count() method is a built-in method in Python that counts the number of set bits.
x: This represents the original numeric value of the integer x.
    By sorting based on the tuple (x.bit_count(), x), the array is first sorted by the count of set bits, and 
    for elements with the same count of set bits, they are further sorted by their numeric value.

"""
