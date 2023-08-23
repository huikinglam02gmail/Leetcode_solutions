/*
 * @lc app=leetcode id=1865 lang=cpp
 *
 * [1865] Finding Pairs With a Certain Sum
 */

// @lc code=start
#include <vector>
#include <unordered_map>

using namespace std;

class FindSumPairs {
private:
    unordered_map<int, int> hashTable;
    vector<int> nums1;
    vector<int> nums2;

public:
    FindSumPairs(vector<int>& nums1, vector<int>& nums2) {
        this->nums1 = nums1;
        this->nums2 = nums2;
        for (int num : nums2) {
            hashTable[num]++;
        }
    }

    void add(int index, int val) {
        int num = nums2[index];
        hashTable[num]--;
        int newNum = num + val;
        hashTable[newNum]++;
        nums2[index] = newNum;
    }

    int count(int tot) {
        int result = 0;
        for (int num1 : nums1) {
            int target = tot - num1;
            if (hashTable.find(target) != hashTable.end()) {
                result += hashTable[target];
            }
        }
        return result;
    }
};

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * FindSumPairs* obj = new FindSumPairs(nums1, nums2);
 * obj->add(index,val);
 * int param_2 = obj->count(tot);
 */
// @lc code=end

