/*
 * @lc app=leetcode id=373 lang=cpp
 *
 * [373] Find K Pairs with Smallest Sums
 */

// @lc code=start
#include<vector>
#include<queue>
#include<utility>
#include<unordered_map>
#include<unordered_set>
using std::pair;
using std::priority_queue;
using std::unordered_map;
using std::unordered_set;
using std::vector;
class Solution {
public:
    vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        priority_queue<pair<int, pair<int, int>>> pq{};
        int n1 = nums1.size();
        int n2 = nums2.size();
        unordered_map<int, unordered_set<int>>visited {};

        pq.push({- nums1[0] - nums2[0], {0, 0}});
        visited.insert({0, unordered_set<int>{0}});

        vector<vector<int>> result;
        while (pq.size() > 0 && result.size() < k)
        {
            auto item = pq.top();
            int i = item.second.first;
            int j = item.second.second;
            pq.pop();
            if (i < n1 - 1 && (visited.find(i + 1) == visited.end() || visited[i + 1].find(j) == visited[i + 1].end()))
            {
                pq.push({- nums1[i + 1] - nums2[j], {i + 1, j}});
                if (visited.find(i + 1) == visited.end())
                {
                    visited.insert({i + 1, unordered_set<int>{j}});
                }
                else
                {
                    visited[i + 1].insert(j);
                }
            }
            if (j < n2 - 1 && (visited.find(i) == visited.end() || visited[i].find(j + 1) == visited[i].end()))
            {
                pq.push({- nums1[i] - nums2[j + 1], {i, j + 1}});
                if (visited.find(i) == visited.end())
                {
                    visited.insert({i, unordered_set<int>{j + 1}});
                }
                else
                {
                    visited[i].insert(j + 1);
                }
            }
            result.push_back(vector<int> {nums1[i], nums2[j]});
        }
        return result;
    }
};
// @lc code=end

