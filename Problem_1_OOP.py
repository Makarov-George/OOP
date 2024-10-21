

class StringVar(object):
    def __init__(self, string):
        self._string = string
    
    def getstring(self):
        return self._string
    
    def setstring(self, string):
        self._string = string

str = StringVar('first_name')
print(str.getstring())
str.setstring('last_name')
print(str.getstring()) 