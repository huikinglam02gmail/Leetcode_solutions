/*
 * @lc app=leetcode id=1601 lang=cpp
 *
 * [1601] Maximum Number of Achievable Transfer Requests
 */

// @lc code=start
#include<vector>
#include<algorithm>
using std::all_of;
using std::max;
using std::vector;
class Solution {
public:
    int maximumRequests(int n, vector<vector<int>>& requests) {
        int result = 0;
        int m = requests.size();
        for (int mask = 0; mask < (1 << m); mask++)
        {
            vector<int> flow (n, 0);
            int count = 0;
            for (int j = 0; j < m; j++)
            {
                if ((mask & (1 << j)) != 0)
                {
                    flow[requests[j][0]]--;
                    flow[requests[j][1]]++;
                    count++;
                }
            }
            if (all_of(flow.begin(), flow.end(), [](int i) { return i == 0; }))
            {
                result = max(result, count);
            }
        }
        return result;           
    }
};
// @lc code=end

