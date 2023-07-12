/*
 * @lc app=leetcode id=1806 lang=cpp
 *
 * [1806] Minimum Number of Operations to Reinitialize a Permutation
 */

// @lc code=start
#include <vector>
#include <deque>
#include <algorithm>

class Solution {
public:
    /*
    We can use BFS from each index and find all the possible positions. The result is the maximum cluster size.
    */
    int reinitializePermutation(int n) {
        std::vector<bool> seen(n, false);
        int result = 0;
        
        for (int i = 0; i < n; i++) {
            if (!seen[i]) {
                std::deque<int> dq;
                seen[i] = true;
                dq.push_back(i);
                int ans = 0;
                
                while (!dq.empty()) {
                    int node = dq.front();
                    dq.pop_front();
                    ans++;
                    int nxt = (node % 2 == 0) ? node / 2 : n / 2 + (node - 1) / 2;
                    
                    if (!seen[nxt]) {
                        seen[nxt] = true;
                        dq.push_back(nxt);
                    }
                }
                
                result = std::max(result, ans);
            }
        }
        
        return result;
    }
};

// @lc code=end

