/*
 * @lc app=leetcode id=1452 lang=csharp
 *
 * [1452] People Whose List of Favorite Companies Is Not a Subset of Another List
 */

// @lc code=start
public class Solution 
{
    public IList<int> PeopleIndexes(IList<IList<string>> favoriteCompanies) 
    {
        int n = favoriteCompanies.Count();
        List<HashSet<string>> preference = new List<HashSet<string>>();
        List<int> result = new List<int>();
        HashSet<int> skip = new HashSet<int>();
        int[] indices = new int[n];
        int[] preferenceSize = new int[n];

        for (int i = 0; i < n; i++)
        {
            preference.Add(new HashSet<string>(favoriteCompanies[i].ToList()));
            indices[i] = i;
            preferenceSize[i] = favoriteCompanies[i].Count;
        }

        Array.Sort(preferenceSize, indices);
        
        for (int i = 0; i < n-1; i++)
        {
            if (!skip.Contains(i))
            {
                int j = i + 1;
                while (j < n)
                {
                    if (preference[indices[i]].IsSubsetOf(preference[indices[j]]))
                    {
                        if (preference[indices[i]].Count == preference[indices[j]].Count)
                        {
                            skip.Add(j);
                        }
                        break;
                    }
                    else
                    {
                        j++;
                    }
                }
                if (j == n)
                {
                    result.Add(indices[i]);
                }
            }
        }

        if (!skip.Contains(n-1))
        {
            result.Add(indices[n-1]);
        }
        result.Sort();
        return result;
    }
}
// @lc code=end

