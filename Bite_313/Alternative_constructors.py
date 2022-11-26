import re


class DomainException(Exception):
    """Raised when an invalid is created."""


class Domain:
  
    # next add a __str__ method and write 2 class methods
    # called parse_url and parse_email to construct domains
    # from an URL and email respectively

    def __init__(self, name):
        # validate a current domain (r'.*\.[a-z]{2,3}$' is fine)
        # if not valid, raise a DomainException
        self.name = name
        if re.findall('.*\.[a-z]{2,3}$', self.name) == []:
            raise DomainException()
        
        
    def __str__(self):
        return f"{self.name}"
    
    @classmethod
    def parse_url(cls, url):
        domain = re.findall(':/.([\w\-\.]+)', url)
        return cls(domain[0])

    
    @classmethod
    def parse_email(cls, email):
        domain = re.findall('@([\w\-\.]+)', email) 
        return cls(domain[0])
