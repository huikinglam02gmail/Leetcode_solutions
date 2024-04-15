/*
 * @lc app=leetcode id=3095 lang=cpp
 *
 * [3095] Shortest Subarray With OR at Least K I
 */

// @lc code=start
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
private:
    /*
    sliding window
    0 <= nums[i] <= 50: at most most 6 bits
    For each num in nums, we update current count of number of each bit. If removing the left element from the collecton would not make the subarray OR less than k, we would proceed to remove it.
    */
    void updateHashTable(bool addOrRemove, int num) {
        for (int i = 0; i < 6; i++) {
            if ((num & (1 << i)) != 0) {
                if (addOrRemove) {
                    hashTable[i]++;
                } else {
                    hashTable[i]--;
                }
                if (hashTable[i] == 1 && addOrRemove) {
                    current += (1 << i);
                }
                if (hashTable[i] == 0 && !addOrRemove) {
                    current -= (1 << i);
                }
            }
        }
    }

public:
    int minimumSubarrayLength(vector<int>& nums, int k) {
        int left = 0;
        int n = nums.size();
        current = 0;
        hashTable.resize(6);
        int result = n + 1;
        for (int right = 0; right < n; right++) {
            updateHashTable(true, nums[right]);
            if (current >= k) {
                result = min(result, right - left + 1);
            }
            bool cannotProceed = false;
            while (left < right && !cannotProceed) {
                updateHashTable(false, nums[left]);
                if (current >= k) {
                    left++;
                    result = min(result, right - left + 1);
                } else {
                    cannotProceed = true;
                    updateHashTable(true, nums[left]);
                }
            }
        }
        return result <= n ? result : -1;
    }

private:
    vector<int> hashTable;
    int current;
};

// @lc code=end

