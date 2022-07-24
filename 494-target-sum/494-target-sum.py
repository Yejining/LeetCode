class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        dp = [0] * (2 * total + 1)
        dp[nums[0] + total] = 1
        dp[-nums[0] + total] += 1

        for i in range(1, len(nums)):
            next_list = [0] * (2 * total + 1)
            for s in range(-total, total + 1):
                if dp[s + total] > 0:
                    next_list[s + nums[i] + total] += dp[s + total]
                    next_list[s - nums[i] + total] += dp[s + total]

            dp = next_list

        return 0 if abs(target) > total else dp[target + total]