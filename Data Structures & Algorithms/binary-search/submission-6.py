class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) < 2:
            if nums[0] == target:
                return 0
            else:
                return -1

        def divide_and_conquer(start: int, end: int):
            print(start, end)
            if len(nums[start:end+1]) < 2:
                return -1
            if len(nums[start:end+1]) == 2:
                if nums[start] == target:
                    return start
                elif nums[end] == target:
                    return end
                else:
                    return -1

            mid_point = (start+end) // 2
            print(mid_point)
            if nums[mid_point] == target:
                return mid_point
            elif nums[mid_point] < target:
                return divide_and_conquer(mid_point,end)
            else:
                return divide_and_conquer(start,mid_point)
        
        return divide_and_conquer(0,len(nums)-1)