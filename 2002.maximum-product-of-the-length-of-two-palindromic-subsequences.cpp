/*
 * @lc app=leetcode id=2002 lang=cpp
 *
 * [2002] Maximum Product of the Length of Two Palindromic Subsequences
 */

// @lc code=start
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <string>
#include <algorithm>

using std::max;
using std::string;
using std::unordered_map;
using std::unordered_set;

class Solution {
public:
    /*
    2 <= s.length <= 12
    so we can use bitmask to represent which bits are used
    First thing to do: for each mask, determine if the mask represents a palindrome O(2 ^ 12)
    Then among the mask, determine if the subMasks of 0 ^ mask are inside the set
    */
    
    /*
    C++ program to decide if a string is a palindrome
    */
    bool isPalindrome(const string& s) {
        int l = 0, r = s.length() - 1;
        while (l < r) {
            if (s[l] != s[r]) {
                return false;
            } else {
                l++;
                r--;
            }
        }
        return true;
    }

    /*
    Method to return all subsets of set bits of num1 while smaller than num2
    */
    unordered_set<int> setBits(int num1, int num2) {
        unordered_set<int> result;
        int temp = num1;
        while (temp > 0) {
            if (temp <= num2) {
                result.insert(temp);
            }
            temp--;
            temp &= num1;
        }
        return result;
    }

    int maxProduct(string s) {
        int n = s.length();
        unordered_map<int, int> palindromes;
        for (int mask = 1; mask < (1 << n); mask++) {
            string sMask = "";
            int count = 0;
            for (int i = n - 1; i >= 0; i--) {
                if ((mask & (1 << i)) > 0) {
                    sMask += s[i];
                    count++;
                }
            }
            if (isPalindrome(sMask)) {
                palindromes[mask] = count;
            }
        }

        int result = 0;
        for (int mask = 1; mask < (1 << n); mask++) {
            if (palindromes.find(mask) != palindromes.end()) {
                unordered_set<int> antiMaskSet = setBits(((1 << n) - 1) ^ mask, 1 << n);
                for (int aMask : antiMaskSet) {
                    if (palindromes.find(aMask) != palindromes.end()) {
                        result = max(result, palindromes[mask] * palindromes[aMask]);
                    }
                }
            }
        }

        return result;
    }
};

// @lc code=end

