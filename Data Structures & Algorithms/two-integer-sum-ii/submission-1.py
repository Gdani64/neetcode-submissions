class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numbers list is sorted in ascending order
        # brute force version
        # for l in range(len(numbers)):
        #     for r in range(l+1,len(numbers)):
        #         if numbers[l] + numbers[r] == target:
        #             return [l+1,r+1]
        
        l = 0
        r = len(numbers) - 1

        while True:
            if numbers[l] + numbers[r] == target:
                return [l+1,r+1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1
        

        


