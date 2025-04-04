class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        upp = word.upper()
        low = word.lower()

        if word == upp:
            return True
        elif word == low:
            return True
        elif len(word) > 1 and word == upp[0]+low[1:]:
            return True
        else:
            return False