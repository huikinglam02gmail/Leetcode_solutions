/*
 * @lc app=leetcode id=2709 lang=cpp
 *
 * [2709] Greatest Common Divisor Traversal
 */

// @lc code=start
#include <vector>
#include <unordered_map>
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

    void unionSet(int u, int v) {
        int pu = find(u);
        int pv = find(v);
        if (pu != pv) {
            parents[pu] = pv;
            --count;
        }
    }

    int getCount() const {
        return count;
    }
};

class Solution {
public:
    bool canTraverseAllPairs(std::vector<int>& nums) {
        if (nums.size() == 1) return true;
        std::unordered_map<int, std::vector<int>> primeIndicesDict;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] == 1) return false;
            std::unordered_map<int, int> primeFacs = primeFactors(nums[i]);
            for (const auto& kvp : primeFacs) {
                int prime = kvp.first;
                primeIndicesDict[prime].push_back(i);
            }
        }
        UnionFindSet uf(nums.size());
        for (const auto& kvp : primeIndicesDict) {
            const std::vector<int>& indices = kvp.second;
            for (int i = 1; i < indices.size(); ++i) {
                uf.unionSet(indices[0], indices[i]);
            }
        }
        int firstParent = uf.find(0);
        for (int i = 1; i < nums.size(); ++i) {
            if (uf.find(i) != firstParent) return false;
        }
        return true;
    }

    std::unordered_map<int, int> primeFactors(int n) {
        std::unordered_map<int, int> primes;
        while (n % 2 == 0) {
            primes[2] += 1;
            n /= 2;
        }

        int i = 3;
        while (i * i <= n) {
            while (n % i == 0) {
                primes[i] += 1;
                n /= i;
            }
            i += 2;
        }
        if (n > 1) {
            primes[n] += 1;
        }
        return primes;
    }
};

// @lc code=end

