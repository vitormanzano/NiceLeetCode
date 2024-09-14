class Solution(object):
    def isPalindrome(self, x):
        s = 0
        aux = x
        
        while aux>0:
            
            k = aux%10
            s = s+k
            aux =aux//10
            
            if aux==0:
                break
            s =s*10
            
        if s==x:
            return True
        else:
            return False
            
