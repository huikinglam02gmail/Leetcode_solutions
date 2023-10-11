/*
 * @lc app=leetcode id=2251 lang=cpp
 *
 * [2251] Number of Flowers in Full Bloom
 */

// @lc code=start
#include <vector>
#include <algorithm>
#include <queue>

class Solution {
public:
    std::vector<int> fullBloomFlowers(std::vector<std::vector<int>>& flowers, std::vector<int>& people) {
        std::vector<std::pair<int, int>> peopleByArrival;
        for (int i = 0; i < people.size(); i++) {
            peopleByArrival.push_back({people[i], i});
        }
        std::sort(peopleByArrival.begin(), peopleByArrival.end());

        std::sort(flowers.begin(), flowers.end());

        std::priority_queue<int, std::vector<int>, std::greater<int>> endHeap;
        std::vector<int> result(people.size(), 0);
        int flowerPtr = 0;

        for (int i = 0; i < people.size(); i++) {
            int time = peopleByArrival[i].first;
            int index = peopleByArrival[i].second;

            while (flowerPtr < flowers.size() && flowers[flowerPtr][0] <= time) {
                endHeap.push(flowers[flowerPtr][1]);
                flowerPtr++;
            }

            while (!endHeap.empty() && endHeap.top() < time) {
                endHeap.pop();
            }

            result[index] = endHeap.size();
        }

        return result;
    }
};

// @lc code=end

