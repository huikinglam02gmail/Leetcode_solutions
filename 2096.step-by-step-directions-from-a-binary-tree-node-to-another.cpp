/*
 * @lc app=leetcode id=2096 lang=cpp
 *
 * [2096] Step-By-Step Directions From a Binary Tree Node to Another
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
#include <algorithm>

using namespace std;

// Definition for a binary tree node.

class Solution {
public:
    string getDirections(TreeNode* r, int sV, int dV) {
        string sp, dp;
        getPath(r, sV, sp);
        getPath(r, dV, dp);

        int startLevel = sp.length() - 1;
        int destLevel = dp.length() - 1;
        while (startLevel >= 0 && destLevel >= 0 && sp[startLevel] == dp[destLevel]) {
            --startLevel;
            --destLevel;
        }

        string sb(startLevel + 1, 'U');
        for (int i = destLevel; i >= 0; --i) {
            sb += dp[i];
        }
        return sb;
    }
    
    bool getPath(TreeNode* r, int v, string& p) {
        if (r->val == v) {
            return true;
        } else if (r->left != nullptr && getPath(r->left, v, p)) {
            p += 'L';
            return true;
        } else if (r->right != nullptr && getPath(r->right, v, p)) {
            p += 'R';
            return true;
        } else {
            return false;
        }
    }
};


// @lc code=end

