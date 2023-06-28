/*
 * @lc app=leetcode id=1782 lang=cpp
 *
 * [1782] Count Pairs Of Nodes
 */

// @lc code=start
#include<vector>
#include<unordered_map>
#include<algorithm>
using std::max;
using std::min;
using std::sort;
using std::unordered_map;
using std::vector;
class Solution {
public:
    vector<int> countPairs(int n, vector<vector<int>>& edges, vector<int>& queries) {
        vector<int> count(n, 0);
        unordered_map<int, unordered_map<int, int>> edgeCount{};
        for (vector<int> edge : edges)
        {
            int a = min(edge[0], edge[1]) - 1;
            int b = max(edge[0], edge[1]) - 1;
            count[a]++;
            count[b]++;
            if (edgeCount.find(a) == edgeCount.end())
            {
                edgeCount.insert({a, unordered_map<int, int>{}});
            }
            if (edgeCount[a].find(b) == edgeCount[a].end())
            {
                edgeCount[a].insert({b, 0});
            }
            edgeCount[a][b]++;
        }

        vector<int> sortedCount(count);
        sort(sortedCount.begin(), sortedCount.end());
        vector<int> result {};
        for (int q : queries)
        {
            int l = 0;
            int r = n - 1;
            int res = 0;
            while (l < r)
            {
                if (sortedCount[l] + sortedCount[r] <= q)
                {
                    l++;
                }
                else
                {
                    res += r - l;
                    r--;
                }
            }

            for (auto p1 : edgeCount)
            {
                for (auto p2 : p1.second)
                {
                    if (count[p1.first] + count[p2.first] > q && count[p1.first] + count[p2.first] <= q + p2.second)
                    {
                        res--;
                    }
                }
            }
            result.push_back(res);
        }
        return result;
    }
};
// @lc code=end

