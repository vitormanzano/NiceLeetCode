'''
Resolução com 0 ms e 12,69 mb de memória. 100% e 80.24%
'''

class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums)-1

        while ( l <= r):
            m = (l+r)//2

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1

