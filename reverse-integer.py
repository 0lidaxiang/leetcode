# Answer 1: 
class Solution:
    def reverse(self, x: int) -> int:
        
        if x >= 0:
            strs=str(x)
            ret=int(strs[::-1])
            if ret >= 2**31-1:
                return 0
            return ret
        else:
            strs=str(x)[1:]
            ret = -1*int(strs[::-1])
            if ret <= -2**31:
                return 0
            return ret