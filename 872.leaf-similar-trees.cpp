/*
 * @lc app=leetcode id=872 lang=cpp
 *
 * [872] Leaf-Similar Trees
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
#include <vector>

class Solution {
public:
    std::vector<int> dfs(TreeNode* root) {
        std::vector<int> result;
        if (root->left) {
            auto left_result = dfs(root->left);
            result.insert(result.end(), left_result.begin(), left_result.end());
        }
        if (root->right) {
            auto right_result = dfs(root->right);
            result.insert(result.end(), right_result.begin(), right_result.end());
        }
        if (!root->left && !root->right) {
            result.push_back(root->val);
        }
        return result;
    }

    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        std::vector<int> leafseq1 = dfs(root1);
        std::vector<int> leafseq2 = dfs(root2);

        if (leafseq1.size() != leafseq2.size()) {
            return false;
        }

        for (size_t i = 0; i < leafseq1.size(); ++i) {
            if (leafseq1[i] != leafseq2[i]) {
                return false;
            }
        }

        return true;
    }
};

// @lc code=end

