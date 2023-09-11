/*
 * @lc app=leetcode id=1282 lang=cpp
 *
 * [1282] Group the People Given the Group Size They Belong To
 */

// @lc code=start
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<vector<int>> groupThePeople(vector<int>& groupSizes) {
        vector<vector<int>> result;
        unordered_map<int, vector<int>> hashMap;

        for (int i = 0; i < groupSizes.size(); i++) {
            int size = groupSizes[i];

            if (hashMap.find(size) == hashMap.end()) {
                hashMap[size] = vector<int>();
            }

            hashMap[size].push_back(i);

            if (hashMap[size].size() == size) {
                result.push_back(hashMap[size]);
                hashMap.erase(size);
            }
        }

        return result;
    }
};

// @lc code=end

