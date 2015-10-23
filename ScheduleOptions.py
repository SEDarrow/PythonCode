class Node():
    def __init__(self, data=None, nextNode=None, prevNode=None):
        self.data = data
        self.nextNode = nextNode
        self.prevNode = prevNode
        
    def getData(self):
        return self.data
    def setData(self, data):
        self.data = self
        
    def getNext(self):
        return self.nextNode
    def setNext(self, nextNode):
        self.nextNode = nextNode   
        
    def getPrev(self):
        return self.nextPrev
    def setPrev(self, nextPrev):
        self.nextPrev = nextPrev     

class LinkedList():
    def __init__(self):
        self.first = Node(None)
        self.last = Node(None, None, self.first)
        self.first.setNext(self.last)
    
    def add(self, data):
        newNode = Node(data, self.first.getNext(), self.first)
        self.first.getNext().setPrev(newNode)
        self.first.setNext(newNode)
        
    def append(self, data):
        newNode = Node(data, self.last, self.last.getPrev())
        self.last.getPrev().setNext(newNode)
        self.last.setPrev(newNode)
        
    def insert(self, data, aNode):
        newNode = Node(data, aNode.getNext(), aNode)
        aNode.getNext().setPrev(newNode)
        aNode.setNext(newNode)
        
    def getNode(self,index):
        currNode = self.first
        for each in range(0, index):
            currNode = currNode.getNext()
        return currNode 
    
    def getLen(self):
        try:
            length = len(self.getList())
            return length
        except:
            return 0
    
    def getList(self):
        currNode = self.first
        listForm = [currNode.getData()]
        while(currNode.getNext().getData() != None):
            currNode = currNode.getNext()
            listForm.append(currNode.getData())
        return listForm[1:]
    
    def __add__(self, other):
        currNode = other.first
        while(currNode.getNext().getData() != None):
            currNode = currNode.getNext()
            self.append(currNode.getData())
        return self        
               
class Time():
    def __init__(self, string):
        self.original = string
        self.hour = int(string[0:2])%12
        self.minute = int(string[3:5])
        self.name = string[5:7] #am or pm
    
    def __str__(self):
        return self.original

class TimePeriod():
    def __init__(self, string):
        self.original = string
        self.start = Time(string[0:7])
        self.end = Time(string[10:17])
    
    def __str__(self):
        return self.original

class Class():
    def __init__(self, classType, section):
        self.number = classType[0]
        self.name = classType[1]
        self.days = section[0]
        self.time = TimePeriod(section[1])
        self.room = section[2]
        self.prof = section[3]
    
    def __str__(self):
        output = str(self.number)+" "+str(self.name)+"\n\t"
        output+= str(self.days)+'\t'+str(self.time)+'\t'+str(self.room)+'\t'+str(self.prof)
        return output
    
    def getTime(self):
        return self.time.start.hour
    
    def ampm(self):
        return self.time.start.name
    
    def compare(self, other):
        if(self.getTime()%12 > other.getTime()%12):
            return 1
        if(self.getTime()%12 < other.getTime()%12):
            return -1
        return 0
 
def sortDays(days):
    am = LinkedList()
    pm = LinkedList()
    added = False
    
    for day in days:
        if(day.ampm() == "am"):
            if(am.getLen()<=0):
                am.add(day)
            else:
                for i in range(1, am.getLen()+1):
                    if(am.getNode(i).getData().compare(day)>=0):
                        am.insert(day, am.getNode(i-1))
                        added = True
                        break
                if not added:
                    am.append(day)
                added = False
        else:
            if(pm.getLen()<=0):
                pm.add(day)
            else:
                for i in range(1, pm.getLen()+1):
                    if(pm.getNode(i).getData().compare(day)>=0):
                        pm.insert(day, pm.getNode(i-1))
                        added = True
                        break
                if not added:
                    pm.append(day)
                added = False
    #return am.getList()+pm.getList()
    return (am+pm).getList()

def printClasses(classes):
    Monday = [["Monday:"]]
    Tuesday = [["Tuesday:"]]
    Wednesday = [["Wednesday:"]]
    Thursday = [["Thursday:"]]
    Friday = [["Friday:"]]
    
    for each in classes:
        for section in classes[each]:
            if 'M' in section[0]:
                Monday.append(Class(each, section))
            if 'T' in section[0]:
                Tuesday.append(Class(each, section))
            if 'W' in section[0]:
                Wednesday.append(Class(each, section))
            if 'R' in section[0]:
                Thursday.append(Class(each, section))
            if 'F' in section[0]:
                Friday.append(Class(each, section))                 
    days = [Monday, Tuesday, Wednesday, Thursday, Friday]
    ScheduleOptions = []
    for day in days:
        #print(day[0])
        ScheduleOptions.append(sortDays(day[1:]))
        #for each in sortDays(day[1:]):
            #print(each)
        #print('')
    return ScheduleOptions

#Asks user for classes to search for
def getPossibilities():
    posibilities = []
    entered = ' '
    #print("Return when done.")
    entered = input("Enter a class: ")
    while entered != '':
        posibilities.append(entered)
        entered = input("Enter a class: ")
    print("")
    return posibilities
        
def main():
    #masterSchedule = input("Enter master schedule file name or return for last entered:")
    #clear the data of blank lines
    schedule = open("MasterClassSchedule.txt", 'r')
    formattedSchedule = open("formatted.txt", 'w')
    for each in schedule.readlines():
        if each != '\n' and each != ' \n':
            formattedSchedule.write(each)
    schedule.close()
    formattedSchedule.close()
        
    #save data to a list
    formattedSchedule = open("formatted.txt", 'r')
    classList = formattedSchedule.readlines()
    formattedSchedule.close()

    possibilities = getPossibilities()
        
    #Remove extra formatting
    for each in range(0, len(classList)):
        classList[each] = classList[each].strip("\n")
        classList[each] = classList[each].strip("\t")
            
    try:
        classes = {}
        index = -1
        while(True):
            index +=1
            if classList[index] == "View Textbooks": #find anchor in list
                if classList[index-1] in possibilities or classList[index-3] in possibilities: #found name of class
                    name = classList[index-1]
                    number = classList[index-3]
                    try:
                        while('-' not in classList[index]):
                            index+=1
                        while('-' in classList[index]):
                            index+=1
                        classes[(number, name)].append(classList[index:index+4])
                    except KeyError:
                        classes[(number, name)] = [classList[index:index+4]]
                
    except Exception as ex: #done going through list
        Options = printClasses(classes)
        return Options
 
#main()