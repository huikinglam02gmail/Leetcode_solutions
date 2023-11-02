/*
 * @lc app=leetcode id=2265 lang=cpp
 *
 * [2265] Count Nodes Equal to Average of Subtree
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
#include <iostream>
#include <algorithm>

using namespace std;

class Solution {
public:
    int result;

    /*
     * Keep track of subtree sum and number of nodes in subtree.
     */
    pair<int, int> DFS(TreeNode* node) {
        if (!node) {
            return make_pair(0, 0);
        } else {
            pair<int, int> leftData = DFS(node->left);
            pair<int, int> rightData = DFS(node->right);
            int leftSum = leftData.first;
            int leftTotal = leftData.second;
            int rightSum = rightData.first;
            int rightTotal = rightData.second;

            if (node->val == (node->val + leftSum + rightSum) / (1 + leftTotal + rightTotal)) {
                result++;
            }

            return make_pair(node->val + leftSum + rightSum, 1 + leftTotal + rightTotal);
        }
    }

    int averageOfSubtree(TreeNode* root) {
        result = 0;
        DFS(root);
        return result;
    }
};

// @lc code=end

