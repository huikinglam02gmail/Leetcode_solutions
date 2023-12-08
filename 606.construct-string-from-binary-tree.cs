/*
 * @lc app=leetcode id=606 lang=csharp
 *
 * [606] Construct String from Binary Tree
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
using System;

public class Solution
{
    /*
    DFS is called for here.
    Preorder traversal: root -> left -> right    
    */

    public string Tree2str(TreeNode root)
    {
        string result = "";
        if (root != null)
        {
            result += root.val.ToString();
            if (root.left != null || root.right != null)
            {
                result += "(" + Tree2str(root.left) + ")";
                if (root.right != null)
                {
                    result += "(" + Tree2str(root.right) + ")";
                }
            }
        }
        return result;
    }
}

// @lc code=end

