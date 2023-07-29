/*
 * @lc app=leetcode id=31 lang=cpp
 *
 * [31] Next Permutation
 */

// @lc code=start
#include <algorithm>
#include <vector>
using std::swap;

class Solution {
public:
    /*
     * A good example is [1,2,4,3]
     * Find the first instance in which nums[i] < nums[i+1]
     * That's the index in which one can exchange between later index
     * -> index 2
     * Then we swap the one element before this index with the rightmost element which is larger than this element
     * [1, 3, 4, 2]
     * finally, we swap everything element between left + 1 and right
     * If the sequence is non-increasing, we swap the whole sequence
     */
    void nextPermutation(std::vector<int>& nums) {
        int n = nums.size();
        int i = n - 2;
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--;
        }

        if (i >= 0) {
            int j = n - 1;
            while (j > i && nums[i] >= nums[j]) {
                j--;
            }
            // exchange
            swap(nums[i], nums[j]);
        }

        i++;
        int k = n - 1;
        while (i < k) {
            swap(nums[i], nums[k]);
            i++;
            k--;
        }
    }
};

// @lc code=end

