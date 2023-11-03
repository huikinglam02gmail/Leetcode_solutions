/*
 * @lc app=leetcode id=1441 lang=cpp
 *
 * [1441] Build an Array With Stack Operations
 */

// @lc code=start
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) {
        vector<string> result;
        int j = 0;
        for (int i = 1; i <= n; i++) {
            result.push_back("Push");
            if (i == target[j]) {
                j++;
            } else {
                result.push_back("Pop");
            }
            if (j == target.size()) {
                return result;
            }
        }
        return result;
    }
};

// @lc code=end

