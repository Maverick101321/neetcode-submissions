class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_sum = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev_sum:
                return [prev_sum[diff], i]
            prev_sum[n] = i