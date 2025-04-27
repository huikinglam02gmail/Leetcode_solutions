#
# @lc app=leetcode id=3527 lang=python3
#
# [3527] Find the Most Common Response
#

# @lc code=start
from typing import List


class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        setResponses = [set(response) for response in responses]
        occur = {}
        for setResponse in setResponses:
            for response in setResponse: occur[response] = occur.get(response, 0) + 1
        data = [[v, k] for k, v in occur.items()]
        data.sort(key = lambda x: [-x[0] , x[1]])
        return data[0][1] 
# @lc code=end

