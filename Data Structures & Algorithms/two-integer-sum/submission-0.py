class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_sum = {}
        for i, n in enumerate(nums):
            dif = target - n
            if dif in prev_sum:
                return [prev_sum[dif], i]
            prev_sum[n] = i