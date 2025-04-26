#problema 1 leetcode
class Solution(object):
    def twoSum(self, nums, target):
        
        n = len(nums)
        

        for i in range (n):
            for j in range(i+1,n):
                numsij = nums[i] + nums[j]

                if numsij == target:
                    return([i,j])



sol = Solution() # Criar um objeto da classe Solution
print(sol.twoSum([2,7,11,15],9))
