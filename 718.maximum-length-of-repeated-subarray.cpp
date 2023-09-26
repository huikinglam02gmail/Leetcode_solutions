/*
 * @lc app=leetcode id=718 lang=cpp
 *
 * [718] Maximum Length of Repeated Subarray
 */

// @lc code=start
#include <vector>
#include <unordered_map>
#include <cmath>

using namespace std;

class Solution {
private:
    vector<long long> lookup;
    const long long basis = 101;
    const long long MOD = static_cast<long long>(pow(2, 31) - 1);
    vector<int> nums1;
    vector<int> nums2;

public:
    int findLength(vector<int>& nums1, vector<int>& nums2) {
        this->nums1 = nums1;
        this->nums2 = nums2;
        int m = nums1.size();
        int n = nums2.size();

        lookup.resize(min(m, n));
        long long seed = 1;
        for (int i = 0; i < min(m, n); i++) {
            lookup[i] = seed;
            seed *= basis;
            seed %= MOD;
        }

        int left = 1;
        int right = min(m, n) + 1;
        int result = 0;

        while (left < right) {
            int mid = left + (right - left) / 2;
            if (foundSubArray(mid)) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return left - 1;
    }

private:
    bool foundSubArray(int size) {
        unordered_map<long long, vector<int>> seen;
        long long h = 0;

        for (int i = 0; i < nums1.size() - size + 1; i++) {
            h = rollingHash(nums1, i, size, h);
            if (seen.find(h) == seen.end()) {
                seen[h] = vector<int>();
            }
            seen[h].push_back(i);
        }

        h = 0;
        for (int i = 0; i < nums2.size() - size + 1; i++) {
            h = rollingHash(nums2, i, size, h);
            if (seen.find(h) != seen.end()) {
                for (int j : seen[h]) {
                    if (arrayEquals(j, i, size)) {
                        return true;
                    }
                }
            }
        }

        return false;
    }

    long long rollingHash(vector<int>& arr, int i, int size, long long seed) {
        long long h = seed;
        if (i == 0) {
            for (int j = 0; j < size; j++) {
                h *= basis;
                h += arr[i + j];
                h %= MOD;
            }
        } else {
            h -= arr[i - 1] * lookup[size - 1];
            while (h < 0) {
                h += MOD;
            }
            h %= MOD;
            h *= basis;
            h += arr[i + size - 1];
            h %= MOD;
        }
        return h;
    }

    bool arrayEquals(int start1, int start2, int size) {
        for (int i = 0; i < size; i++) {
            if (nums1[start1 + i] != nums2[start2 + i]) {
                return false;
            }
        }
        return true;
    }
};

// @lc code=end

