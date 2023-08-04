/*
 * @lc app=leetcode id=139 lang=cpp
 *
 * [139] Word Break
 */

// @lc code=start
#include <iostream>
#include <vector>
#include <unordered_set>
#include <queue>

class Solution {
public:
    bool wordBreak(std::string s, std::vector<std::string>& wordDict) {
        std::queue<std::string> q;
        std::unordered_set<std::string> seen;
        q.push(s);
        seen.insert(s);
        while (!q.empty()) {
            s = q.front();
            q.pop();
            for (const std::string& word : wordDict) {
                if (s.find(word) == 0) {
                    std::string new_s = s.substr(word.length());
                    if (new_s.empty()) {
                        return true;
                    }
                    if (seen.find(new_s) == seen.end()) {
                        q.push(new_s);
                        seen.insert(new_s);
                    }
                }
            }
        }
        return false;
    }
};

// @lc code=end

