class Animal:
    names_list = []
    j = 10000
    
    def __init__(self, name):
        self.name = name
        self.names_list.append(self.name.title())

            

    def __str__(self):
        return str(self.j + len(self.names_list)) + ". " + self.names_list[-1]

    @classmethod
    def zoo(cls):
        j = 10000
        names_string = ""
        for i in cls.names_list:
            j += 1
            if names_string == "":
                names_string = str(j) + ". " + i
            else:
                names_string = names_string + "\n" + str(j) + ". " + i
        return names_string
            
