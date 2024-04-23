/*
 * @lc app=leetcode id=2096 lang=csharp
 *
 * [2096] Step-By-Step Directions From a Binary Tree Node to Another
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
    public string GetDirections(TreeNode r, int sV, int dV) {
        StringBuilder sp = new StringBuilder();
        StringBuilder dp = new StringBuilder();
        GetPath(r, sV, ref sp);
        GetPath(r, dV, ref dp);
        string spString = sp.ToString();
        string dpString = dp.ToString();

        int startLevel = spString.Length - 1;
        int destLevel = dpString.Length - 1;
        while (startLevel >= 0 && destLevel >= 0 && spString[startLevel] == dpString[destLevel]){ 
            --startLevel;
            --destLevel;
        }
        
        StringBuilder sb = new StringBuilder();
        for (int i = startLevel; i >= 0; --i) {
            sb.Append('U');
        }
        for (int i = destLevel; i >= 0; --i) {
            sb.Append(dpString[i]);
        }       
        return sb.ToString();
    }
    
    public bool GetPath(TreeNode r, int v, ref StringBuilder p) {
        if (r.val == v) {
            return true;
        } else if (r.left != null && GetPath(r.left, v, ref p)) {
            p.Append("L");
            return true;
        } else if (r.right != null && GetPath(r.right, v, ref p)) {
            p.Append("R");
            return true;
        } else {
            return false;
        }
    }
}
// @lc code=end

