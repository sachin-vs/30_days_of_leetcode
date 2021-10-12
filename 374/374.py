# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        min,max=1,n
        while min<=max:
            mid=min+(max-min)//2
            if guess(mid)==0:return mid
            elif guess(mid)==1:min=mid+1
            else:max=mid-1