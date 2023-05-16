/*
 * @lc app=leetcode id=24 lang=csharp
 *
 * [24] Swap Nodes in Pairs
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
    public ListNode SwapPairs(ListNode head) 
    {
        ListNode dummy = new ListNode(-1, head);
        ListNode temp1 = dummy;
        ListNode temp2;
        ListNode temp3;
        while (temp1 != null && temp1.next != null && temp1.next.next != null)
        {
            temp2 = temp1.next;
            temp3 = temp2.next;
            temp1.next = temp3;
            temp2.next = temp3.next;
            temp3.next = temp2;
            temp1 = temp1.next.next;
        }
        return dummy.next;
    }
}
// @lc code=end

