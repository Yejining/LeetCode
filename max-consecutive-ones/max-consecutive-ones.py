class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count = 0

        for i, elem in enumerate(nums):
            if elem == 1:
                count += 1
                continue
            
            max_count = max(count, max_count)
            count = 0

        return max(count, max_count)