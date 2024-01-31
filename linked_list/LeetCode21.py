"""

Problem:

21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

Time Complexity:
O(n+m)

Space Complexity:
O(1)

"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = ListNode(data, self.head)
        self.head = node


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res_head = ListNode()
        res = res_head
        while list1 and list2:
            if list1.val < list2.val:
                res.next, list1 = list1, list1.next
            else:
                res.next, list2 = list2, list2.next
            res = res.next

        res.next = list1 or list2

        return res_head.next


if __name__ == "__main__":
    solution_instance = Solution()
    ll1 = LinkedList()
    ll1.insert_at_beginning(4)
    ll1.insert_at_beginning(2)
    ll1.insert_at_beginning(1)

    ll2 = LinkedList()
    ll2.insert_at_beginning(4)
    ll2.insert_at_beginning(3)
    ll2.insert_at_beginning(1)

    res_ll = solution_instance.mergeTwoLists(ll1.head, ll2.head)

    while res_ll:
        print(res_ll.val, end=" ")
        res_ll = res_ll.next

""""
Explanation:

1. **Initialization:**
   - Create a dummy node (`res_head`) to simplify the code. This dummy node is not part of the final result; 
        it is used to keep track of the head of the merged list.

2. **Comparison and Merging:**
   - Use a `while` loop to iterate as long as both `list1` and `list2` are not exhausted.
   - Inside the loop, compare the values of the current nodes from `list1` and `list2`.
   - If the value in `list1` is smaller, update `res.next` to point to the node from `list1`, and advance the `list1` 
        pointer to the next node.
   - If the value in `list2` is smaller or equal, update `res.next` to point to the node from `list2`, and advance the
        `list2` pointer to the next node.
   - Move the `res` pointer to the newly added node.

3. **Handling Remaining Nodes:**
   - After the loop, check if either `list1` or `list2` still has remaining nodes.
   - If `list1` is not exhausted, append the remaining nodes from `list1` to the merged list.
   - If `list2` is not exhausted, append the remaining nodes from `list2` to the merged list.

4. **Result:**
   - The final merged list is formed, and the head of this list is at `res_head.next`.
   - Return `res_head.next` as the result.

Let's analyze the time and space complexity of the given `mergeTwoLists` function:

**Time Complexity:** - The time complexity is O(n + m), where n is the length of `list1` and m is the length of 
`list2`. - The function iterates through both lists once, and the length of the merged list is the sum of the lengths 
of `list1` and `list2`.

**Space Complexity:**
- The space complexity is O(1) because the function uses a constant amount of extra space regardless of the input size.
- The only additional space used is for the dummy node (`res_head`), the `res` pointer, and a few temporary variables. 
    These consume a constant amount of space, making the space complexity constant.

In summary:
- Time Complexity: O(n + m)
- Space Complexity: O(1)
"""
