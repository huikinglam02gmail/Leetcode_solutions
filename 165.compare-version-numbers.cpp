/*
 * @lc app=leetcode id=165 lang=cpp
 *
 * [165] Compare Version Numbers
 */

// @lc code=start
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<string> trimLeadingZero(vector<string>& versionSplit) {
        vector<string> vArr;
        for (const string& part : versionSplit) {
            int p = 0;
            while (p < part.length() && part[p] == '0') p++;
            if (p == part.length()) vArr.push_back("0");
            else vArr.push_back(part.substr(p));
        }
        return vArr;
    }

    int compareVersion(string version1, string version2) {
        vector<string> version1_split, version2_split;
        size_t pos = 0;
        while ((pos = version1.find('.')) != string::npos) {
            version1_split.push_back(version1.substr(0, pos));
            version1.erase(0, pos + 1);
        }
        version1_split.push_back(version1);

        pos = 0;
        while ((pos = version2.find('.')) != string::npos) {
            version2_split.push_back(version2.substr(0, pos));
            version2.erase(0, pos + 1);
        }
        version2_split.push_back(version2);

        vector<string> vArr1 = trimLeadingZero(version1_split);
        vector<string> vArr2 = trimLeadingZero(version2_split);

        while (vArr1.size() < vArr2.size()) vArr1.push_back("0");
        while (vArr2.size() < vArr1.size()) vArr2.push_back("0");

        for (size_t i = 0; i < vArr2.size(); i++) {
            if (vArr1[i].length() > vArr2[i].length()) return 1;
            else if (vArr1[i].length() < vArr2[i].length()) return -1;
            else if (vArr1[i] > vArr2[i]) return 1;
            else if (vArr1[i] < vArr2[i]) return -1;
        }
        return 0;
    }
};

// @lc code=end

