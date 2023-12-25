/*
 * @lc app=leetcode id=321 lang=cpp
 *
 * [321] Create Maximum Number
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<int> mostCompetitive(std::vector<int>& nums, int k) {
        std::vector<int> stack;
        int n = nums.size();
        
        for (int i = 0; i < n; i++) {
            while (!stack.empty() && nums[i] > stack.back() && n - i + stack.size() - 1 >= k) {
                stack.pop_back();
            }
            stack.push_back(nums[i]);
        }
        
        return std::vector<int>(stack.begin(), stack.begin() + k);
    }

    std::vector<int> mergeSubsequences(std::vector<int>& seq1, std::vector<int>& seq2) {
        std::vector<int> result;
        int i = 0, j = 0;

        while (i < seq1.size() && j < seq2.size()) {
            if (seq1[i] > seq2[j]) {
                result.push_back(seq1[i]);
                i++;
            } else if (seq1[i] < seq2[j]) {
                result.push_back(seq2[j]);
                j++;
            } else {
                int i1 = i + 1, j1 = j + 1;

                while (i1 < seq1.size() && j1 < seq2.size() && seq1[i1] == seq2[j1]) {
                    i1++;
                    j1++;
                }

                if (i1 == seq1.size() || (j1 < seq2.size() && seq1[i1] < seq2[j1])) {
                    result.push_back(seq2[j]);
                    j++;
                } else {
                    result.push_back(seq1[i]);
                    i++;
                }
            }
        }

        while (i < seq1.size()) {
            result.push_back(seq1[i]);
            i++;
        }

        while (j < seq2.size()) {
            result.push_back(seq2[j]);
            j++;
        }

        return result;
    }

    std::vector<int> findMax(std::vector<int>& result1, std::vector<int>& result2) {
        int n = result1.size();

        for (int i = 0; i < n; i++) {
            if (result1[i] > result2[i]) {
                return result1;
            } else if (result1[i] < result2[i]) {
                return result2;
            }
        }

        return result1;
    }

    std::vector<int> maxNumber(std::vector<int>& nums1, std::vector<int>& nums2, int k) {
        int useOneLowerLimit = std::max(0, k - static_cast<int>(nums2.size()));
        int useOneUpperLimit = std::min(static_cast<int>(nums1.size()), k);
        std::vector<int> result(k, 0);

        for (int i = useOneLowerLimit; i <= useOneUpperLimit; i++) {
            std::vector<int> nums1MaxSubSeq = mostCompetitive(nums1, i);
            std::vector<int> nums2MaxSubSeq = mostCompetitive(nums2, k - i);
            std::vector<int> current = mergeSubsequences(nums1MaxSubSeq, nums2MaxSubSeq);
            result = findMax(result, current);
        }

        return result;
    }
};

// @lc code=end

