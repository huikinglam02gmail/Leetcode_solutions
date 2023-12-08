/*
 * @lc app=leetcode id=606 lang=cpp
 *
 * [606] Construct String from Binary Tree
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
#include <string>

using namespace std;

class Solution {
public:
    /*
    DFS is called for here.
    Preorder traversal: root -> left -> right    
    */

    string tree2str(TreeNode* root) {
        string result = "";
        if (root) {
            result += to_string(root->val);
            if (root->left || root->right) {
                result += "(" + tree2str(root->left) + ")";
                if (root->right) {
                    result += "(" + tree2str(root->right) + ")";
                }
            }
        }
        return result;
    }
};

// @lc code=end

