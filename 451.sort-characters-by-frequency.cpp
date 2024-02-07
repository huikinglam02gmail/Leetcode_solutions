/*
 * @lc app=leetcode id=451 lang=cpp
 *
 * [451] Sort Characters By Frequency
 */

// @lc code=start
#include <string>
#include <unordered_map>
#include <vector>
#include <algorithm>

class Solution {
public:
    std::string frequencySort(std::string s) {
        std::unordered_map<char, int> hashTable;

        for (char c : s) {
            hashTable[c]++;
        }

        std::vector<std::pair<char, int>> frequencies(hashTable.begin(), hashTable.end());
        std::sort(frequencies.begin(), frequencies.end(), [](const auto& a, const auto& b) {
            return a.second > b.second;
        });

        std::string result;
        for (const auto& p : frequencies) {
            result += std::string(p.second, p.first);
        }

        return result;
    }
};

// @lc code=end

