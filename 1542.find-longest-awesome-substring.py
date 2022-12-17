class Solution:
    # To form palindrome, we need: 
    # 1. all appearance being even
    # 2. all appearance except 1 being even
    # And because only have digits, there are only 2^10 possibilities of even odd combinations
    def longestAwesome(self, s: str) -> int:
        hashTable = {}
        hashTable[0] = -1
        palindromes = set()
        palindromes.add(0)
        for i in range(10):
            palindromes.add(1 << i)
        current = 0
        result = 0
        for i, c in enumerate(s):
            current ^= (1 << int(c))
            if current not in hashTable:
                hashTable[current] = i
            for item in palindromes:
                if current ^ item in hashTable:
                    result = max(result, i - hashTable[current ^ item])
        return result