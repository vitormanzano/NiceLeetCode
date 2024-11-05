class Solution(object):
    def lengthOfLastWord(self, s):
        palavra = s.strip().split()

        if not palavra:
            return 0
        return len(palavra[-1])
