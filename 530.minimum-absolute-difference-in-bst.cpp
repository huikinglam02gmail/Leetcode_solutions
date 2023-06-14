/*
 * @lc app=leetcode id=530 lang=cpp
 *
 * [530] Minimum Absolute Difference in BST
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
#include <algorithm>

class Solution 
{
private:
    int min_diff;
    int last_node_val;

    void DFS(TreeNode* root)
    {
        if (root->left != nullptr)
        {
            DFS(root->left);
        }

        min_diff = std::min(min_diff, root -> val - last_node_val);
        last_node_val = root->val;

        if (root -> right != nullptr)
        {
            DFS(root->right);
        }
    }

public:
    int getMinimumDifference(TreeNode* root)
    {
        min_diff = 100001;
        last_node_val = -100001;
        DFS(root);
        return min_diff;
    }
};
// @lc code=end

