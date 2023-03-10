/*
 * @lc app=leetcode id=382 lang=csharp
 *
 * [382] Linked List Random Node
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

 using System;
public class Solution 
{
    ListNode Head;
    Random autoRand;
    public Solution(ListNode head) 
    {
        Head = head;
        autoRand = new Random();
    }
    
    public int GetRandom() 
    {
        int n = 1;
        int k = 1;
        ListNode node = Head;
        ListNode ans = Head;

        while (node.next != null)
        {
            n++;
            node = node.next;
            if (autoRand.NextDouble() < (double)k / (double)n)
            {
                ans = ans.next;
                k++;
            } 
        }
        return ans.val;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(head);
 * int param_1 = obj.GetRandom();
 */
// @lc code=end

