/*
 * @lc app=leetcode id=881 lang=cpp
 *
 * [881] Boats to Save People
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    /*
    Sort the people. Then for each heaviest person, try to pair him with the lightest person (two-pointer)
    */
    int numRescueBoats(std::vector<int>& people, int limit) {
        std::sort(people.begin(), people.end());
        int result = 0;
        int left = 0;
        int right = people.size() - 1;
        while (left <= right) {
            result++;
            if (people[left] + people[right] <= limit) {
                left++;
            }
            right--;
        }
        return result;
    }
};

// @lc code=end

