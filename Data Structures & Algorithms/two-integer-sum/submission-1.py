class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for key, value in enumerate(nums):
            difference = target - value
            if difference in hashMap:
                return [hashMap[difference], key]
            hashMap[value] = key
