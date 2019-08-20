"""
link: https://leetcode-cn.com/problems/two-sum/submissions/
"""

# Answer 1:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)-1):
            x = nums[i]
            for j in range(i+1, len(nums)):
                y = nums[j]
                if x+y == target:
                    return [i, j]              

# Answer 2:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tul = dict()
        for i in range(0,len(nums)):
            x = nums[i]
            y = target -x
            if y not in tul.keys():
                tul[x] = i
            else:
                return [tul[y], i]        

# Answer 3: 最快
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = dict()
        for i, x in enumerate(nums):
            if dic.get(target -x)  is None:
                dic[x] = i
            else:
                return [dic.get(target -x) , i]