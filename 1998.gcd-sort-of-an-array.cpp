/*
 * @lc app=leetcode id=1998 lang=cpp
 *
 * [1998] GCD Sort of an Array
 */

// @lc code=start
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>

class UnionFindSet {
private:
    std::vector<int> parents;
    int count;

public:
    UnionFindSet(int n) : parents(n), count(n) {
        for (int i = 0; i < n; ++i) {
            parents[i] = i;
        }
    }

    int find(int u) {
        if (u != parents[u]) {
            parents[u] = find(parents[u]);
        }
        return parents[u];
    }

    void unionSets(int u, int v) {
        int pu = find(u);
        int pv = find(v);
        if (pu != pv) {
            int pMax = std::max(pu, pv);
            int pMin = std::min(pu, pv);
            parents[pMax] = pMin;
            count--;
        }
    }

    int getCount() const {
        return count;
    }
};

class Solution {
private:
    std::vector<int> smallestPrimes;

    std::vector<int> smallestPrimeSieveOfEratosthenes(int n) {
        std::vector<int> prime(n + 1);
        for (int i = 0; i <= n; ++i) {
            prime[i] = i;
        }

        int p = 2;
        while (p * p <= n) {
            if (prime[p] == p) {
                for (int i = p * p; i <= n; i += p) {
                    if (prime[i] == i) {
                        prime[i] = p;
                    }
                }
            }
            p++;
        }
        return prime;
    }

    std::unordered_set<int> allPrimeFactors(int num) {
        std::unordered_set<int> factors;
        if (num <= 1) {
            return factors;
        }

        int p = smallestPrimes[num];
        if (p == num) {
            factors.insert(num);
        } else {
            factors.insert(p);
            auto subFactors = allPrimeFactors(num / p);
            factors.insert(subFactors.begin(), subFactors.end());
        }

        return factors;
    }

public:
    bool gcdSort(std::vector<int>& nums) {
        int maxNum = *std::max_element(nums.begin(), nums.end());
        int n = nums.size();

        smallestPrimes = smallestPrimeSieveOfEratosthenes(maxNum);
        std::unordered_map<int, std::vector<int>> primeToIndexDict;

        for (int i = 0; i < n; ++i) {
            std::unordered_set<int> primes = allPrimeFactors(nums[i]);
            for (int prime : primes) {
                primeToIndexDict[prime].push_back(i);
            }
        }

        UnionFindSet uf(n);
        for (const auto& entry : primeToIndexDict) {
            const std::vector<int>& indices = entry.second;
            for (int i = 1; i < indices.size(); ++i) {
                uf.unionSets(indices[0], indices[i]);
            }
        }

        std::vector<std::vector<int>> numSortedWithIndex;
        for (int i = 0; i < n; ++i) {
            numSortedWithIndex.push_back({nums[i], i});
        }
        std::sort(numSortedWithIndex.begin(), numSortedWithIndex.end());

        for (int i = 0; i < n; ++i) {
            if (uf.find(numSortedWithIndex[i][1]) != uf.find(i)) {
                return false;
            }
        }

        return true;
    }
};

// @lc code=end

