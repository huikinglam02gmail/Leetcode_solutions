/*
 * @lc app=leetcode id=131 lang=cpp
 *
 * [131] Palindrome Partitioning
 */

// @lc code=start
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> res;
        vector<string> path;
        dfs(s, path, res);
        return res;
    }
    
private:
    bool isPalindrome(const string& s) {
        int left = 0;
        int right = s.size() - 1;
        while (left < right) {
            if (s[left] != s[right]) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    void dfs(const string& s, vector<string>& path, vector<vector<string>>& res) {
        if (s.empty()) {
            res.push_back(path);
            return;
        }
        
        for (int i = 1; i <= s.size(); i++) {
            string prefix = s.substr(0, i);
            if (isPalindrome(prefix)) {
                path.push_back(prefix);
                dfs(s.substr(i), path, res);
                path.pop_back();
            }
        }
    }
};

// @lc code=end

