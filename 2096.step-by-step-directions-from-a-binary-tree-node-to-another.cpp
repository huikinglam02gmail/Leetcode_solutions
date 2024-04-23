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
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    string getDirections(TreeNode* r, int sV, int dV) {
        string sp, dp;
        getPath(r, sV, sp);
        getPath(r, dV, dp);
        
        reverse(sp.begin(), sp.end());
        reverse(dp.begin(), dp.end());
        
        while (!sp.empty() && !dp.empty() && sp[0] == dp[0]) {
            sp.erase(sp.begin());
            dp.erase(dp.begin());
        }
        
        for (char& c : sp) {
            if (c == 'L' || c == 'R') c = 'U';
        }
        
        return sp + dp;
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

