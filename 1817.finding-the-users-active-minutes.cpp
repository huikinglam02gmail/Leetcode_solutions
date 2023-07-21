/*
 * @lc app=leetcode id=1817 lang=cpp
 *
 * [1817] Finding the Users Active Minutes
 */

// @lc code=start
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>

class Solution {
public:
    /*
     * Very easy: just use an unordered_map <id, unordered_set>. Return the histogram of size.
     */
    std::vector<int> findingUsersActiveMinutes(std::vector<std::vector<int>>& logs, int k) {
        std::unordered_map<int, std::unordered_set<int>> hashTable;
        for (const auto& log : logs) {
            int id = log[0];
            int time = log[1];
            hashTable[id].insert(time);
        }

        std::vector<int> result(k, 0);
        for (const auto& valueSet : hashTable) {
            result[valueSet.second.size() - 1]++;
        }

        return result;
    }
};

// @lc code=end

