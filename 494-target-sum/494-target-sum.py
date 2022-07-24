class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total, target = sum(nums), -target if target < 0 else target
        num = int((total + target) / 2)
        if not float((total + target) / 2).is_integer(): return 0

        zero_len = sum([1 for i in nums if i == 0])
        zero_ways = 2 ** zero_len

        nums = [i for i in nums if i != 0]
        
        if len(nums) == 0: return zero_ways
        if len(nums) == 1 and nums[0] == target: return 1 * zero_ways
        return sum([1 for i in range(len(nums)) for x in combinations(nums, i) if sum(x) == num]) * zero_ways
