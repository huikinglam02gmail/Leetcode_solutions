/*
 * @lc app=leetcode id=1326 lang=cpp
 *
 * [1326] Minimum Number of Taps to Open to Water a Garden
 */

// @lc code=start
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minTaps(int n, vector<int>& ranges) {
        vector<pair<int, int>> candidates;
        for (int i = 0; i < ranges.size(); ++i) {
            candidates.push_back(make_pair(i - ranges[i], i + ranges[i]));
        }
        sort(candidates.begin(), candidates.end());

        int result = 0, cur = 0, i = 0;
        priority_queue<int> heap;
        
        while (cur < n) {
            while (i < candidates.size() && cur >= candidates[i].first) {
                heap.push(candidates[i].second);
                ++i;
            }
            if (!heap.empty() && heap.top() > cur) {
                cur = heap.top();
                heap.pop();
                ++result;
            } else {
                return -1;
            }
        }
        return result;
    }
};
// @lc code=end

