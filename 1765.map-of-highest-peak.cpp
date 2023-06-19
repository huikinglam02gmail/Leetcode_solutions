/*
 * @lc app=leetcode id=1765 lang=cpp
 *
 * [1765] Map of Highest Peak
 */

// @lc code=start
#include<vector>
#include<queue>
#include<tuple>
#include<set>
#include<algorithm>
#include<iostream>

using std::iostream;
using std::make_tuple;
using std::queue;
using std::set;
using std::tuple;
using std::vector;
class Solution {
public:
    vector<vector<int>> highestPeak(vector<vector<int>>& isWater) {
        int m = isWater.size();
        int n = isWater[0].size();
        vector<vector<int>> height;
        vector<vector<bool>> visited;
        height.resize(m, std::vector<int>(n, 0));
        visited.resize(m, std::vector<bool>(n, false));
        queue<tuple<int, int>> queue{};
        int current = 0;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (isWater[i][j] == 1) {
                    queue.push(make_tuple(i, j));
                    visited[i][j] = true;
                }
            }
        }
        
        while (queue.size() > 0) {
            int size = queue.size();
            
            for (int i = 0; i < size; i++) {
                tuple<int, int> t = queue.front();
                queue.pop();
                int x = get<0>(t);
                int y = get<1>(t);
                height[x][y] = current;
                
                vector<tuple<int, int>> neighbors = {
                    make_tuple(x + 1, y),
                    make_tuple(x - 1, y),
                    make_tuple(x, y + 1),
                    make_tuple(x, y - 1)
                };
                
                for (tuple<int, int> neighbor : neighbors) {
                    int nx = get<0>(neighbor);
                    int ny = get<1>(neighbor);
                    
                    if (nx >= 0 && nx < m && ny >= 0 && ny < n && !visited[nx][ny]) {
                        visited[nx][ny] = true;
                        queue.push(neighbor);
                    }
                }
            }
            
            current++;
        }
        
        return height;        
    }
};
// @lc code=end

