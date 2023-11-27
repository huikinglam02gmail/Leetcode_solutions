/*
 * @lc app=leetcode id=935 lang=csharp
 *
 * [935] Knight Dialer
 */

// @lc code=start
public class Solution {
    private static long MOD = 1000000007;
    
    private long[,] MatrixMultiply(long[,] A, long[,] C) {
        int n = A.GetLength(0);
        long[,] B = new long[n, n];
        
        for (int i = 0; i < n; i++) {            
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    B[i, j] += A[i, k] * C[k, j];
                    B[i, j] %= MOD;
                }
            }
        }
        
        return B;
    }
    
    public static int bitLength(int bits)
    {
        var size = 0;
        while(bits != 0)
        {
            bits >>= 1;
            size++;
        }
        return size;
    }

    public int KnightDialer(int n) {
        

        long[,] M = {
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
        
        long[,] seed = new long[10,10];
        for (int i = 0; i < 10; i++) {
            for (long j = 0; j < 10; j++) {
                seed[i, j] = (i == j) ? 1 : 0;
            }
        }
        
        for (int i = 0; i < bitLength(n - 1); i++) {
            if (((n - 1) & (1 << i)) != 0) {
                seed = MatrixMultiply(seed, M);
            }
            M = MatrixMultiply(M, M);
        }
        
        long result = 0;
        for (int j = 0; j < 10; j++) {
            for (int k = 0; k < 10; k++) {
                result += seed[j, k];
                result %= MOD;
            }
        }
        
        return Convert.ToInt32(result);
    }
}

// @lc code=end

