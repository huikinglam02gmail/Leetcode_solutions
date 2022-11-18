/*
 * @lc app=leetcode id=1476 lang=csharp
 *
 * [1476] Subrectangle Queries
 */

// @lc code=start
public class SubrectangleQueries {

    List<int[]> modified;
    int[][] Rectangle;
    public SubrectangleQueries(int[][] rectangle) {
        modified = new List<int[]>();
        Rectangle = rectangle;
    }
    
    public void UpdateSubrectangle(int row1, int col1, int row2, int col2, int newValue) {
        modified.Add(new int[5] {row1, col1, row2, col2, newValue});
    }
    
    public int GetValue(int row, int col) {
        int n = modified.Count;
        for (int i = n-1; i >= 0; i--)
        {
            if (modified[i][0] <= row && row <= modified[i][2] && modified[i][1] <= col && col <= modified[i][3])
            {
                return modified[i][4];
            }
        }
        return Rectangle[row][col];
    }
}

/**
 * Your SubrectangleQueries object will be instantiated and called as such:
 * SubrectangleQueries obj = new SubrectangleQueries(rectangle);
 * obj.UpdateSubrectangle(row1,col1,row2,col2,newValue);
 * int param_2 = obj.GetValue(row,col);
 */
// @lc code=end

