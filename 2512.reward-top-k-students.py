#
# @lc app=leetcode id=2512 lang=python3
#
# [2512] Reward Top K Students
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        positives, negatives = set(), set()
        for pos in positive_feedback: positives.add(pos)
        for neg in negative_feedback: negatives.add(neg)
        
        hashTable = {}
        for sentence, id in sorted(zip(report, student_id), key = lambda x: x[1]):
            sentenceSplit = sentence.split(" ")
            score = 0
            for word in sentenceSplit:
                if word in positives: score += 3
                if word in negatives: score -= 1
            if score not in hashTable: hashTable[score] = []
            hashTable[score].append(id)
        result = []
        for key1, idList in sorted(hashTable.items(), key = lambda x : - x[0]):
            for id in idList:
                if len(result) < k: result.append(id)
        return result
# @lc code=end
