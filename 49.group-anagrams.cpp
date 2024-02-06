/*
 * @lc app=leetcode id=49 lang=cpp
 *
 * [49] Group Anagrams
 */

// @lc code=start
#include <vector>
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    std::vector<std::vector<std::string>> groupAnagrams(std::vector<std::string>& strs) {
        std::unordered_map<std::string, std::vector<std::string>> hash_table;

        for (const auto& str : strs) {
            std::string key = str;
            std::sort(key.begin(), key.end());

            if (hash_table.find(key) == hash_table.end()) {
                hash_table[key] = std::vector<std::string>();
            }

            hash_table[key].push_back(str);
        }

        std::vector<std::vector<std::string>> result;
        for (const auto& entry : hash_table) {
            result.push_back(entry.second);
        }

        return result;
    }
};

// @lc code=end

