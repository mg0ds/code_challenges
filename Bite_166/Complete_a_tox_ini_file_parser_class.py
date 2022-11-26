import configparser


class ToxIniParser:

    def __init__(self, ini_file):
        """Use configparser to load ini_file into self.config"""
        self.config = configparser.ConfigParser()
        self.config.read(ini_file)
        pass

    @property
    def number_of_sections(self):
        """Return the number of sections in the ini file.
           New to properties? -> https://pybit.es/property-decorator.html
        """
        self.sections = self.config.sections()
        a = [_ for _ in self.sections]
        #print(a)
        return len(a)


    @property
    def environments(self):
        """Return a list of environments
           (= "envlist" attribute of [tox] section)"""
        self.envlist = self.config["tox"]["envlist"]
        self.envlist = self.envlist.replace("\n", ",")
        self.b = [_.strip() for _ in self.envlist.split(",")]
        self.b = [_ for _ in self.b if _]
        #print(b)
        return self.b
        

    @property
    def base_python_versions(self):
        """Return a list of all basepython across the ini file"""
        #self.basepython = self.config["testenv:"+[_ for _ in self.b]]
        python_list = []
        for _ in self.b:
            try:
                #self.basepython = self.config["testenv:"+_]["basepython"]
                python_list.append(self.config["testenv:"+_]["basepython"])
                #basepython_set = set(self.basepython)
                #print(python_list)
            except:
                continue
        return set(python_list)
        #print(self.basepython)
