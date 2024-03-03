/*
 * @lc app=leetcode id=3042 lang=cpp
 *
 * [3042] Count Prefix and Suffix Pairs I
 */

// @lc code=start
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    int countPrefixSuffixPairs(vector<string>& words) {
        int n = words.size();
        int result = 0;
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (words[j].find(words[i]) == 0 && words[j].rfind(words[i]) == words[j].size() - words[i].size()) {
                    result++;
                }
            }
        }
        return result;
    }
};

// @lc code=end

