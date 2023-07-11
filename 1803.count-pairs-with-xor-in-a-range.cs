/*
 * @lc app=leetcode id=1803 lang=csharp
 *
 * [1803] Count Pairs With XOR in a Range
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class TrieNode {
    public TrieNode[] Children { get; }
    public int Count { get; set; }

    public TrieNode() {
        Children = new TrieNode[2];
        Count = 0;
    }
}

public class Trie {
    private TrieNode root;
    private int levels;

    public Trie(int levels) {
        root = new TrieNode();
        this.levels = levels;
    }

    public int CountXORPairsSmallerThanK(int num, int k) {
        TrieNode node = root;
        int result = 0;
        int level = levels - 1;

        while (node != null && level >= 0) {
            int ind = ((k ^ num) & (1 << level)) / (1 << level);

            if ((k & (1 << level)) > 0 && node.Children[1 - ind] != null) {
                result += node.Children[1 - ind].Count;
            }

            node = node.Children[ind];
            level--;
        }

        return result;
    }



    public void AddNewNumber(int num) {
        TrieNode node = root;

        for (int i = levels - 1; i >= 0; i--) {
            int digit = (num & (1 << i)) / (1 << i);

            if (node.Children[digit] == null) {
                node.Children[digit] = new TrieNode();
            }

            node = node.Children[digit];
            node.Count++;
        }
    }
}

public class Solution {    
    public static int BitLength(int bits) {
        return (int) (Math.Log(bits, 2)) + 1;
    }
    public int CountPairs(int[] nums, int low, int high) {
        Trie trie = new Trie(BitLength(Math.Max(nums.Max(), high + 1)));
        int[] result = new int[2];
        int[] limit = new int[] { low, high + 1 };

        foreach (int num in nums) {
            for (int j = 0; j < 2; j++) {
                result[j] += trie.CountXORPairsSmallerThanK(num, limit[j]);
            }

            trie.AddNewNumber(num);
        }

        return result[1] - result[0];
    }
}

// @lc code=end

