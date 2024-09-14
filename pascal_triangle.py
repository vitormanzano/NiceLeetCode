class Solution(object):
    def generate(self, numRows):
        vet = []
        for i in range(numRows):
            vet0=[]
            for j in range(i+1):
                if j==0 or j==i:
                    vet0.append(1)
                else:
            
                    vet0.append(vet[i-1][j-1]+vet[i-1][j])
                
            vet.append(vet0)
        return vet
