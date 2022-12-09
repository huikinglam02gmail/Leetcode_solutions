/*
 * @lc app=leetcode id=1026 lang=csharp
 *
 * [1026] Maximum Difference Between Node and Ancestor
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
    int ans = 0;
    public int[] dfs(TreeNode root)
    {
        int[] result = new int[2] {root.val, root.val};
        if (root.left != null)
        {
            int[] resultLeft = dfs(root.left);
            ans = Math.Max(ans, Math.Abs(root.val - resultLeft[0]));
            ans = Math.Max(ans, Math.Abs(root.val - resultLeft[1]));
            result[0] = Math.Min(result[0], resultLeft[0]);
            result[1] = Math.Max(result[1], resultLeft[1]);
        }
        if (root.right != null)
        {
            int[] resultRight = dfs(root.right);
            ans = Math.Max(ans, Math.Abs(root.val - resultRight[0]));
            ans = Math.Max(ans, Math.Abs(root.val - resultRight[1]));
            result[0] = Math.Min(result[0], resultRight[0]);
            result[1] = Math.Max(result[1], resultRight[1]);
        }
        return result;
    }
    public int MaxAncestorDiff(TreeNode root) 
    {
        int[] resultRoot = dfs(root);
        return ans;
    }
}
// @lc code=end

