'''
  0ms / beats 100%
  12.03mb / beats 90%
'''

class Solution(object):
    def searchInsert(self, nums, target):
        l,r = 0,len(nums)-1

        while ( l <= r):
            m = (l+r)//2

            if ( nums[m] > target):
                r = m-1
            elif nums[m] < target:
                l = m+1
            else:
                return m
        return l
        
  
