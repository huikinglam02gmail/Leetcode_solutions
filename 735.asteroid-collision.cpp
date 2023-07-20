/*
 * @lc app=leetcode id=735 lang=cpp
 *
 * [735] Asteroid Collision
 */

// @lc code=start
#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

class Solution {
public:
    /*
     * Use a stack to maintain the preexisting asteroids.
     * One important point is that the negative ones appearing left of the positive ones will never collide, so they will be ignored.
     * I used a collision_ended marker to indicate if any collision between an old positive asteroid in the stack and a new negative asteroid has been accounted for.
     * Note that I only turn it True when the incoming asteroid is larger than or equal to the incoming asteroid.
     */
    std::vector<int> asteroidCollision(std::vector<int>& asteroids) {
        std::stack<int> st;
        for (int asteroid : asteroids) {
            if (st.empty()) {
                st.push(asteroid);
            } else {
                bool collisionEnded = false;
                while (!st.empty() && st.top() >= 0 && asteroid < 0 && !collisionEnded) {
                    int old = st.top();
                    st.pop();
                    collisionEnded = old + asteroid >= 0;
                    if (old + asteroid > 0) {
                        st.push(old);
                    }
                }
                if (!collisionEnded) {
                    st.push(asteroid);
                }
            }
        }
        std::vector<int> result;
        while (!st.empty()) {
            result.push_back(st.top());
            st.pop();
        }
        std::reverse(result.begin(), result.end());
        return result;
    }
};
// @lc code=end

