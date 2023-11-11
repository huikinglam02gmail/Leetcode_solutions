/*
 * @lc app=leetcode id=2642 lang=cpp
 *
 * [2642] Design Graph With Shortest Path Calculator
 */

// @lc code=start
#include <vector>
#include <unordered_map>;
#include <queue>
#include <algorithm>
using std::greater;
using std::pair;
using std::priority_queue;
using std::unordered_map;
using std::vector;
class Graph {
private:
    vector<unordered_map<int, int>> graph;
    vector<int> Dijkstra(int n, int source) 
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

public:
    Graph(int n, vector<vector<int>>& edges) {
        graph = vector<unordered_map<int, int>>(n, unordered_map<int, int>{});
        for (vector<int> edge : edges) graph[edge[0]][edge[1]] = edge[2];
    }
    
    void addEdge(vector<int> edge) {
        graph[edge[0]][edge[1]] = edge[2];
    }
    
    int shortestPath(int node1, int node2) {
        return Dijkstra(graph.size(), node1)[node2];
    }
};

/**
 * Your Graph object will be instantiated and called as such:
 * Graph* obj = new Graph(n, edges);
 * obj->addEdge(edge);
 * int param_2 = obj->shortestPath(node1,node2);
 */
// @lc code=end

