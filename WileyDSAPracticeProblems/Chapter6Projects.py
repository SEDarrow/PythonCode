#P-6.32
""" Give a complete ArrayDeque implementation of the double-ended queue
ADT as sketched in Section 6.3.2. """
class ArrayDeque():
    DEFAULT_SIZE = 10
    
    def __init__(self):
        self.queue = [None]*self.DEFAULT_SIZE
        self.front = 1
        self.size = 0
        
    def addFirst(self, data):
        self.size += 1
        if(self.size > len(self.queue)):
            self._resize(2)
        index = (self.front-1) % (len(self.queue))
        self.queue[index] = data
        self.front = index
        return           
        
    def addLast(self, data):
        self.size += 1
        if(self.size > len(self.queue)):
            self._resize(2)
        index = (self.front+self.size-1) % (len(self.queue))
        self.queue[index] = data
        return  
        
    def getFirst(self):
        return self.queue[self.front]
    
    def getLast(self):
        return self.queue[(self.front+self.size-1) % (len(self.queue))]
    
    def removeFirst(self):
        self.size = self.size-1
        first = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front+1)%len(self.queue)
        return first
    
    def removeLast(self):
        last = self.queue[(self.front+self.size-1) % (len(self.queue))]
        self.queue[(self.front+self.size-1) % (len(self.queue))] = None
        self.size = self.size-1
        return last
    
    def getLength(self):
        return self.size
    
    def _resize(self, n):
        new = [None]*(self.size*n)
        curr = self.front
        for each in range(self.size):
            new[each] = self.queue[curr % (len(self.queue))]
            curr+=1
        self.queue = new
        self.front = 0
        self.last = self.size-1
        
    def __str__(self):
        return str(self.queue)
    
#P-6.35
""" The introduction of Section 6.1 notes that stacks are often used to provide
“undo” support in applications like a Web browser or text editor. While
support for undo can be implemented with an unbounded stack, many
applications provide only limited support for such an undo history, with a
fixed-capacity stack. When push is invoked with the stack at full capacity,
rather than throwing a Full exception (as described in Exercise C-6.16),
a more typical semantic is to accept the pushed element at the top while
“leaking” the oldest element from the bottom of the stack to make room.
Give an implementation of such a LeakyStack abstraction, using a circular
array with appropriate storage capacity. This class should have a public
interface similar to the bounded-capacity stack in Exercise C-6.16, but
with the desired leaky semantics when full"""
class LeakyStack:
    DEFAULT_SIZE = 10
    def __init__(self):
        self.stack = [None]*self.DEFAULT_SIZE
        self.top = -1
        self.size = 0
        
    def push(self, data):
        self.stack[(self.top+1)%len(self.stack)] = data
        self.top = (self.top+1)%len(self.stack)
        self.size +=1
    
    def pop(self):
        data = self.stack[self.top]
        self.stack[self.top] = None
        self.top = (self.top-1)%len(self.stack)
        return data
        
    def __str__(self):
        return str(self.stack)
