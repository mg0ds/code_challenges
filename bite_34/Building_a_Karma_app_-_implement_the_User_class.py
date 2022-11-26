from collections import namedtuple
from datetime import datetime

Transaction = namedtuple(
    'Transaction',
    'giver points date',
    defaults=(None, None, datetime.now()))


class User:
    
    def __init__(self, name):
        self.name = name
        self._transactions = []
        self._fans = []
    
    def name(self):
        return self.name
    
    @property
    def fans(self):
        return len(set(self._fans))
    
    @property
    def karma(self):
        return sum(self._transactions)
    
    @property
    def points(self):
        return self._transactions
        
    def __add__(self, amount):
        self._transactions.append(amount[1])
        self._fans.append(amount[0])
        
    def __str__(self):
        if self.fans == 1:
            return '{} has a karma of {} and 1 fan'.format(self.name, self.karma)
        else:
            return '{} has a karma of {} and {} fans'.format(self.name, self.karma, self.fans)
        
        
        
    
    
    
