/*
 * @lc app=leetcode id=239 lang=cpp
 *
 * [239] Sliding Window Maximum
 */

// @lc code=start
#include <queue>
#include <vector>
#include <utility>
using std::make_pair;
using std::pair;
using std::priority_queue;
using std::vector;

class Solution {
/*
Use a max heap to maintain the elements and index.
*/
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        priority_queue<pair<int, int>> pq{};
        for (int i = 0; i < k; i++)
        {
            pq.push(make_pair(nums[i], i));
        }

        vector<int> result{pq.top().first};
        for (int i = k; i < nums.size(); i++)
        {
            pq.push(make_pair(nums[i], i));
            while (pq.top().second <= i - k)
            {
                pq.pop();
            }
            result.push_back(pq.top().first);
        }
        return result;
    }
};
// @lc code=end

