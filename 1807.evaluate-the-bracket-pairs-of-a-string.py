#
# @lc app=leetcode id=1807 lang=python3
#
# [1807] Evaluate the Bracket Pairs of a String
#

# @lc code=start
class Solution:
    '''
    use stack to hold previous string, when seeing "(". pop when seeing ")"
    '''
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        hashTable = {a: b for a, b in knowledge}

        stack = []
        current = ""
        for c in s:
            if c == "(":
                stack.append(current)
                current = ""
            elif c == ")":
                current = stack.pop() + hashTable.get(current, "?")
            else:
                current += c
        return current
        
        
# @lc code=end

