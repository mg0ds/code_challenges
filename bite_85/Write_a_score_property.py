SCORES = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
RANKS = 'white yellow orange green blue brown black paneled red'.split()
BELTS = dict(zip(SCORES, RANKS))


class NinjaBelt:
    
    score: int

    def __init__(self, score=0):
        self._score = score
        self._last_earned_belt = None

    def _get_belt(self, new_score):
        """Might be a useful helper"""
        print(new_score)
        i = 0
        msg = "Congrats, you earned {} points obtaining the PyBites Ninja {} Belt"
        previous_belt = self._last_earned_belt
        for sc in SCORES:
            if new_score >= sc:
                self._last_earned_belt = RANKS[i]
            i += 1
        if self._last_earned_belt != previous_belt:
            print(msg.format(new_score, self._last_earned_belt.title()))
        else:
            print("Set new score to {}".format(new_score))
    
    def _get_score(self):
        return self._score

    def _set_score(self, new_score):
        if type(new_score) != int:
            raise ValueError("Score takes an int")
        else:
            if new_score > self._score:
                self._score = new_score
                self._get_belt(new_score)
            else:
                raise ValueError("Cannot lower score")

    score = property(_get_score, _set_score)
    
