/*
 * @lc app=leetcode id=1761 lang=cpp
 *
 * [1761] Minimum Degree of a Connected Trio in a Graph
 */

// @lc code=start
#include<vector>
#include<unordered_set>
#include<algorithm>
using std::min;
using std::unordered_set;
using std::vector;
class Solution 
{
public:
    int minTrioDegree(int n, vector<vector<int>>& edges) 
    {
        vector<unordered_set<int>> graph(n, unordered_set<int>{});
        vector<int> degree(n, 0);
        
        for (vector<int> edge : edges) 
        {
            int u = edge[0] - 1;
            int v = edge[1] - 1;
            
            graph[u].insert(v);
            graph[v].insert(u);
            degree[u]++;
            degree[v]++;
        }
        
        int result = 3 * n;
        
        for (int i = 0; i < n - 2; i++) 
        {
            for (int j = i + 1; j < n - 1; j++) 
            {
                for (int k = j + 1; k < n; k++) 
                {
                    if (graph[i].count(j) == 1 && graph[i].count(k) == 1 && graph[j].count(k) == 1) 
                    {
                        result = min(result, degree[i] + degree[j] + degree[k] - 6);
                    }
                }
            }
        }        
        return result != 3 * n ? result : -1;
    }
};
// @lc code=end

