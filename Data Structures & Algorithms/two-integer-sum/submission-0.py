class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index={}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in index:
                index[nums[i]]=i  
            else:
                return [index[diff], i]