/*
 * @lc app=leetcode id=23 lang=csharp
 *
 * [23] Merge k Sorted Lists
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
 using System.Collections.Generic;
public class Solution 
{
    public ListNode MergeKLists(ListNode[] lists) 
    {
        PriorityQueue<ListNode, int> queue = new PriorityQueue<ListNode, int>();

        foreach (ListNode node in lists)
        {
            if (node != null)
            {
                queue.Enqueue(node, node.val);                
            }
        }

        ListNode head = null;
        ListNode temp = null;
        while (queue.TryDequeue(out ListNode node, out int val))
        {
            if (head == null)
            {
                head = node;
                temp = head;
            }
            else
            {
                temp.next = node;
                temp = temp.next;
            }
            if (node.next != null)
            {
                queue.Enqueue(node.next, node.next.val);
            }
        }
        if (temp != null)
        {
            temp.next = null;
        }
        return head;
    }
}
// @lc code=end

