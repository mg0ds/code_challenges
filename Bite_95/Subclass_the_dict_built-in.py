from datetime import date

MSG = 'Hey {}, there are more people with your birthday!'


class BirthdayDict(dict):
    """Override dict to print a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""
    
    def __setitem__(self, name, birthday):
        for k, v in self.__dict__.items():
            if v.month == birthday.month and v.day == birthday.day:
                print(MSG.format(name))
        self.__dict__[name] = birthday
