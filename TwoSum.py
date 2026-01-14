# brute forced solution, searching for a number that is target-currentnum. 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0 
        n = len(nums)
        while i<n:
            y = i
            while (y<(n)):
                if((target-nums[i] == nums[y]) & (i != y)):
                    return [i,y]
                else:
                    y+=1
            i+=1