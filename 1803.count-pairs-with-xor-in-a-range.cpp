/*
 * @lc app=leetcode id=1803 lang=cpp
 *
 * [1803] Count Pairs With XOR in a Range
 */

// @lc code=start
#include <vector>
#include <unordered_map>
#include <cmath>

using namespace std;

class TrieNode {
public:
    TrieNode* children[2];
    int count;

    TrieNode() {
        children[0] = nullptr;
        children[1] = nullptr;
        count = 0;
    }
};

class Trie {
private:
    TrieNode* root;
    int levels;

public:
    Trie(int levels) {
        root = new TrieNode();
        this->levels = levels;
    }

    int countXORPairsSmallerThanK(int num, int k) {
        TrieNode* node = root;
        int result = 0;
        int level = levels - 1;

        while (node != nullptr && level >= 0) {
            int ind = ((k ^ num) & (1 << level)) / (1 << level);

            if ((k & (1 << level)) > 0 && node->children[1 - ind] != nullptr) {
                result += node->children[1 - ind]->count;
            }

            node = node->children[ind];
            level--;
        }

        return result;
    }

    void addNewNumber(int num) {
        TrieNode* node = root;

        for (int i = levels - 1; i >= 0; i--) {
            int digit = (num & (1 << i)) / (1 << i);

            if (node->children[digit] == nullptr) {
                node->children[digit] = new TrieNode();
            }

            node = node->children[digit];
            node->count++;
        }
    }
};

class Solution {
public:
    static int bitLength(int bits) {
        return (int) (log2(bits)) + 1;
    }

    int countPairs(vector<int>& nums, int low, int high) {
        Trie trie(bitLength(max(*max_element(nums.begin(), nums.end()), high + 1)));
        int result[2] = {0, 0};
        int limit[2] = {low, high + 1};

        for (int num : nums) {
            for (int j = 0; j < 2; j++) {
                result[j] += trie.countXORPairsSmallerThanK(num, limit[j]);
            }

            trie.addNewNumber(num);
        }

        return result[1] - result[0];
    }
};

// @lc code=end

