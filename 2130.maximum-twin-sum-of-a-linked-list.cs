/*
 * @lc app=leetcode id=2130 lang=csharp
 *
 * [2130] Maximum Twin Sum of a Linked List
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
    public int PairSum(ListNode head) 
    {
        List<int> arr = new List<int>();
        ListNode temp = head;
        while (temp != null)
        {
            arr.Add(temp.val);
            temp = temp.next;
        }
        int n = arr.Count;
        int result = 0;
        for (int i = 0; i < n / 2; i++)
        {
            result = Math.Max(result, arr[i] + arr[n - 1 - i]);
        }
        return result;
    }
}
// @lc code=end

