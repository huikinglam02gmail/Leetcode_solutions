/*
 * @lc app=leetcode id=894 lang=cpp
 *
 * [894] All Possible Full Binary Trees
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
#include<vector>
using std::vector;
class Solution {
public:
    /*
    If n is even, it's just impossible.
    If n is odd, we can use dynamic programming to solve:
    A Full Binary Tree (FBT) with n nodes must be a node with children being 1 + (n-2) or (n-2) + 1, add odd pairs upwards.
    */
    std::vector<TreeNode*> allPossibleFBT(int n) {
        std::vector<TreeNode*> result[n + 1];
        
        for (int i = 0; i <= n; i++) {
            result[i] = std::vector<TreeNode*>();
        }
        
        for (int i = 1; i <= n; i += 2) {
            if (i == 1) {
                result[i].push_back(new TreeNode(0));
            } else {
                for (int j = 1; j < i; j += 2) {
                    for (TreeNode* leftNode : result[j]) {
                        for (TreeNode* rightNode : result[i - j - 1]) {
                            TreeNode* root = new TreeNode(0);
                            root->left = leftNode;
                            root->right = rightNode;
                            result[i].push_back(root);
                        }
                    }
                }
            }
        }
        
        return result[n];
    }
};
// @lc code=end

