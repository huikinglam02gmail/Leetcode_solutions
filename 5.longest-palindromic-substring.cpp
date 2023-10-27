/*
 * @lc app=leetcode id=5 lang=cpp
 *
 * [5] Longest Palindromic Substring
 */

// @lc code=start
#include <string>
#include <vector>

using std::string;

class Solution {
public:
    std::string longestPalindrome(std::string s) {
        // Modify the string so that it's always odd
        std::string newString = "|";
        for (char c : s) {
            newString += c;
            newString += "|";
        }

        int n = newString.length();
        std::vector<int> lps(n, 0);
        int center = 0, right = 0; // Center and right boundary of the rightmost palindrome

        for (int i = 0; i < n; i++) {
            if (i < center + right) { // If there's an overlap
                int j = lps[center - (i - center)]; // Reflect

                if (j < center + right - i) { // Case A
                    lps[i] = j;
                    continue;
                }
                else if (j > center + right - i) { // Case B
                    lps[i] = center + right - i;
                    continue;
                }
                else { // Case C
                }
            }
            else { // No overlap
                int j = 0;
            }

            while (i - lps[i] > 0 && i + lps[i] < n - 1 && newString[i - lps[i] - 1] == newString[i + lps[i] + 1]) {
                lps[i]++;
            }

            if (i + lps[i] > center + right) {
                center = i;
                right = lps[i];
            }
        }

        int maxLength = 0;
        int maxIndex = 0;

        for (int i = 0; i < n; i++) {
            if (lps[i] > maxLength) {
                maxLength = lps[i];
                maxIndex = i;
            }
        }

        string result{};
        for (int i = maxIndex - maxLength + 1; i <= maxIndex + maxLength; i += 2)
        {
            result += newString[i];
        }
        return result;
    }
};

// @lc code=end

