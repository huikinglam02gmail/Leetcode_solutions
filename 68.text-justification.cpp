/*
 * @lc app=leetcode id=68 lang=cpp
 *
 * [68] Text Justification
 */

// @lc code=start
#include <vector>
#include <string>

class Solution {
public:
    std::vector<std::string> fullJustify(std::vector<std::string>& words, int maxWidth) {
        int j = 0;
        int wordLengthAccumulated = 0;
        std::vector<std::string> result;
        int n = words.size();

        for (int i = 0; i < n; i++) {
            if (wordLengthAccumulated + i - j + words[i].length() > maxWidth) {
                std::string row = words[j];
                int remainingEmptySpace = maxWidth - wordLengthAccumulated;
                wordLengthAccumulated -= words[j].length();
                j++;

                if (i == j) {
                    row += std::string(remainingEmptySpace, ' ');
                } else {
                    int shortest = remainingEmptySpace / (i - j);
                    while (j < i) {
                        if (remainingEmptySpace % (i - j) > 0) {
                            row += std::string(shortest + 1, ' ');
                            remainingEmptySpace -= shortest + 1;
                        } else {
                            row += std::string(shortest, ' ');
                            remainingEmptySpace -= shortest;
                        }
                        row += words[j];
                        wordLengthAccumulated -= words[j].length();
                        j++;
                    }
                }

                result.push_back(row);
            }

            wordLengthAccumulated += words[i].length();
        }

        std::string row = "";

        while (wordLengthAccumulated > 0) {
            row += words[j];
            wordLengthAccumulated -= words[j].length();

            if (wordLengthAccumulated > 0) {
                row += " ";
                j++;
            }
        }

        while (row.length() < maxWidth) {
            row += " ";
        }

        result.push_back(row);

        return result;
    }
};

// @lc code=end

