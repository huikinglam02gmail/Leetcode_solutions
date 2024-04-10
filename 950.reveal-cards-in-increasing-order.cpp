/*
 * @lc app=leetcode id=950 lang=cpp
 *
 * [950] Reveal Cards In Increasing Order
 */

// @lc code=start
#include <vector>
#include <queue>
#include <algorithm>

class Solution {
public:
    std::vector<int> deckRevealedIncreasing(std::vector<int>& deck) {
        int n = deck.size();
        int j = 0;
        std::vector<int> result(n, 0);
        std::queue<int> dq;

        std::sort(deck.begin(), deck.end());

        for (int i = 0; i < n; i++) {
            dq.push(i);
        }

        while (dq.size() >= 2) {
            result[dq.front()] = deck[j++];
            dq.pop();
            dq.push(dq.front());
            dq.pop();
        }

        result[dq.front()] = deck[j];
        return result;
    }
};

// @lc code=end

