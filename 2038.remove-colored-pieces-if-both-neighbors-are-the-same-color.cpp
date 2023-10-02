/*
 * @lc app=leetcode id=2038 lang=cpp
 *
 * [2038] Remove Colored Pieces if Both Neighbors are the Same Color
 */

// @lc code=start
#include <vector>
#include <algorithm>
#include <string>

class Solution {
public:
    bool winnerOfGame(std::string colors) {
        colors = 'C' + colors + 'C';
        std::vector<int> count(2, 0);
        int consec = 0;
        char last = ' ';

        for (char color : colors) {
            if (color != last) {
                if (last == 'A') {
                    count[0] -= std::min(consec, 2);
                }
                else if (last == 'B') {
                    count[1] -= std::min(consec, 2);
                }
                consec = 1;
            }
            else {
                consec++;
            }

            if (color == 'A') {
                count[0]++;
            }
            else if (color == 'B') {
                count[1]++;
            }

            last = color;
        }

        return count[0] > count[1];
    }
};
// @lc code=end

