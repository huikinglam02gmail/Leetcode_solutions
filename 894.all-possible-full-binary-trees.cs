/*
 * @lc app=leetcode id=894 lang=csharp
 *
 * [894] All Possible Full Binary Trees
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
    /*
    If n is even, it's just impossible.
    If n is odd, we can use dynamic programming to solve:
    A Full Binary Tree (FBT) with n nodes must be a node with children being 1 + (n-2) or (n-2) + 1, add odd pairs upwards.
    */
    public IList<TreeNode> AllPossibleFBT(int n) {
        List<TreeNode>[] result = new List<TreeNode>[n + 1];
        for (int i = 0; i <= n; i++) {
            result[i] = new List<TreeNode>();
        }
        
        for (int i = 1; i <= n; i += 2) {
            if (i == 1) {
                result[i].Add(new TreeNode(0));
            } else {
                for (int j = 1; j < i; j += 2) {
                    foreach (TreeNode leftNode in result[j]) {
                        foreach (TreeNode rightNode in result[i - j - 1]) {
                            TreeNode root = new TreeNode(0);
                            root.left = leftNode;
                            root.right = rightNode;
                            result[i].Add(root);
                        }
                    }
                }
            }
        }
        
        return result[n];
    }
}
// @lc code=end

