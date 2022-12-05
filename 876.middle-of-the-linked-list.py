#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # turtle and hare algorithm will find the mid point perfectly
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next
            fast = fast.next
            slow = slow.next
            
        if not fast.next:
            return slow
        elif fast.next and not fast.next.next:
            return slow.next
# @lc code=end

