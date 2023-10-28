/*
 * @lc app=leetcode id=1220 lang=cpp
 *
 * [1220] Count Vowels Permutation
 */

// @lc code=start
#include <vector>

class Solution {
public:
    /*
    Clearly, a state machine problem
    Should be possible to solve by matrix multiplication!
    dp[n][k]: number of strings of length n that can be formed with end "k"
    k = 0: "a"; k = 1: "e"; k = 2: "i"; k = 3: "o"; k = 4: "u"
    Then construct the transition matrix T:
     [[0,1,1,0,1], 
      [1,0,1,0,0],
      [0,1,0,1,0],
      [0,0,1,0,0],
      [0,0,1,1,0]]
    Then for n, break it down into bit representation
    keep calculating and multiplying two powers of T   
    */

    std::vector<std::vector<long long>> matrixMultiply(const std::vector<std::vector<long long>>& M1, const std::vector<std::vector<long long>>& M2) {
        int m1 = M1.size();
        int n1 = M1[0].size();
        int n2 = M2[0].size();
        std::vector<std::vector<long long>> res(m1, std::vector<long long>(n2, 0));

        for (int i = 0; i < m1; i++) {
            for (int j = 0; j < n2; j++) {
                for (int k = 0; k < n1; k++) {
                    res[i][j] += M1[i][k] * M2[k][j];
                    res[i][j] %= MOD;
                }
            }
        }

        return res;
    }

    const long long MOD = 1000000007;

    int bitLength(int x)
    {
        int count = 0; 
        while (x) 
        { 
            count++; 
            x >>= 1; 
        } 
        return count; 
    }


    int countVowelPermutation(int n) {
        std::vector<std::vector<long long>> seed(5, std::vector<long long>(5, 0));
        for (int i = 0; i < 5; i++) {
            seed[i][i] = 1;
        }

        std::vector<std::vector<long long>> T = {
            {0, 1, 1, 0, 1},
            {1, 0, 1, 0, 0},
            {0, 1, 0, 1, 0},
            {0, 0, 1, 0, 0},
            {0, 0, 1, 1, 0}
        };

        int bl = bitLength(n); // Find the position of the most significant bit
        for (int i = 0; i < bl; i++) {
            if ((n - 1) & (1 << i)) {
                seed = matrixMultiply(T, seed);
            }
            T = matrixMultiply(T, T);
        }

        long long result = 0;
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                result += seed[i][j];
                result %= MOD;
            }
        }

        return static_cast<int>(result);
    }
};


// @lc code=end

