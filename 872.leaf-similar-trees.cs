/*
 * @lc app=leetcode id=872 lang=csharp
 *
 * [872] Leaf-Similar Trees
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
    public List<int> dfs(TreeNode root)
    {
        List<int> result = new List<int>();
        if (root.left != null)
        {
            result = result.Concat(dfs(root.left)).ToList();
        }
        if (root.right != null)
        {
            result = result.Concat(dfs(root.right)).ToList();
        }
        if (root.left == null && root.right == null)
        {
            result.Add(root.val);
        }
        return result;
    }
    public bool LeafSimilar(TreeNode root1, TreeNode root2) 
    {
        List<int> leafseq1 = dfs(root1);
        List<int> leafseq2 = dfs(root2);
        if (leafseq1.Count != leafseq2.Count)
        {
            return false;
        }
        for (int i = 0; i < leafseq1.Count; i++)
        {
            if (leafseq1[i] != leafseq2[i])
            {
                return false;
            }
        }
        return true;
    }
}
// @lc code=end

