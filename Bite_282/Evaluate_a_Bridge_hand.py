from collections import namedtuple
from enum import Enum
from typing import Sequence

Suit = Enum("Suit", list("SHDC"))
Rank = Enum("Rank", list("AKQJT98765432"))
Card = namedtuple("Card", ["suit", "rank"])

HCP = {Rank.A: 4, Rank.K: 3, Rank.Q: 2, Rank.J: 1}
SSP = {2: 1, 1: 2, 0: 3}  # cards in a suit -> short suit points


class BridgeHand:
    def __init__(self, cards: Sequence[Card]):
        """
        Process and store the sequence of Card objects passed in input.
        Raise TypeError if not a sequence
        Raise ValueError if any element of the sequence is not an instance
        of Card, or if the number of elements is not 13
        """
        self.cards = cards
        if len(self.cards) != 13:
            raise ValueError("Should be 13 cards!")
        if not isinstance(self.cards, list):
            raise TypeError("Not list")
        if None in self.cards:
            raise ValueError("None in cards")
        
        s_list = []
        h_list = []
        d_list = []
        c_list = []
        
        for suit, rank in self.cards:
            if suit._value_ == 1:
                s_list.append(rank)
            elif suit._value_ == 2:
                h_list.append(rank)
            elif suit._value_ == 3:
                d_list.append(rank)
            elif suit._value_ == 4:
                c_list.append(rank)

        #sort suit lists by rank
        s_list = sorted(s_list, key=lambda x: x.value)
        h_list = sorted(h_list, key=lambda x: x.value)
        d_list = sorted(d_list, key=lambda x: x.value)
        c_list = sorted(c_list, key=lambda x: x.value)
        
        #make string representation suit list
        self.s_list_str = "".join([x.name for x in s_list])
        self.h_list_str = "".join([x.name for x in h_list])
        self.d_list_str = "".join([x.name for x in d_list])
        self.c_list_str = "".join([x.name for x in c_list])
        
        self.all_cards = self.s_list_str + self.h_list_str + self.d_list_str + self.c_list_str
        self.cards_list = [self.s_list_str, self.h_list_str, self.d_list_str, self.c_list_str]

    def __str__(self) -> str:
        """
        Return a string representing this hand, in the following format:
        "S:AK3 H:T987 D:KJ98 C:QJ"
        List the suits in SHDC order, and the cards within each suit in
        AKQJT..2 order.
        Separate the suit symbol from its cards with a colon, and
        the suits with a single space.
        Note that a "10" should be represented with a capital 'T'
        """
        hand = ""
        
        if len(self.s_list_str) > 0:
            hand += "S:" + self.s_list_str + " "
        if len(self.h_list_str) > 0:
            hand += "H:" + self.h_list_str + " "
        if len(self.d_list_str) > 0:
            hand += "D:" + self.d_list_str + " "
        if len(self.c_list_str) > 0:
            hand += "C:" + self.c_list_str
        return hand.rstrip()

    @property
    def hcp(self) -> int:
        """ Return the number of high card points contained in this hand """
        hcp_points = 0
        for card in self.all_cards:
            for rank in HCP:
                if card == rank.name:
                    hcp_points += HCP[rank]
        
        return hcp_points

    @property
    def doubletons(self) -> int:
        """ Return the number of doubletons contained in this hand """
        db = 0
        for sc in self.cards_list:
            if len(sc) == 2:
                db += 1
        return db
        

    @property
    def singletons(self) -> int:
        """ Return the number of singletons contained in this hand """
        st = 0
        for sc in self.cards_list:
            if len(sc) == 1:
                st += 1
        return st
        
        
    @property
    def voids(self) -> int:
        """ Return the number of voids (missing suits) contained in
            this hand
        """
        v = 0

        for sc in self.cards_list:
            if len(sc) == 0:
                v += 1
        return v

    @property
    def ssp(self) -> int:
        """ Return the number of short suit points in this hand.
            Doubletons are worth one point, singletons two points,
            voids 3 points
        """
        ssp_points = SSP[2]*self.doubletons + SSP[1]*self.singletons + SSP[0]*self.voids
        
        return ssp_points


    @property
    def total_points(self) -> int:
        """ Return the total points (hcp and ssp) contained in this hand """
        return self.hcp + self.ssp

    @property
    def ltc(self) -> int:
        """ Return the losing trick count for this hand - see bite description
            for the procedure
        """
        ltc_points = 0
        for sc in self.cards_list:
            if len(sc) == 1:
                if sc != "A":
                    ltc_points += 1
            elif len(sc) == 2:
                if sc != "AK":
                    if sc[0] == "A" or sc[0] == "K":
                        ltc_points += 1
                    else:
                        ltc_points += 2
            elif len(sc) > 2:
               if sc[0:3] != "AKQ":
                    if sc[0:2] == "AK" or sc[0:2] == "AQ" or sc[0:2] == "KQ":
                        ltc_points += 1
                    elif sc[0] == "A" or sc[0] == "K" or sc[0] == "Q":
                        ltc_points += 2
                    else:
                        ltc_points += 3
        
        return ltc_points
