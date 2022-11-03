/*
 * @lc app=leetcode id=1432 lang=csharp
 *
 * [1432] Max Difference You Can Get From Changing an Integer
 */

// @lc code=start
public class Solution 
{
    public int arrayScanning(int[] arr, int def, int startIndex, int forbidden)
    {
        int n = arr.Length;
        int digit = def;
        bool found = false;
        StringBuilder sb = new StringBuilder();
        int current;
        for (int i = 0; i < startIndex; i++)
        {
            sb.Append(arr[i].ToString());
        }
        
        for (int i = startIndex; i < n; i++)
        {
            if (arr[i] != forbidden)
            {
                if (found && arr[i] == digit)
                {
                    current = def;
                }
                else if (!found && arr[i] != def)
                {
                    found = true;
                    digit = arr[i];
                    current = def;
                }
                else
                {
                    current = arr[i];
                }
            }                
            else
            {
                current = arr[i];
            }
            sb.Append(current.ToString());
        }
        return Int32.Parse(sb.ToString());        
    }
    
    public int MaxDiff(int num) 
    {
        int a;
        int b;
        string numString = num.ToString();
        int n = numString.Length;
        int[] numDigits = new int[n];
        int count = 0;
        foreach (char c in numString)
        {
            numDigits[count] = (int)(c - '0');
            count += 1;
        }
        a = arrayScanning(numDigits, 9, 0, 10);
        if (numDigits[0] != 1)
        {
            b = arrayScanning(numDigits, 1, 0, 10);
        }
        else
        {
            b = arrayScanning(numDigits, 0, 1, 1);
        }
        return a - b;
    }
}
// @lc code=end

