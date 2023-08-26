/*
 * @lc app=leetcode id=1871 lang=cpp
 *
 * [1871] Jump Game VII
 */

// @lc code=start
#include <string>
#include <deque>

class Solution {
public:
    bool canReach(std::string s, int minJump, int maxJump) {
        std::deque<int> dq;
        dq.push_back(0);
        bool result = false;
        
        for (int i = 0; i < s.size(); i++) {
            while (!dq.empty() && dq.front() < i) {
                dq.pop_front();
            }
            
            if (s[i] == '0' && !dq.empty() && dq.front() - maxJump + minJump <= i && i <= dq.front()) {
                dq.push_back(i + maxJump);
                if (i == s.size() - 1) {
                    result = true;
                }
            }
        }
        
        return result;
    }
};
// @lc code=end

