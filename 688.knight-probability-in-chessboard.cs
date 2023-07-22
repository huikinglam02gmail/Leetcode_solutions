/*
 * @lc app=leetcode id=688 lang=csharp
 *
 * [688] Knight Probability in Chessboard
 */

// @lc code=start
public class Solution
{
    /*
    Given n and current position we can calculate the probability for the knight to be at i,j on board for the next round
    Also we do not need to consider fraction. just sum up and divide by pow(8,k)        
    */
    
    private bool InsideBoard(int row, int col, int n)
    {
        return row >= 0 && row < n && col >= 0 && col < n;
    }
    
    public double KnightProbability(int n, int k, int row, int column)
    {
        int[][] possibleSteps = new int[][] {
            new int[] {1, 2},
            new int[] {2, 1},
            new int[] {2, -1},
            new int[] {1, -2},
            new int[] {-1, -2},
            new int[] {-2, -1},
            new int[] {-2, 1},
            new int[] {-1, 2}
        };
        
        List<int[]>[][] destination = new List<int[]>[n][];
        for (int i = 0; i < n; i++)
        {
            destination[i] = new List<int[]>[n];
            for (int j = 0; j < n; j++)
            {
                destination[i][j] = new List<int[]>();
                foreach (int[] possibleStep in possibleSteps)
                {
                    int newRow = i + possibleStep[0];
                    int newCol = j + possibleStep[1];
                    if (InsideBoard(newRow, newCol, n))
                        destination[i][j].Add(new int[] { newRow, newCol });
                }
            }
        }
        
        double[][] dpOld = new double[n][];
        for (int i = 0; i < n; i++)
        {
            dpOld[i] = new double[n];
        }
        dpOld[row][column] = 1;
        
        for (int run = 0; run < k; run++)
        {
            double[][] dpNew = new double[n][];
            for (int i = 0; i < n; i++)
            {
                dpNew[i] = new double[n];
            }
            
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    if (dpOld[i][j] > 0)
                    {
                        foreach (int[] item in destination[i][j])
                        {
                            dpNew[item[0]][item[1]] += dpOld[i][j];
                        }
                    }
                }
            }
            
            dpOld = dpNew;
        }
        
        double result = 0;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                result += dpOld[i][j];
            }
        }
        
        return result / Math.Pow(8, k);
    }
}

// @lc code=end

