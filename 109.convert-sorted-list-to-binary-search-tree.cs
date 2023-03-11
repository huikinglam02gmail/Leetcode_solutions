/*
 * @lc app=leetcode id=109 lang=csharp
 *
 * [109] Convert Sorted List to Binary Search Tree
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
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
 using System.Collections.Generic;
public class Solution 
{
    public TreeNode generate(List<int> arr)
    {
        TreeNode root = null;
        if (arr.Count > 0)
        {
            int left = 0;
            int right = arr.Count - 1;
            int mid = (left + right) / 2;
            root = new TreeNode(arr[mid]);
            root.left = generate(arr.GetRange(0, mid));
            root.right = generate(arr.GetRange(mid + 1, arr.Count - mid - 1));
        }
        return root;
    }
    public TreeNode SortedListToBST(ListNode head) 
    {
        List<int> result = new List<int>();
        ListNode temp = head;
        while (temp != null)
        {
            result.Add(temp.val);
            temp = temp.next;
        }
        return generate(result);
    }
}
// @lc code=end

