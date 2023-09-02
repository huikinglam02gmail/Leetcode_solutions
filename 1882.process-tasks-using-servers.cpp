/*
 * @lc app=leetcode id=1882 lang=cpp
 *
 * [1882] Process Tasks Using Servers
 */

// @lc code=start
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> assignTasks(vector<int>& servers, vector<int>& tasks) {
        priority_queue<vector<int>> free{}; // {weight, index, endTime}
        priority_queue<vector<int>> busy {}; // {endTime, weight, index}

        for (int i = 0; i < servers.size(); i++) 
        {
            free.push(vector<int>{- servers[i], - i, 0});
        }

        vector<int> ans {};
        for (int j = 0; j < tasks.size(); j++) 
        {
            while (free.empty() || (!busy.empty() && - busy.top()[0] <= j)) 
            {
                vector<int> busyTop = busy.top();
                busy.pop();
                free.push({busyTop[1], busyTop[2], busyTop[0]});
            }

            vector<int> freeTop = free.top();
            free.pop();
            ans.push_back(- freeTop[1]);
            busy.push(vector<int> {- max(- freeTop[2], j) - tasks[j], freeTop[0], freeTop[1]});
        }

        return ans;
    }
};

// @lc code=end

