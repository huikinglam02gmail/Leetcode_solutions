/*
 * @lc app=leetcode id=92 lang=csharp
 *
 * [92] Reverse Linked List II
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val = 0, ListNode next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

public class Solution {
    public ListNode ReverseBetween(ListNode head, int left, int right) {
        int i = 1;
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        ListNode prev = dummy;
        ListNode temp = head;
        ListNode start = null;
        Stack<ListNode> stack = new Stack<ListNode>();

        while (temp != null) {
            if (left <= i && i <= right) {
                stack.Push(temp);
            }
            if (i == left) {
                start = prev;
            }
            prev = prev.next;
            temp = temp.next;
            i++;
        }

        ListNode last = (stack.Count > 0) ? stack.Peek().next : null;

        while (stack.Count > 0) {
            start.next = stack.Pop();
            start = start.next;
        }

        start.next = last;

        return dummy.next;
    }
}

// @lc code=end

