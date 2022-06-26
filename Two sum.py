class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        
        found = defaultdict(int)
        
        for i, num in enumerate(nums, start=1):
            x = target - num
            if found[x]:
                return [i-1, found[x]-1]
            found[num] = i
        