/*
 * @lc app=leetcode id=1976 lang=cpp
 *
 * [1976] Number of Ways to Arrive at Destination
 */

// @lc code=start
#include <vector>
#include <queue>
#include <unordered_map>
#include <tuple>

using std::get;
using std::greater;
using std::make_tuple;
using std::pair;
using std::priority_queue;
using std::tuple;
using std::unordered_map;
using std::vector;

class Solution {
private:
    const long long MOD = 1000000007;
    vector<unordered_map<int, int>> graph;
    vector<long long> dp;
    priority_queue<tuple<long long, int, long long>, vector<tuple<long long, int, long long>>, greater<>> pq{};
public:
    int countPaths(int n, std::vector<std::vector<int>>& roads) {
        graph = vector<unordered_map<int, int>>(n, unordered_map<int, int>());
        for (const auto& road : roads) {
            int u = road[0];
            int v = road[1];
            int time = road[2];
            graph[u][v] = time;
            graph[v][u] = time;
        }

        vector<long long> SSP = Dijkstra(graph, 0);

        
        dp = vector<long long>(n, 0);
        pq.push(make_tuple((long long)0, 0, (long long)1));
        vector<int> nodesInHeap(n, 0);
        nodesInHeap[0]++;

        while (!pq.empty()) {
            tuple<long long, int, long long> t = pq.top();
            long long arrivalTime = get<0>(t);
            int node = get<1>(t);
            long long arrivalCount = get<2>(t);

            pq.pop();
            dp[node] += arrivalCount;
            dp[node] %= MOD;
            nodesInHeap[node]--;

            if (node != n - 1 && nodesInHeap[node] == 0) {
                for (auto& [nxt, delta] : graph[node]) {
                    if (arrivalTime + delta == SSP[nxt]) {
                        pq.push(make_tuple(SSP[nxt], nxt, dp[node]));
                        nodesInHeap[nxt]++;
                    }
                }
            }
        }

        return (int)dp[n - 1];
    }

    vector<long long> Dijkstra(vector<unordered_map<int, int>>& graph, int source) 
    {
        int n = graph.size();
        vector<long long> result(n, (long long)-1);

        priority_queue<pair<long, int>, vector<pair<long, int>>, greater<pair<long, int>>> heap {};
        vector<bool> visited(n, false);
        int visitedCount = 0;
        heap.push({0, source});

        while (!heap.empty() && visitedCount < n) {
            long weight = heap.top().first;
            int node = heap.top().second;
            heap.pop();
            
            if (result[node] < 0) {
                result[node] = weight;
                visited[node] = true;
                visitedCount++;
                for (const auto& neighbor : graph[node]) {
                    int nxt = neighbor.first;
                    long nxtWeight = weight + (long long)neighbor.second;
                    heap.push({nxtWeight, nxt});
                }
            }
        }

        return result;
    }

};

// @lc code=end

