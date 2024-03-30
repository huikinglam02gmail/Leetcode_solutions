/*
 * @lc app=leetcode id=2079 lang=cpp
 *
 * [2079] Watering Plants
 */

// @lc code=start
#include <vector>

class Solution {
public:
    /*
    Just simulation
    */
    int wateringPlants(std::vector<int>& plants, int capacity) {
        int result = 0;
        int curCapacity = capacity;
        for (int i = 0; i < plants.size(); i++) {
            if (curCapacity < plants[i]) {
                result += 2 * i;
                curCapacity = capacity;
            }
            curCapacity -= plants[i];
            result += 1;
        }
        return result;
    }
};

// @lc code=end

