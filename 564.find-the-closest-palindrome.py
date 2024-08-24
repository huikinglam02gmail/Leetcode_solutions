#
# @lc app=leetcode id=564 lang=python3
#
# [564] Find the Closest Palindrome
#

# @lc code=start
class Solution:
    '''
    Consider the Candidates:
    1. if the number is close to 10^k: 999 -> 1001; 1000 -> 999
    therefore, look at nearby 10^k +- 1
    2. for "normal" numbers like 1234 or 12932:
    a. odd string length:
    possibilities: 12821, 12921, 13031
    b. even string length:
    possibilities: 1221, 1111, 1331        
    '''    
    def nearestPalindromic(self, n: str) -> str:
        n_l = len(n)
        candidates = set()
        mid = n_l // 2
        prefix = n[:mid]
        if n_l % 2 == 0:
            if prefix + prefix[::-1] != n: candidates.add(prefix + prefix[::-1])
            candidates.add(str(int(prefix) - 1) + str(int(prefix) - 1)[::-1])
            candidates.add(str(int(prefix) + 1) + str(int(prefix) + 1)[::-1])            
        else:
            seed = prefix + n[mid] + prefix[::-1]
            if n[mid] != "0": candidates.add(str(int(seed) - pow(10, n_l - mid - 1)))
            elif len(n) > 1: candidates.add(str(int(prefix) - 1) + "9" + str(int(prefix) - 1)[::-1])
            if n[mid] != "9": candidates.add(str(int(seed) + pow(10, n_l - mid - 1)))
            elif len(n) > 1: candidates.add(str(int(prefix)+1) + "0" + str(int(prefix) + 1)[::-1])                
            if seed != n: candidates.add(seed)
        if n[0] == "1":
            seed = int(n[0]) * pow(10, len(n) - 1)
            candidates.add(str(seed - 1))
        elif n[0] == "9":
            seed = (int(n[0]) + 1) * pow(10, len(n) - 1)
            candidates.add(str(seed + 1))
        min_diff = float("inf")
        result = "0"
        for candidate in candidates:
            if abs(int(candidate) - int(n)) < min_diff:
                result = candidate
                min_diff = abs(int(candidate) - int(n))
            elif abs(int(candidate) - int(n)) == min_diff and int(candidate) < int(result): result = candidate
        return result
# @lc code=end

