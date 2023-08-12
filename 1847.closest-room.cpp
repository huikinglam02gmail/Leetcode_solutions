/*
 * @lc app=leetcode id=1847 lang=cpp
 *
 * [1847] Closest Room
 */

// @lc code=start
#include <vector>
#include <set>
#include <algorithm>

class Solution {
public:
    std::vector<int> closestRoom(std::vector<std::vector<int>>& rooms, std::vector<std::vector<int>>& queries) {
        std::vector<std::vector<int>> sortedQueries;
        for (int i = 0; i < queries.size(); i++) {
            sortedQueries.push_back({ queries[i][1], queries[i][0], i });
        }
        std::sort(sortedQueries.begin(), sortedQueries.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
            return a[0] > b[0];
        });

        int notYetInserted = 0;
        std::sort(rooms.begin(), rooms.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
            return a[1] > b[1];
        });

        std::set<int> tree;
        std::vector<int> result(queries.size(), -1);

        for (const auto& query : sortedQueries) {
            int minSize = query[0];
            int preferred = query[1];
            int ind = query[2];

            while (notYetInserted < rooms.size() && rooms[notYetInserted][1] >= minSize) {
                tree.insert(rooms[notYetInserted][0]);
                notYetInserted++;
            }

            if (!tree.empty()) {
                auto bisectLeftIt = tree.lower_bound(preferred);
                std::vector<std::pair<int, int>> alternatives;

                if (bisectLeftIt != tree.end()) {
                    alternatives.push_back({ abs(preferred - *bisectLeftIt), *bisectLeftIt });
                }

                if (bisectLeftIt != tree.begin()) {
                    bisectLeftIt--;
                    alternatives.push_back({ abs(preferred - *bisectLeftIt), *bisectLeftIt });
                }

                if (!alternatives.empty()) {
                    std::sort(alternatives.begin(), alternatives.end());
                    result[ind] = alternatives[0].second;
                }
            }
        }

        return result;
    }
};
// @lc code=end

