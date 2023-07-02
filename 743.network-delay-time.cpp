/*
 * @lc app=leetcode id=743 lang=cpp
 *
 * [743] Network Delay Time
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
class Solution
{
private:
    vector<unordered_map<int, int>> graph;
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
            
            result[node] = weight;
            
            if (!visited[node]) {
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

public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        graph.resize(n, unordered_map<int, int>());
        for (vector<int> time : times)
        {
            graph[time[0] - 1].insert({time[1] - 1, time[2]});
        }
        vector<int> result = Dijkstra(graph, n, k - 1);
        sort(result.begin(), result.end());
        return result[0] == -1 ? -1 : result.back();
    }
};
// @lc code=end

