/*
 * @lc app=leetcode id=2305 lang=cpp
 *
 * [2305] Fair Distribution of Cookies
 */

// @lc code=start
#include<vector>
#include<string>
#include<unordered_map>
#include<algorithm>
using std::min;
using std::sort;
using std::stoi;
using std::string;
using std::to_string;
using std::unordered_map;
using std::vector;
class Solution {
private:
    vector<int> Cookies;
    vector<unordered_map<string, int>> memo;
    string delimiter{"_"};
    int DFS(int i, const string& stateString)
    {
        int l = 0;
        vector<int> state{};
        for (int r = 0; r < stateString.size() + 1; r++)
        {
            if (r == stateString.size() || stateString.at(r) == delimiter.at(0))
            {
                state.push_back(stoi(stateString.substr(l, r - l)));
                l = r + 1;
            }
        }
        if (i == Cookies.size())
        {
            return state.back();
        }
        else if (memo[i].find(stateString) == memo[i].end())
        {
            int result = INT_MAX;
            for (int j = 0; j < state.size(); j++)
            {
                state[j] += Cookies[i];
                vector<int> newState(state);
                sort(newState.begin(), newState.end());
                result = min(result, DFS(i + 1, stateStringFromState(newState, delimiter)));
                state[j] -= Cookies[i];
            }
            memo[i].insert({stateString, result});
        }
        return memo[i][stateString];
    }

    string stateStringFromState(vector<int>& state, string& delim)
    {
        string stateString = "";
        for (int i = 0; i < state.size(); i++)
        {
            stateString += to_string(state[i]);
            if (i < state.size() - 1)
            {
                stateString += delim;
            }
        }
        return stateString;
    }

public:
    int distributeCookies(vector<int>& cookies, int k) {
        Cookies = cookies;
        memo.resize(cookies.size(), unordered_map<string, int>{});
        vector<int> initial(k, 0);
        return DFS(0, stateStringFromState(initial, delimiter));
    }
};
// @lc code=end

