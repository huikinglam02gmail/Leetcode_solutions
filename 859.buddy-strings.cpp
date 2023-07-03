/*
 * @lc app=leetcode id=859 lang=cpp
 *
 * [859] Buddy Strings
 */

// @lc code=start
#include<string>
#include<vector>
#include<algorithm>
using std::max_element;
using std::pair;
using std::string;
using std::vector;
class Solution {
public:
    bool buddyStrings(string s, string goal) {
        if (s.size() == goal.size()) {
            vector<int> hashTable(26, 0);
            vector<pair<int, int>> mismatch {};
            for (int i = 0; i < s.size(); i++) {
                hashTable[(int)s[i] - (int)'a']++;
                if (s[i] != goal[i]) {
                    mismatch.push_back({(int)s[i], (int)goal[i]});
                }
            }
            switch(mismatch.size())
            {
                case 0: return *max_element(hashTable.begin(), hashTable.end()) > 1;
                case 2: return mismatch[0].first == mismatch[1].second && mismatch[0].second == mismatch[1].first;
            }
        }
        return false;
    }
};
// @lc code=end

