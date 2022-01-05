class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        lessthan = 0 
        count = 0 
        for n in nums:
                if n < target:
                    lessthan += 1
                elif n == target:
                    count += 1
        return range(lessthan, lessthan+count) 