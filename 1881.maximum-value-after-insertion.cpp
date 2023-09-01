/*
 * @lc app=leetcode id=1881 lang=cpp
 *
 * [1881] Maximum Value after Insertion
 */

// @lc code=start
#include <string>

using namespace std;

class Solution {
public:
    string maxValue(string n, int x) {
        bool neg = n[0] == '-';
        int i = neg ? 1 : 0;
        bool stop = false;

        while (i < n.length() && !stop) {
            if (neg)
                stop = x < stoi(n.substr(i, 1));
            else
                stop = x > stoi(n.substr(i, 1));

            if (!stop)
                i++;
        }

        return n.substr(0, i) + to_string(x) + n.substr(i);
    }
};
// @lc code=end

