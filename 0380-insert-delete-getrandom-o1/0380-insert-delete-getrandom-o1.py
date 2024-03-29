class RandomizedSet(object):

    def __init__(self):
        self.S = set()

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.S:
            return False
        else :
            self.S.add(val)
            return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.S:
            self.S.remove(val)
            return True
        else :
            return False
        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(list(self.S))
        




