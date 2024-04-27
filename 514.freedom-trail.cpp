/*
 * @lc app=leetcode id=514 lang=cpp
 *
 * [514] Freedom Trail
 */

// @lc code=start
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    /*
    Use a hash table to store the indices of characters inside the ring
    Use a 2D vector to store the minimum steps to finish typing the current key
    Enumerate the minimum of all possible steps from different starts to a certain spot
    To go from index i to j, minimum step = min(abs(i - j), l_r - abs)
    */
    int findRotateSteps(string ring, string key) {
        vector<vector<int>> hashRing(26);
        for (int i = 0; i < ring.size(); ++i) {
            hashRing[ring[i] - 'a'].push_back(i);
        }

        int l_r = ring.size();
        vector<vector<int>> steps(key.size(), vector<int>(l_r, INT_MAX));
        vector<int> starts = {0};

        for (int i = 0; i < key.size(); ++i) {
            vector<int> ends = hashRing[key[i] - 'a'];
            for (int end : ends) {
                for (int start : starts) {
                    if (i == 0) {
                        steps[i][end] = min(steps[i][end], 1 + min(abs(start - end), l_r - abs(start - end)));
                    } else {
                        steps[i][end] = min(steps[i][end], steps[i - 1][start] + 1 + min(abs(start - end), l_r - abs(start - end)));
                    }
                }
            }
            starts = ends;
        }

        int minSteps = INT_MAX;
        for (int step : steps[key.size() - 1]) {
            minSteps = min(minSteps, step);
        }
        return minSteps;
    }
};

// @lc code=end

