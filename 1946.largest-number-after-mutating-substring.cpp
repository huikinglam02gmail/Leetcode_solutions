/*
 * @lc app=leetcode id=1946 lang=cpp
 *
 * [1946] Largest Number After Mutating Substring
 */

// @lc code=start
/**
 * @lc app=leetcode id=1946 lang=cpp
 *
 * [1946] Largest Number After Mutating Substring
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string maximumNumber(string num, vector<int>& change) {
        int n = num.size();
        vector<char> newNum(num.begin(), num.end());

        for (int i = 0; i < n; i++) {
            int j = i;
            if (newNum[j] < change[newNum[j] - '0'] + '0') {
                while (j < n && newNum[j] <= change[newNum[j] - '0'] + '0') {
                    newNum[j] = change[newNum[j] - '0'] + '0';
                    j++;
                }
            }
            if (j > i) {
                return string(newNum.begin(), newNum.end());
            }
        }

        return num;
    }
};

// @lc code=end

