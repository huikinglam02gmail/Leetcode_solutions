/*
 * @lc app=leetcode id=1860 lang=cpp
 *
 * [1860] Incremental Memory Leak
 */

// @lc code=start
#include <vector>
#include <queue>
#include <algorithm>

class Solution {
public:
    std::vector<int> memLeak(int memory1, int memory2) {
        std::priority_queue<std::pair<long long, int>> heap;
        heap.push({ memory1, 0});
        heap.push({ memory2, - 1});
        int i = 1;
        while (heap.top().first >= i) {
            auto [available, ind] = heap.top();
            heap.pop();
            heap.push({available - i, ind});
            i++;
        }
        std::vector<int> result = {i, 0, 0};
        while (!heap.empty()) {
            auto [available, ind] = heap.top();
            heap.pop();
            result[- ind + 1] = available;
        }
        return result;
    }
};

// @lc code=end

