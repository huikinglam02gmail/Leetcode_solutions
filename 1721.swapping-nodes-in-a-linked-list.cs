/*
 * @lc app=leetcode id=1721 lang=csharp
 *
 * [1721] Swapping Nodes in a Linked List
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
    public ListNode SwapNodes(ListNode head, int k) 
    {
        int n = 0;
        ListNode temp = head;
        while (temp != null)
        {
            n++;
            temp = temp.next;
        }
        ListNode i = null;
        ListNode j = null;
        temp = head;
        int count = 0;
        while (temp != null)
        {
            count++;
            if (count == k)
            {
                i = temp;
            }
            if (count == n + 1 - k)
            {
                j = temp;
            }
            temp = temp.next;
        }
        int val = i.val;
        i.val = j.val;
        j.val = val;
        return head;
    }
}
// @lc code=end

