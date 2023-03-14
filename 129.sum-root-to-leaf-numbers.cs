/*
 * @lc app=leetcode id=129 lang=csharp
 *
 * [129] Sum Root to Leaf Numbers
 */

// @lc code=start
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
    public int SumNumbers(TreeNode root) 
    {
        int result = 0;
        Queue<object[]> queue = new Queue<object[]>();
        queue.Enqueue(new object[2]{root, ""});

        while (queue.TryDequeue(out object[] arr))
        {
            TreeNode node = arr[0] as TreeNode;
            string s = arr[1].ToString();
            if (node.left != null)
            {
                queue.Enqueue(new object[2]{node.left, s + node.val.ToString()});
            }
            if (node.right != null)
            {
                queue.Enqueue(new object[2]{node.right, s + node.val.ToString()});
            }
            if (node.left == null && node.right == null)
            {
                result += Int32.Parse(s + node.val.ToString());
            }
        }    
        return result;
    }
}
// @lc code=end

