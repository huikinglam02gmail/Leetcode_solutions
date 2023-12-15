/*
 * @lc app=leetcode id=1436 lang=cpp
 *
 * [1436] Destination City
 */

// @lc code=start
#include <unordered_map>
#include <vector>

class Solution {
public:
    // Count outgoing edges
    std::string destCity(std::vector<std::vector<std::string>>& paths) {
        std::unordered_map<std::string, int> outgoing;

        for (const auto& path : paths) {
            const std::string& start = path[0];
            const std::string& end = path[1];

            if (outgoing.find(start) == outgoing.end()) {
                outgoing[start] = 0;
            }

            outgoing[start] += 1;

            if (outgoing.find(end) == outgoing.end()) {
                outgoing[end] = 0;
            }
        }

        for (const auto& pair : outgoing) {
            if (pair.second == 0) {
                return pair.first;
            }
        }

        // Return an empty string if no destination city is found
        return "";
    }
};

// @lc code=end

