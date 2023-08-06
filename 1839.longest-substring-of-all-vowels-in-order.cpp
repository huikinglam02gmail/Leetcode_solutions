/*
 * @lc app=leetcode id=1839 lang=cpp
 *
 * [1839] Longest Substring Of All Vowels in Order
 */

// @lc code=start
#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    /*
    This is a sliding window problem.
    Pretty much we can add to the current string the current character
    Since we only have aeiou, we just need to find if the appearance of a, e, i, o and u are sorted.
    If not, any further indices would not be beautiful.
    For example if word = "aeiaaioaaaaeiiiiouuuooaauuaeiu" When we have current valid string to be "aei", and when "a" comes in, we check if "e", "i", "o" and "u" has occurred. If so, pop them.
    */
    int longestBeautifulSubstring(std::string word) {
        std::unordered_map<char, int> vowels = {
            {'a', 0},
            {'e', 1},
            {'i', 2},
            {'o', 3},
            {'u', 4}
        };
        
        std::vector<std::queue<int>> indices(5);
        
        int result = 0;
        for (int ind = 0; ind < word.length(); ind++) {
            char c = word[ind];
            for (int i = vowels[c] + 1; i < 5; i++) {
                while (!indices[i].empty()) {
                    for (int j = 0; j < i; j++) {
                        while (!indices[j].empty() && indices[j].front() < indices[i].front()) {
                            indices[j].pop();
                        }
                    }
                    indices[i].pop();
                }
            }
            indices[vowels[c]].push(ind);
            bool allIndicesNonEmpty = std::all_of(indices.begin(), indices.end(), [](const std::queue<int>& q) {
                return !q.empty();
            });
            if (allIndicesNonEmpty) {
                int sum = 0;
                for (const auto& q : indices) {
                    sum += q.size();
                }
                result = std::max(result, sum);
            }
        }
        return result;
    }
};

// @lc code=end

