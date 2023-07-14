/*
 * @lc app=leetcode id=1807 lang=cpp
 *
 * [1807] Evaluate the Bracket Pairs of a String
 */

// @lc code=start
#include <unordered_map>
#include <stack>
#include <vector>
#include <string>

using std::string;
using std::unordered_map;
using std::vector;

class Solution {
public:
    /*
    use stack to hold previous string, when seeing "(". pop when seeing ")"
    */
    string evaluate(string s, vector<vector<string>>& knowledge) {
        unordered_map<string, string> hashTable;
        
        for (const auto& pair : knowledge) {
            hashTable[pair[0]] = pair[1];
        }
        
        int n = s.length();
        string temp;
        string result = "";
        int i = 0;

        while (i < n)
        {
            if (s[i] != '(')
            {
                result += s[i++];
            }
            else
            {
                int j = i + 1;
                temp = "";
                while (j < n && s[j] != ')')
                {
                    temp += s[j++];
                }
                result += (hashTable.find(temp) != hashTable.end() ? hashTable[temp] : "?");
                i = j + 1;
            }
        }
        
        return result;
    }
};

// @lc code=end

