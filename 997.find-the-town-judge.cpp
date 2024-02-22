/*
 * @lc app=leetcode id=997 lang=cpp
 *
 * [997] Find the Town Judge
 */

// @lc code=start
#include <vector>
#include <unordered_set>
#include <unordered_map>

class Solution {
public:
    int findJudge(int n, std::vector<std::vector<int>>& trust) {
        if (trust.empty()) {
            if (n == 1) return n;
        } else {
            std::unordered_set<int> hash_source;
            std::unordered_map<int, int> hash_sink;
            for (auto item : trust) {
                hash_source.insert(item[0]);
                if (hash_sink.find(item[1]) == hash_sink.end()) {
                    hash_sink[item[1]] = 0;
                }
                hash_sink[item[1]] += 1;
            }
            for (int i = 1; i <= n; i++) {
                if (hash_source.find(i) == hash_source.end() && hash_sink.find(i) != hash_sink.end() && hash_sink[i] == n - 1) {
                    return i;
                }
            }
        }
        return -1;
    }
};

// @lc code=end

