/*
 * @lc app=leetcode id=1081 lang=csharp
 *
 * [1081] Smallest Subsequence of Distinct Characters
 */

// @lc code=start
public class Solution {
    private List<List<int>> appear = new List<List<int>>(26);
    private int lastUsedIndex = -1;
    public string SmallestSubsequence(string s) {
        for (int i = 0; i < 26; i++) {
            appear.Add(new List<int>());
        }

        PriorityQueue<char, int> needProcess = new PriorityQueue<char, int>();

        for (int i = 0; i < s.Length; i++) {
            int ind = s[i] - 'a';
            if (appear[ind].Count == 0) {
                needProcess.Enqueue(s[i], ind);
            }
            appear[ind].Add(i);
        }

        string result = "";
        Stack<char> temp = new Stack<char>();

        while (needProcess.TryDequeue(out char c, out int ind)) 
        {
            if (!CanUseThisCharacter(ind)) {
                temp.Push(c);
            } else {
                result += c;
                appear[ind].Clear();
                while (temp.Count > 0) 
                {
                    char cTemp = temp.Pop();
                    needProcess.Enqueue(cTemp, (int) (cTemp - 'a'));
                }
            }
        }

        return result;
    }

    private bool CanUseThisCharacter(int i) {
        int ind = appear[i][bisectLeft<int>(appear[i], lastUsedIndex)];
        for (int j = 0; j < appear.Count; j++) 
        {
            if (j != i && appear[j].Count > 0 && bisectLeft<int>(appear[j], ind) == appear[j].Count) {
                return false;
            }
        }
        lastUsedIndex = ind;
        appear[i].Clear();
        return true;
    }

    public static int bisectLeft<T>(IList<T> arr, T x, int lo=0, int hi=-1) where T : IConvertible, IComparable, IComparable<T>, IEquatable<T>
    {
        hi = (hi == -1) ? arr.Count : hi;
        while (lo < hi)
        {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid].CompareTo(x) < 0)
            {
                lo = mid + 1;
            }
            else
            {
                hi = mid;
            }
        }
        return lo;     
    }
}
// @lc code=end

