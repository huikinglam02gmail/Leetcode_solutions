/*
 * @lc app=leetcode id=935 lang=cpp
 *
 * [935] Knight Dialer
 */

// @lc code=start
#include <cmath>
#include <vector>

class Solution {
private:
    long long MOD =  (long long)1000000007;
public:

    std::vector<std::vector<long long>> MatrixMultiply(const std::vector<std::vector<long long>>& A, const std::vector<std::vector<long long>>& C) {
        int n = A.size();
        std::vector<std::vector<long long>> B(n, std::vector<long long>(n, (long long)0));

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    B[i][j] += A[i][k] * C[k][j];
                    B[i][j] %= MOD;
                }
            }
        }

        return B;
    }

    int bitLength(int bits){
        int size = 0;
        while(bits != 0){
            bits >>= 1;
            size++;
        }
        return size;       
    }

    int knightDialer(int n) {

        std::vector<std::vector<long long>> M = {
            {0, 0, 0, 0, 1, 0, 1, 0, 0, 0},
            {0, 0, 0, 0, 0, 0, 1, 0, 1, 0},
            {0, 0, 0, 0, 0, 0, 0, 1, 0, 1},
            {0, 0, 0, 0, 1, 0, 0, 0, 1, 0},
            {1, 0, 0, 1, 0, 0, 0, 0, 0, 1},
            {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
            {1, 1, 0, 0, 0, 0, 0, 1, 0, 0},
            {0, 0, 1, 0, 0, 0, 1, 0, 0, 0},
            {0, 1, 0, 1, 0, 0, 0, 0, 0, 0},
            {0, 0, 1, 0, 1, 0, 0, 0, 0, 0}
        };

        std::vector<std::vector<long long>> seed(10, std::vector<long long>(10, (long long)0));
        for (int i = 0; i < 10; i++) {
            seed[i][i] = 1;
        }

        for (int i = 0; i < bitLength(n - 1); i++) {
            if ((n - 1) & (1 << i)) {
                seed = MatrixMultiply(seed, M);
            }
            M = MatrixMultiply(M, M);
        }

        long long result = 0;
        for (int j = 0; j < 10; j++) {
            for (int k = 0; k < 10; k++) {
                result += seed[j][k];
                result %= MOD;
            }
        }

        return (int)result;
    }
};

// @lc code=end

