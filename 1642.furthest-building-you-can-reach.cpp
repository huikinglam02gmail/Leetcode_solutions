/*
 * @lc app=leetcode id=1642 lang=cpp
 *
 * [1642] Furthest Building You Can Reach
 */

// @lc code=start
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int furthestBuilding(vector<int>& heights, int bricks, int ladders) {
        priority_queue<int, vector<int>, greater<int>> minHeap;
        int result = 0;
        
        for (int i = 0; i < heights.size() - 1; i++) {
            if (heights[i + 1] > heights[i]) {
                minHeap.push(heights[i + 1] - heights[i]);
                
                if (ladders < minHeap.size()) {
                    bricks -= minHeap.top();
                    minHeap.pop();
                    if (bricks < 0) {
                        return i;
                    }
                }
            }
            result = i + 1;
        }
        
        return result;
    }
};

// @lc code=end

