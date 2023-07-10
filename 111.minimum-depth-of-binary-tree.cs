/*
 * @lc app=leetcode id=111 lang=csharp
 *
 * [111] Minimum Depth of Binary Tree
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
public class Solution {
    public int MinDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        
        Queue<TreeNode> queue = new Queue<TreeNode>();
        queue.Enqueue(root);
        int steps = 1;
        
        while (queue.Count > 0) {
            int levelSize = queue.Count;
            
            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.Dequeue();
                
                if (node.left == null && node.right == null) {
                    return steps;
                }
                
                if (node.left != null) {
                    queue.Enqueue(node.left);
                }
                
                if (node.right != null) {
                    queue.Enqueue(node.right);
                }
            }
            
            steps++;
        }
        
        return -1;
    }
}
// @lc code=end

