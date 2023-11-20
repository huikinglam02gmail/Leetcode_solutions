/*
 * @lc app=leetcode id=2391 lang=cpp
 *
 * [2391] Minimum Amount of Time to Collect Garbage
 */

// @lc code=start
#include <vector>
#include <unordered_map>

class Solution {
public:
    int garbageCollection(std::vector<std::string>& garbage, std::vector<int>& travel) {
        std::unordered_map<char, std::vector<int>> hashTable = {
            { 'M', std::vector<int>() },
            { 'P', std::vector<int>() },
            { 'G', std::vector<int>() }
        };

        for (int i = 0; i < garbage.size(); i++) {
            for (char c : garbage[i]) {
                hashTable[c].push_back(i);
            }
        }

        std::vector<int> prefix(1, 0);
        prefix.insert(prefix.end(), travel.begin(), travel.end());

        for (int i = 1; i < prefix.size(); i++) {
            prefix[i] += prefix[i - 1];
        }

        int result = 0;

        for (const auto& route : hashTable) {
            for (int i = 0; i < route.second.size(); i++) {
                result += 1 + prefix[route.second[i]] - prefix[i == 0 ? 0 : route.second[i - 1]];
            }
        }

        return result;
    }
};

// @lc code=end

