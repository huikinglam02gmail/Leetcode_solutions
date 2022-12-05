/*
 * @lc app=leetcode id=876 lang=csharp
 *
 * [876] Middle of the Linked List
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
public class Solution 
{
    public ListNode MiddleNode(ListNode head) 
    {
        ListNode fast = head;
        ListNode slow = head;
        while (fast.next != null && fast.next.next != null)
        {
            fast = fast.next.next;
            slow = slow.next;
        }
        if (fast.next == null)
        {
            return slow;
        }
        else if (fast.next != null && fast.next.next == null)
        {
            return slow.next;
        }
        else
        {
            return slow;
        }
    }
}
// @lc code=end

