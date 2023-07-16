/*
 * @lc app=leetcode id=1813 lang=cpp
 *
 * [1813] Sentence Similarity III
 */

// @lc code=start
#include <vector>
#include <string>
#include <queue>
using std::deque;
using std::string;
using std::vector;

class Solution {
    /*
    Use two deques to hold the sentences
    Then pop from fronts and ends
    return if deque1 or deque2 is empty
    */
public:
    bool areSentencesSimilar(string sentence1, string sentence2) {
        deque<string> dq1{};
        deque<string> dq2{};
        string word = "";
        for (char s : sentence1)
        {
            if (s == ' ')
            {
                dq1.push_back(word);
                word = "";
            }
            else
            {
                word += s;
            }
        }
        if (word.compare("") != 0)
        {
            dq1.push_back(word);
            word = "";
        }

        for (char s : sentence2)
        {
            if (s == ' ')
            {
                dq2.push_back(word);
                word = "";
            }
            else
            {
                word += s;
            }
        }
        if (word.compare("") != 0)
        {
            dq2.push_back(word);
            word = "";
        }
        while (dq1.size() > 0 && dq2.size() > 0 && dq1.front().compare(dq2.front()) == 0)
        {
            dq1.pop_front();
            dq2.pop_front();
        }
        while (dq1.size() > 0 && dq2.size() > 0 && dq1.back().compare(dq2.back()) == 0)
        {
            dq1.pop_back();
            dq2.pop_back();
        }
        return dq1.size() == 0 || dq2.size() == 0;
    }
};

// @lc code=end

