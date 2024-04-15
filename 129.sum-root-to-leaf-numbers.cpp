/*
 * @lc app=leetcode id=129 lang=cpp
 *
 * [129] Sum Root to Leaf Numbers
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
#include <queue>
#include <string>

using namespace std;

class Solution {
public:
    int sumNumbers(TreeNode* root) {
        if (!root) return 0;
        int result = 0;
        queue<pair<TreeNode*, string>> q;
        q.push({root, ""});
        while (!q.empty()) {
            auto [node, s] = q.front();
            q.pop();
            if (node->left) {
                q.push({node->left, s + to_string(node->val)});
            }
            if (node->right) {
                q.push({node->right, s + to_string(node->val)});
            }
            if (!node->left && !node->right) {
                result += stoi(s + to_string(node->val));
            }
        }
        return result;
    }
};

// @lc code=end

