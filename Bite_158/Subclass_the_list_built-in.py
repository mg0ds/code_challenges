class IntList(list):
    
    def __init__(self, mylist):
        self.mylist = mylist
        
    @property
    def mean(self):
        return sum(self.mylist)/len(self.mylist)
        
    @property
    def median(self):
        if len(self.mylist)%2 == 0:
            return (sorted(self.mylist)[int((len(self.mylist)/2))] + sorted(self.mylist)[int((len(self.mylist)/2)-1)])/2
        else:
            return sorted(self.mylist)[int((len(self.mylist)/2))]
    
    def append(self, new_number):
        if isinstance(new_number, str):
            raise TypeError
        else:
            self.mylist.append(int(new_number))
            
    def __add__(self, other):
        for a in other:
            if isinstance(a, str):
                raise TypeError
            else:
                self.mylist.append(a)
        return self.mylist
                
    def __iadd__(self, other):
        for a in other:
            if isinstance(a, str):
                raise TypeError
            else:
                self.mylist.append(a)
        return self.mylist
