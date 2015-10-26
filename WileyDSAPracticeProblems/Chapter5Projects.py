#P-6.32
class ArrayDeque():
    def __init__(self):
        self._data = []
    
    def isEmpty(self):
        return len(self._data) == 0
    
    def enque(self, data):
        self._data.append(data)
        
class Test():
    def __init__(self, val1, val2):
        self.__secretVal = val1
        self._protectedVal = val2
    def getSecret(self):
        return self.__secretVal
    
class CNT():
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
    def __str__(self):
        return str(self.a)+' + '+str(self.b)
    def magnitude(self):
        return (self.a**2 + self.b**2)**(1/2)
    