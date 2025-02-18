class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        
        if maxChoosableInteger >= desiredTotal :
            return True
        
        if int(maxChoosableInteger * (maxChoosableInteger+1) / 2) < desiredTotal :
            return False
        
        if int(maxChoosableInteger * (maxChoosableInteger+1) / 2) == desiredTotal :
            return (maxChoosableInteger % 2 == 1)
        
        self.rec = {}

        return self.can_I_win_the_game(tuple(range(1, maxChoosableInteger+1)), desiredTotal)

    def can_I_win_the_game(self, nums, target):
        if nums[-1] >= target :
            return True
        
        if nums in self.rec :
            return self.rec[nums]

        for i in range(len(nums)):
            if not self.can_I_win_the_game(nums[:i]+nums[i+1:], target - nums[i]):
                self.rec[nums] = True
                return True
        
        self.rec[nums] = False
        return False