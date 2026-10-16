class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen={}
        dict=[]
        for num in nums:
            if num in seen:
                if seen[num]==1:
                    dict.append(num)
                seen[num]+=1
            else:
                seen[num]=1
        if dict:
            return True

        return False