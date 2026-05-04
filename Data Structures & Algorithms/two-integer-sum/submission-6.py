class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i in range(0, len(nums)):
            
            complement = target - nums[i]
            if (complement in visited) and (visited[complement] != i):
                return [visited[complement], i]
               
            visited[nums[i]] = i

        
            




    

