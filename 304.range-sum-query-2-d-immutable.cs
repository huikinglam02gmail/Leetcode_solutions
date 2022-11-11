/*
 * @lc app=leetcode id=304 lang=csharp
 *
 * [304] Range Sum Query 2D - Immutable
 */

// @lc code=start
public class NumMatrix 
{
    int[][] prefixSum;

    public NumMatrix(int[][] matrix) 
    {
        int m = matrix.Length;
        int n = matrix[0].Length;
        prefixSum = new int[m+1][];

        for (int i=0; i<m+1; i++)
        {
            prefixSum[i] = new int[n+1];
            for (int j=0; j<n+1; j++)
            {
                if (i == 0 || j == 0)
                {
                    prefixSum[i][j] = 0;
                }
                else
                {
                    prefixSum[i][j] = prefixSum[i-1][j] + prefixSum[i][j-1] + matrix[i-1][j-1] - prefixSum[i-1][j-1];
                }
            }
        }   
    }
    
    public int SumRegion(int row1, int col1, int row2, int col2) 
    {
        return prefixSum[row2+1][col2+1] - prefixSum[row1][col2+1] - prefixSum[row2+1][col1] + prefixSum[row1][col1];
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.SumRegion(row1,col1,row2,col2);
 */
// @lc code=end

