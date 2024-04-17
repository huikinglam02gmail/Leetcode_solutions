/*
 * @lc app=leetcode id=988 lang=csharp
 *
 * [988] Smallest String Starting From Leaf
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
using System.Collections.Generic;

public class Solution {
    /*
    BFS from the root
    each time we just add the root val to the left of the string
    When we arrive at a leaf, not node.left and not node.right, we put our result into the bank
    */
    public string SmallestFromLeaf(TreeNode root) {
        string result = "";
        Queue<Tuple<TreeNode, string>> queue = new Queue<Tuple<TreeNode, string>>();
        queue.Enqueue(new Tuple<TreeNode, string>(root, Convert.ToChar(root.val + 'a').ToString()));
        while (queue.Count > 0) {
            var tuple = queue.Dequeue();
            TreeNode node = tuple.Item1;
            string str = tuple.Item2;
            if (node.left == null && node.right == null) {
                if (result.Length == 0) {
                    result = str;
                } else {
                    result = string.Compare(result, str) < 0 ? result : str;
                }
            }
            if (node.left != null) {
                queue.Enqueue(new Tuple<TreeNode, string>(node.left, Convert.ToChar(node.left.val + 'a') + str));
            }
            if (node.right != null) {
                queue.Enqueue(new Tuple<TreeNode, string>(node.right, Convert.ToChar(node.right.val + 'a') + str));
            }
        }
        return result;
    }
}

// @lc code=end

