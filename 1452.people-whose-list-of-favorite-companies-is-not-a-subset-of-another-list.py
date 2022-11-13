#
# @lc app=leetcode id=1452 lang=python3
#
# [1452] People Whose List of Favorite Companies Is Not a Subset of Another List
#

# @lc code=start
class Solution:
    # Use hash set to store each person's preference
    # Use issubset to check if each pair completely overlap

    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        n = len(favoriteCompanies)
        preference = [set(choice) for choice in favoriteCompanies]
        sortedIndices = [x[0] for x in sorted(enumerate(preference), key = lambda x: len(x[1]))]
        result = set()
        skip = set()
        for i in range(n-1):
            if i not in skip:
                j = i+1
                while j < n:
                    if preference[sortedIndices[i]].issubset(preference[sortedIndices[j]]):
                        if len(preference[sortedIndices[i]]) == len(preference[sortedIndices[j]]):
                            skip.add(j)
                        break
                    else:
                        j += 1
                if j == n:
                    result.add(sortedIndices[i])
        if n-1 not in skip:
            result.add(sortedIndices[n-1])
        return sorted(list(result))
# @lc code=end

