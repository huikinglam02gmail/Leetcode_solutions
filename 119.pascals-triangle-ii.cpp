/*
 * @lc app=leetcode id=119 lang=cpp
 *
 * [119] Pascal's Triangle II
 */

// @lc code=start
/**
 * @lc app=leetcode id=119 lang=cpp
 *
 * [119] Pascal's Triangle II
 */

#include <vector>
using namespace std;

class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> curr(1, 1);
        int i = 0;
        while (i < rowIndex) {
            vector<int> nxt(1, 1);
            for (int j = 0; j < curr.size() - 1; j++) {
                nxt.push_back(curr[j] + curr[j + 1]);
            }
            nxt.push_back(1);
            curr = nxt;
            i++;
        }
        return curr;
    }
};

// @lc code=end

