/*
 * @lc app=leetcode id=1325 lang=cpp
 *
 * [1325] Delete Leaves With a Given Value
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
class Solution {
public:
    // Helper method to perform DFS and remove leaf nodes with the target value
    TreeNode* dfs(TreeNode* node, int target) {
        if (!node) {
            return nullptr;
        }

        node->left = dfs(node->left, target);
        node->right = dfs(node->right, target);

        if (!node->left && !node->right && node->val == target) {
            return nullptr;
        } else {
            return node;
        }
    }

    TreeNode* removeLeafNodes(TreeNode* root, int target) {
        return dfs(root, target);
    }
};

// @lc code=end

