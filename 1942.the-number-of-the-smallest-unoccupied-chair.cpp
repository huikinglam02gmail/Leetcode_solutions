/*
 * @lc app=leetcode id=1942 lang=cpp
 *
 * [1942] The Number of the Smallest Unoccupied Chair
 */

// @lc code=start
#include <vector>
#include <queue>
#include <algorithm>
#include <utility>

using std::greater;
using std::make_pair;
using std::pair;
using std::priority_queue;
using std::vector;

class Solution {
public:
    int smallestChair(vector<vector<int>>& times, int targetFriend) 
    {
        priority_queue<int, vector<int>, greater<int>> free;
        int curChair = -1;
        vector<vector<int>> timesWithIndex;
        
        for (int i = 0; i < times.size(); i++) {
            timesWithIndex.push_back(vector<int>{times[i][0], times[i][1], i});
        }
        
        sort(timesWithIndex.begin(), timesWithIndex.end());
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> occupied;
        
        for (const auto& item : timesWithIndex) {
            int arrival = item[0];
            int leaving = item[1];
            int i = item[2];
            
            while (!occupied.empty() && occupied.top().first <= arrival) 
            {
                int occupy = occupied.top().second;
                occupied.pop();
                free.push(occupy);
            }
            
            if (free.empty()) {
                curChair += 1;
                free.push(curChair);
            }
            
            int freeChairToUse = free.top();
            free.pop();
            
            if (i == targetFriend) {
                return freeChairToUse;
            }
            
            occupied.push(make_pair(leaving, freeChairToUse));
        }
        
        return -1;
    }
};
// @lc code=end

