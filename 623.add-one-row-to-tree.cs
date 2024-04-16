/*
 * @lc app=leetcode id=623 lang=csharp
 *
 * [623] Add One Row to Tree
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

public class Solution {
    public TreeNode AddOneRow(TreeNode root, int val, int depth) {
        if (depth == 1) return new TreeNode(val, root, null);
        
        Queue<TreeNode> queue = new Queue<TreeNode>();
        int currentDepth = 1;
        queue.Enqueue(root);
        
        while (currentDepth < depth) {
            currentDepth++;
            int levelSize = queue.Count;
            
            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.Dequeue();
                
                if (currentDepth == depth) {
                    TreeNode leftNode = node.left;
                    TreeNode rightNode = node.right;
                    node.left = new TreeNode(val, leftNode, null);
                    node.right = new TreeNode(val, null, rightNode);
                } else {
                    if (node.left != null)
                        queue.Enqueue(node.left);
                    if (node.right != null)
                        queue.Enqueue(node.right);
                }
            }
        }
        
        return root;
    }
}

// @lc code=end

