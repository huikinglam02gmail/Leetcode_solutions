/*
 * @lc app=leetcode id=1980 lang=cpp
 *
 * [1980] Find Unique Binary String
 */

// @lc code=start
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    string findDifferentBinaryString(vector<string>& nums) {
        int n = nums.size();
        int i = 0;
        while (i < (1 << n)) {
            string binaryString = toBinaryString(i, n);
            if (find(nums.begin(), nums.end(), binaryString) == nums.end()) {
                return binaryString;
            } else {
                i++;
            }
        }
        return "";
    }

private:
    string toBinaryString(int num, int n) {
        string binaryString = "";
        for (int i = 0; i < n; i++) {
            binaryString = (char)('0' + (num % 2)) + binaryString;
            num /= 2;
        }
        return binaryString;
    }
};

// @lc code=end

