/*
 * @lc app=leetcode id=207 lang=cpp
 *
 * [207] Course Schedule
 */

// @lc code=start
#include <vector>
#include <queue>
#include <unordered_set>
using std::queue;
using std::unordered_set;
using std::vector;

class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> G(numCourses);
        vector<int> degree(numCourses);
        
        for (const vector<int>& prerequisite : prerequisites) {
            int j = prerequisite[0];
            int i = prerequisite[1];
            G[i].push_back(j);
            degree[j]++;
        }
        
        queue<int> dq;
        unordered_set<int> seen;
        
        for (int i = 0; i < numCourses; i++) {
            if (degree[i] == 0) {
                dq.push(i);
                seen.insert(i);
            }
        }
        
        while (!dq.empty()) {
            int i = dq.front();
            dq.pop();
            
            for (int j : G[i]) {
                degree[j]--;
                
                if (degree[j] == 0) {
                    dq.push(j);
                    seen.insert(j);
                }
            }
        }
        
        return seen.size() == numCourses;
    }
};

// @lc code=end

