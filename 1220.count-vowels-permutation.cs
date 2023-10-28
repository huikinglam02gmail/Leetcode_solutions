/*
 * @lc app=leetcode id=1220 lang=csharp
 *
 * [1220] Count Vowels Permutation
 */

// @lc code=start
public class Solution
{
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

    private long[,] MatrixMultiply(long[,] M1, long[,] M2)
    {
        int m1 = M1.GetLength(0);
        int n1 = M1.GetLength(1);
        int n2 = M2.GetLength(1);
        long[,] res = new long[m1, n2];

        for (int i = 0; i < m1; i++)
        {
            for (int j = 0; j < n2; j++)
            {
                for (int k = 0; k < n1; k++)
                {
                    res[i, j] += M1[i, k] * M2[k, j];
                    res[i, j] %= MOD;
                }
            }
        }

        return res;
    }

    private const long MOD = 1000000007;

    public int CountVowelPermutation(int n)
    {
        long[,] seed = new long[5, 5];
        for (int i = 0; i < 5; i++)
        {
            seed[i, i] = 1;
        }

        long[,] T = {
            {0, 1, 1, 0, 1},
            {1, 0, 1, 0, 0},
            {0, 1, 0, 1, 0},
            {0, 0, 1, 0, 0},
            {0, 0, 1, 1, 0}
        };

        int bl = Convert.ToString(n - 1, 2).Length;
        for (int i = 0; i < bl; i++)
        {
            if (((n - 1) & (1 << i)) != 0)
            {
                seed = MatrixMultiply(T, seed);
            }
            T = MatrixMultiply(T, T);
        }

        long result = 0;
        for (int i = 0; i < 5; i++)
        {
            for (int j = 0; j < 5; j++)
            {
                result += seed[i, j];
                result %= MOD;
            }
        }

        return Convert.ToInt32(result);
    }
}
// @lc code=end

