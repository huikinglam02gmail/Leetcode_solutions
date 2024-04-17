/*
 * @lc app=leetcode id=988 lang=cpp
 *
 * [988] Smallest String Starting From Leaf
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
#include <tuple>
#include <algorithm>
#include <string>

using namespace std;

class Solution {
public:
    /*
    BFS from the root
    each time we just add the root val to the left of the string
    When we arrive at a leaf, not node.left and not node.right, we put our result into the bank
    */
    string smallestFromLeaf(TreeNode* root) {
        string result = "";
        queue<pair<TreeNode*, string>> q;
        q.push({root, string(1, 'a' + root->val)});
        while (!q.empty()) {
            auto [node, str] = q.front();
            q.pop();
            if (!node->left && !node->right) {
                if (result.empty()) {
                    result = str;
                } else {
                    result = min(result, str);
                }
            }
            if (node->left) {
                q.push({node->left, char('a' + node->left->val) + str});
            }
            if (node->right) {
                q.push({node->right, char('a' + node->right->val) + str});
            }
        }
        return result;
    }
};
// @lc code=end

