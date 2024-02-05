/*
 * @lc app=leetcode id=387 lang=cpp
 *
 * [387] First Unique Character in a String
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    int firstUniqChar(std::string s) {
        std::vector<std::vector<int>> hashTable(26, std::vector<int>());
        
        for (int i = 0; i < s.length(); i++) {
            char c = s[i];
            hashTable[c - 'a'].push_back(i);
        }

        std::vector<int> candidates;
        for (int i = 0; i < 26; i++) {
            if (hashTable[i].size() == 1) {
                candidates.push_back(hashTable[i][0]);
            }
        }

        std::sort(candidates.begin(), candidates.end());

        if (candidates.empty()) {
            return -1;
        } else {
            return candidates[0];
        }
    }
};

// @lc code=end

