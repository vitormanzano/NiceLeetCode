class Solution(object):
    def reverse(self, x):
        aux = x
        if aux<0:
            aux = aux*(-1)
            
        sum = 0
        while (aux>0):  
            k = aux%10
            aux = aux//10
            sum +=k
            sum = sum*10
            
        if x<0:
            sum = sum *(-1)
            
        sum = sum//10
        
        if sum >  (2**31) -1 or sum  < -2 ** 31:
            return 0
            
        return sum
