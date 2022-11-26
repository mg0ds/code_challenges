from dataclasses import dataclass

@dataclass(order=True)
class Bite:
    #sort_index: int = field(init=False, repr=False)
    
    number: int
    title: str
    level: str = "Beginner"
    
    def __post_init__(self):
        self.title = self.title[0].upper() + self.title[1:].lower()
        self.sort_index = self.number
