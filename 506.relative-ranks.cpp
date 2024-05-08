/*
 * @lc app=leetcode id=506 lang=cpp
 *
 * [506] Relative Ranks
 */

// @lc code=start
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& score) {
        vector<vector<int>> data;
        for (int i = 0; i < score.size(); i++) {
            data.push_back({ score[i], i });
        }
        sort(data.begin(), data.end(), [](const vector<int>& x, const vector<int>& y) {
            return y[0] < x[0];
        });
        int n = score.size();
        vector<string> result(n);
        for (int i = 0; i < n; i++) {
            if (i == 0) result[data[i][1]] = "Gold Medal";
            else if (i == 1) result[data[i][1]] = "Silver Medal";
            else if (i == 2) result[data[i][1]] = "Bronze Medal";
            else result[data[i][1]] = to_string(i + 1);
        }
        return result;
    }
};

// @lc code=end

