/*
 * @lc app=leetcode id=823 lang=cpp
 *
 * [823] Binary Trees With Factors
 */

// @lc code=start
#include <vector>
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    int numFactoredBinaryTrees(std::vector<int>& arr) {
        std::unordered_map<long long, long long> hashTable;
        for (int num : arr) {
            hashTable[static_cast<long long>(num)] = 1;
        }

        std::vector<long long> keys;
        for (const auto& entry : hashTable) {
            keys.push_back(entry.first);
        }
        std::sort(keys.begin(), keys.end());

        std::unordered_map<long long, std::vector<std::pair<long long, long long>>> products;
        long long MOD = 1000000007;

        for (size_t i = 0; i < keys.size(); i++) {
            for (size_t j = i; j < keys.size(); j++) {
                long long product = keys[i] * keys[j];
                if (hashTable.find(product) != hashTable.end()) {
                    if (products.find(product) == products.end()) {
                        products[product] = std::vector<std::pair<long long, long long>>();
                    }
                    products[product].push_back(std::make_pair(keys[i], keys[j]));
                }
            }
        }

        long long result = 0;
        for (long long key : keys) {
            if (products.find(key) != products.end()) {
                for (const auto& item : products[key]) {
                    hashTable[key] += (hashTable[item.first] * hashTable[item.second]) % MOD;
                    if (item.first != item.second) {
                        hashTable[key] += (hashTable[item.first] * hashTable[item.second]) % MOD;
                    }
                    hashTable[key] %= MOD;
                }
            }
            result += hashTable[key];
            result %= MOD;
        }

        return static_cast<int>(result);
    }
};

// @lc code=end

