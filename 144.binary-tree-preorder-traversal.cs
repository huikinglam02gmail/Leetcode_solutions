/*
 * @lc app=leetcode id=144 lang=csharp
 *
 * [144] Binary Tree Preorder Traversal
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
public class Solution 
{
    public IList<int> PreorderTraversal(TreeNode root) 
    {
        return dfs(root);
    }
    public List<int> dfs(TreeNode node)
    {
        List<int> result = new List<int>();
        if (node != null)
        {
            result.Add(node.val);
            result.AddRange(dfs(node.left));
            result.AddRange(dfs(node.right));
        }
        return result;
    }
}
// @lc code=end
