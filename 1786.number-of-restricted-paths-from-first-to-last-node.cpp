/*
 * @lc app=leetcode id=1786 lang=cpp
 *
 * [1786] Number of Restricted Paths From First to Last Node
 */

// @lc code=start
#include<vector>
#include<unordered_map>
#include<queue>
#include<algorithm>
using std::greater;
using std::pair;
using std::priority_queue;
using std::sort;
using std::unordered_map;
using std::vector;
class Solution {
private:
    vector<int> Dijkstra(vector<unordered_map<int, int>>& graph, int n, int source) 
    {
        vector<int> result(n, -1);

        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> heap;
        vector<bool> visited(n, false);
        int visitedCount = 0;
        heap.push({0, source});

        while (!heap.empty() && visitedCount < n) {
            int weight = heap.top().first;
            int node = heap.top().second;
            heap.pop();
            
            if (result[node] < 0) {
                result[node] = weight;
                visited[node] = true;
                visitedCount++;
                for (const auto& neighbor : graph[node]) {
                    int nxt = neighbor.first;
                    int nxtWeight = weight + neighbor.second;
                    heap.push({nxtWeight, nxt});
                }
            }
        }
        return result;
    }
    long long MOD = (long long)1000000007;

public:
    int countRestrictedPaths(int n, vector<vector<int>>& edges) {
        vector<unordered_map<int, int>> graph(n, unordered_map<int, int>{});
        for (vector<int> edge: edges)
        {
            graph[edge[0] - 1][edge[1] - 1] = edge[2];
            graph[edge[1] - 1][edge[0] - 1] = edge[2];            
        }

        vector<int> distanceToLastNode = Dijkstra(graph, n, n - 1);
        vector<pair<int, int>> distanceToLastNodeSorted{};
        for (int i = 0; i < n; i++)
        {
            distanceToLastNodeSorted.push_back(pair<int, int>{distanceToLastNode[i], i});
        }
        sort(distanceToLastNodeSorted.begin(), distanceToLastNodeSorted.end(), greater<pair<int, int>>());

        vector<long long> result(n, (long long)0);
        result[0] += (long long)1;

        int i = 0;
        while (distanceToLastNodeSorted[i].second != 0)
        {
            i++;
        }

        for (int j = i; j < n; j++)
        {
            int node = distanceToLastNodeSorted[j].second;
            int distance = distanceToLastNodeSorted[j].first;

            for (auto it = graph[node].begin(); it != graph[node].end(); it++)
            {
                int nextNode = it->first;
                int nextDistance = distanceToLastNode[nextNode];

                if (nextDistance < distance)
                {
                    result[nextNode] += result[node];
                    result[nextNode] %= MOD;
                }
            }
        }

        return (int)result[n - 1];
    }
};
// @lc code=end