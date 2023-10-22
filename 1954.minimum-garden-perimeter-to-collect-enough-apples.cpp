/*
 * @lc app=leetcode id=1954 lang=cpp
 *
 * [1954] Minimum Garden Perimeter to Collect Enough Apples
 */

// @lc code=start
class Solution {
public:
    long long minimumPerimeter(long long neededApples) {
        long long i = 0;
        while (neededApples > 0) {
            neededApples -= 12 * i * i;
            i++;
        }
        return 8 * (i - 1);
    }
};

// @lc code=end

