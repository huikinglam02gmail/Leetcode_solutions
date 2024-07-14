#
# @lc app=leetcode id=726 lang=python3
#
# [726] Number of Atoms
#

# @lc code=start
class Solution:
    '''
    Because numbers after parentheses mean every value inside the parenthesis gets multiplied by the number, we can use stack to solve the problem.
    formula = "K4(ON(SO3)2)2"
    First read K: 4
    Then put into the stack: [{K: 4}]
    Then read: ON
    Put into the stack:
    [{K:4},{O:1, N:1}]
    Then read SO3
    Then we see a close parenthesis. turn on close_paren
    The number we count afterwards will be applied to the current hash table
    When it becomes not a digit, multiply the number with value inside the current_hash:
    {S: 2, O: 6}
    Then turn off close_paren, pop out from stack and add to current hash
    stack is now [{K:4}], current_hash is now {S:2, O:7, N:1}
    We see a close again. turn on close_paren
    Then we read 2, end of formula
    Final clean up
    multiply the number with value inside hash:
    {S:4, O: 14, N: 2}
    pop stack and add to current hash:
    {K:4, S:4, O: 14, N: 2}   
    '''

    def cleanup(self, hash_table):
        if len(self.name) > 0:
            if self.number == 0: self.number += 1
            hash_table[self.name] = hash_table.get(self.name, 0) + self.number
            self.name = ""
            self.number = 0
        return hash_table
    
    def paren_cleanup(self, hash_table):
        if self.number == 0: self.number += 1
        for key in hash_table.keys(): hash_table[key] *= self.number
        prev_hash = self.stack.pop()
        for key in prev_hash.keys(): hash_table[key] = hash_table.get(key, 0) + prev_hash[key]
        self.name = ""
        self.number = 0
        return hash_table
    
    def countOfAtoms(self, formula: str) -> str:
        self.stack = []
        self.name, self.number = "", 0
        current_hash = {}
        close_paren = False
        for c in formula:
            if c.isdigit():
                self.number *= 10
                self.number += int(c)
            else:
                if close_paren:
                    current_hash = self.paren_cleanup(current_hash)
                    close_paren = False
                if c.islower(): self.name += c
                else:
                    current_hash = self.cleanup(current_hash)
                    if c.isupper(): self.name += c
                    elif c == "(":
                        self.stack.append(current_hash)
                        current_hash = {}
                    elif c == ")": close_paren = True
        if close_paren:
            current_hash = self.paren_cleanup(current_hash)
            close_paren = False
        else:
            current_hash = self.cleanup(current_hash)
        result = ''
        for key in sorted(current_hash.keys()):
            result += key
            if current_hash[key] > 1: result += str(current_hash[key])
        return result
# @lc code=end

