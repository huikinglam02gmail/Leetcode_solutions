/*
 * @lc app=leetcode id=1081 lang=cpp
 *
 * [1081] Smallest Subsequence of Distinct Characters
 */

// @lc code=start
#include <vector>
#include <queue>
#include <algorithm> // Include for std::lower_bound
#include <string>

using namespace std;
class Solution {
public:
    string smallestSubsequence(string s) {
        vector<vector<int>> appear(26, vector<int>());
        int lastUsedIndex = -1;

        for (int i = 0; i < s.length(); i++) {
            int ind = s[i] - 'a';
            if (appear[ind].empty()) {
                appear[ind].push_back(i);
            }
            else {
                appear[ind].push_back(i);
            }
        }

        string result = "";
        vector<int> temp;
        priority_queue<int, vector<int>, greater<int>> needProcess;

        for (int i = 0; i < 26; i++) {
            if (!appear[i].empty()) {
                needProcess.push(i);
            }
        }

        while (!needProcess.empty()) {
            int ind = needProcess.top();
            needProcess.pop();
            if (!canUseThisCharacter(ind, appear, lastUsedIndex)) {
                temp.push_back(ind);
            }
            else {
                result += char(ind + 'a');
                appear[ind].clear();
                while (!temp.empty()) {
                    needProcess.push(temp.back());
                    temp.pop_back();
                }
            }
        }

        return result;
    }

private:
    bool canUseThisCharacter(int i, vector<vector<int>>& appear, int& lastUsedIndex) {
        int ind = appear[i][lower_bound(appear[i].begin(), appear[i].end(), lastUsedIndex) - appear[i].begin()];
        for (int j = 0; j < 26; j++) {
            if (j != i && !appear[j].empty() && lower_bound(appear[j].begin(), appear[j].end(), ind) == appear[j].end()) {
                return false;
            }
        }
        lastUsedIndex = ind;
        appear[i].clear();
        return true;
    }
};
// @lc code=end

