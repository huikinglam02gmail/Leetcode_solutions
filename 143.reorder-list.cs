/*
 * @lc app=leetcode id=143 lang=csharp
 *
 * [143] Reorder List
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

public class Solution {
    /**
     * Use turtle and hare algorithm to find mid point.
     * Reverse the latter half
     * Merge the two LL
     */
    public void ReorderList(ListNode head) {
        if (head == null || head.next == null) return;
        ListNode slow = head;
        ListNode fast = head;
        ListNode sPrev = null;
        while (fast != null && fast.next != null) {
            sPrev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        if (fast != null) {
            sPrev = sPrev.next;
            slow = slow.next;
        }
        sPrev.next = null;
        sPrev = sPrev.next;
        while (slow != null) {
            ListNode sNext = slow.next;
            slow.next = sPrev;
            sPrev = slow;
            slow = sNext;
        }
        ListNode temp1 = head;
        ListNode temp2 = sPrev;
        while (temp1 != null) {
            ListNode temp1Next = temp1.next;
            temp1.next = temp2;
            temp2 = temp1Next;
            temp1 = temp1.next;
        }
    }
}

// @lc code=end

