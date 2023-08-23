/*
 * @lc app=leetcode id=767 lang=cpp
 *
 * [767] Reorganize String
 */

// @lc code=start
#include <iostream>
#include <vector>
#include <string>
#include <queue>

using namespace std;

class Solution {
public:
    string reorganizeString(string s) {
        vector<int> hashTable(26, 0);
        for (char c : s) {
            hashTable[c - 'a']++;
        }
        
        int maxCount = 0;
        for (int count : hashTable) {
            maxCount = max(maxCount, count);
        }
        
        if (maxCount > (s.length() + 1) / 2) {
            return "";
        }
        
        priority_queue<pair<int, char>> heap;
        for (int i = 0; i < 26; i++) {
            if (hashTable[i] > 0) {
                heap.push({hashTable[i], static_cast<char>(i + 'a')});
            }
        }
        
        string result = "";
        while (!heap.empty()) 
        {
            int Count1 = heap.top().first;
            char chr1 = heap.top().second;
            heap.pop();
            if (!heap.empty())
            {
                int Count2 = heap.top().first;
                char chr2 = heap.top().second;
                heap.pop();
                if (!result.empty() && result.back() == chr1) 
                {
                    result += chr2;
                    Count2--;
                }
                if (Count2 > 0)
                {
                    heap.push({Count2, chr2});
                }
            }

            result += chr1;
            Count1--;
            if (Count1 > 0)
            {
                heap.push({Count1, chr1});
            }
        }       
        return result;
    }

private:
    priority_queue<pair<int, char>> heap;
};
// @lc code=end

