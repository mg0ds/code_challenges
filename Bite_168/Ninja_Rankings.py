from dataclasses import dataclass, field
from typing import List, Tuple

bites: List[int] = [283, 282, 281, 263, 255, 230, 216, 204, 197, 196, 195]
names: List[str] = [
    "snow",
    "natalia",
    "alex",
    "maquina",
    "maria",
    "tim",
    "kenneth",
    "fred",
    "james",
    "sara",
    "sam",
]


@dataclass(order = True)
class Ninja:
    """
    The Ninja class will have the following features:

    string: name
    integer: bites
    support <, >, and ==, based on bites
    print out in the following format: [469] bob
    """
    sort_index: int = field(init=False, repr=False)
    name: str
    bites: int

    def __post_init__(self):
        self.sort_index = self.bites
        
    def __str__(self):
        return "[{}] {}".format(self.bites, self.name)
    

@dataclass
class Rankings:
    """
    The Rankings class will have the following features:

    method: add() that adds a Ninja object to the rankings
    method: dump() that removes/dumps the lowest ranking Ninja from Rankings
    method: highest() returns the highest ranking Ninja, but it takes an optional
            count parameter indicating how many of the highest ranking Ninjas to return
    method: lowest(), the same as highest but returns the lowest ranking Ninjas, also
            supports an optional count parameter
    returns how many Ninjas are in Rankings when len() is called on it
    method: pair_up(), pairs up study partners, takes an optional count
            parameter indicating how many Ninjas to pair up
    returns List containing tuples of the paired up Ninja objects
    """

    def __init__(self):
        self._rankings = []
        self.pair_list = []
    
    def add(self, nn):
        self._rankings.append(nn)
        self._rankings = sorted(self._rankings, reverse=True)
        #print(self._rankings)
        
    def __len__(self):
        return len(self._rankings)
        
    def dump(self):
        aa = self._rankings.pop(-1)
        return aa
    
    def highest(self, how_many=1):
        #print(self._rankings)
        return self._rankings[:how_many]
        
    def lowest(self, how_many=1):
        return sorted(self._rankings[-1*how_many:])
        
    def pair_up(self, how_many=3):
        for poz in range(how_many):
            temp_touple = (self._rankings[poz], self._rankings[-(poz+1)])
            self.pair_list.append(temp_touple)
        return self.pair_list
