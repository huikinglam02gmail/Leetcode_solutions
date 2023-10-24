/*
 * @lc app=leetcode id=515 lang=csharp
 *
 * [515] Find Largest Value in Each Tree Row
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode() {}
 *     public TreeNode(int val) { this.val = val; }
 *     public TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

public class Solution {
    public IList<int> LargestValues(TreeNode root) {
        // Use BFS to find max level by level
        List<int> result = new List<int>();
        Queue<TreeNode> queue = new Queue<TreeNode>();
        if (root != null) {
            queue.Enqueue(root);
        }
        
        while (queue.Count > 0) {
            int currentMax = int.MinValue;
            int levelSize = queue.Count;
            
            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.Dequeue();
                currentMax = Math.Max(currentMax, node.val);
                
                if (node.left != null) {
                    queue.Enqueue(node.left);
                }
                if (node.right != null) {
                    queue.Enqueue(node.right);
                }
            }
            
            result.Add(currentMax);
        }
        
        return result;
    }
}

// @lc code=end

