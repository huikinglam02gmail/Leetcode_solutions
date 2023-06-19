/*
 * @lc app=leetcode id=1766 lang=cpp
 *
 * [1766] Tree of Coprimes
 */

// @lc code=start
#include<vector>
#include<unordered_map>
#include<unordered_set>
#include<numeric>
using std::gcd;
using std::unordered_map;
using std::unordered_set;
using std::vector;
class Solution {
private:
    unordered_map<int, vector<vector<int>>> numSeen{};
    unordered_set<int> onPath{};
    vector<unordered_set<int>> coPrimes;
    vector<unordered_set<int>> graph;
    vector<int> Nums;
    vector<int> result;
    void DFS(int node, int steps)
    {
        int lastIndex = -1;
        int minDist = INT_MAX;
        for (int cop : coPrimes[Nums[node]])
        {
            if (numSeen.find(cop) != numSeen.end() && numSeen[cop].size() > 0 && steps - numSeen[cop].back().back() < minDist)
            {
                minDist = steps - numSeen[cop].back().back();
                lastIndex = numSeen[cop].back().front();
            }
        }

        result[node] = lastIndex;
        onPath.insert(node);

        if (numSeen.find(Nums[node]) == numSeen.end())
        {
            numSeen[Nums[node]] = vector<vector<int>>{};
        }

        numSeen[Nums[node]].push_back(vector<int> { node, steps });

        for (int nxt : graph[node])
        {
            if (onPath.find(nxt) == onPath.end())
            {
                DFS(nxt, steps + 1);
            }
        }

        onPath.erase(node);
        numSeen[Nums[node]].pop_back();
    }
public:
    vector<int> getCoprimes(vector<int>& nums, vector<vector<int>>& edges) {
        Nums = nums;
        coPrimes.resize(51, unordered_set<int>{});
        for (int i = 1; i <= 50; i++)
        {
            for (int j = i; j <= 50; j++)
            {
                if (gcd(i, j) == 1)
                {
                    coPrimes[i].insert(j);
                    coPrimes[j].insert(i);
                }
            }
        }

        graph.resize(nums.size(), unordered_set<int>{});
        for (auto edge : edges)
        {
            int a = edge[0];
            int b = edge[1];
            graph[a].insert(b);
            graph[b].insert(a);
        }

        result.resize(nums.size(), -1);
        DFS(0, 0);
        return result;
    }
};
// @lc code=end

