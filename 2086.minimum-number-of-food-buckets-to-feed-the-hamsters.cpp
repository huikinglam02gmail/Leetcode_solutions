/*
 * @lc app=leetcode id=2086 lang=cpp
 *
 * [2086] Minimum Number of Food Buckets to Feed the Hamsters
 */

// @lc code=start
#include <string>

using namespace std;

class Solution {
public:
    /**
     * Take a greedy approach, keep track of last placed food position
     * For each Hamster:
     * 1. check for 0 <= i - 1 < n, last == i - 1; if not:
     * 2. try to feed it on its right: i + 1, given 0 <= i + 1 < n, and hamsters[i + 1] == '.' -> result += 1, last = i + 1
     * 3. if unsuccessful, try to feed it on its right, given  0 <= i - 1 < n, and hamsters[i - 1] == '.' -> result += 1, last = i - 1
     * 4. else return -1
     */
    int minimumBuckets(string hamsters) {
        int last = -2;
        int result = 0;
        int n = hamsters.length();
        for (int i = 0; i < n; i++) {
            if (hamsters[i] == '.') continue;
            if (i >= 1 && last == i - 1) continue;
            if (i < n - 1 && hamsters[i + 1] == '.') {
                result += 1;
                last = i + 1;
            } else if (i >= 1 && hamsters[i - 1] == '.') {
                result += 1;
                last = i - 1;
            } else {
                return -1;
            }
        }
        return result;
    }
};

// @lc code=end

