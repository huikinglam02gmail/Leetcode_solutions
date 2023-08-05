/*
 * @lc app=leetcode id=95 lang=csharp
 *
 * [95] Unique Binary Search Trees II
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
    public List<TreeNode> ConstructTrees(int start, int end) {
        List<TreeNode> list = new List<TreeNode>();

        if (start > end) {
            list.Add(null);
            return list;
        }

        for (int i = start; i <= end; i++) {
            List<TreeNode> leftSubtree = ConstructTrees(start, i - 1);
            List<TreeNode> rightSubtree = ConstructTrees(i + 1, end);

            foreach (TreeNode left in leftSubtree) {
                foreach (TreeNode right in rightSubtree) {
                    TreeNode node = new TreeNode(i);
                    node.left = left;
                    node.right = right;
                    list.Add(node);
                }
            }
        }
        return list;
    }

    public IList<TreeNode> GenerateTrees(int n) {
        return ConstructTrees(1, n);
    }
}

// @lc code=end

