class Node():
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode
        
    def getData(self):
        return self.data
    def setData(self, data):
        self.data = self
        
    def getNext(self):
        return self.nextNode
    def setNext(self, nextNode):
        self.nextNode = nextNode   

class LinkedList():
    def __init__(self, first=None):
        self.first = first
    
    def add(self, data, sort=False):
        newNode = Node(data, self.first)
        self.first = newNode   
        
    def insert(self, data, pNode):
        newNode = Node(data, pNode.getNext())
        pNode.setNext(newNode)
        
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
        while(currNode.getNext() != None):
            currNode = currNode.getNext()
            listForm.append(currNode.getData())
        return listForm
               
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
        if(self.getTime%12 > other.getTime%12):
            return 1
        if(self.getTime%12 < other.getTime%12):
            return -1
        return 0

def sortDays(days):
    am = LinkedList()
    pm = LinkedList()
    
    for day in days:
        if(day.ampm() == "am"):
            am.add(day, True)
        else:
            pm.add(day, True)
    return am.getList()+pm.getList()
    

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
    
    for day in days:
        print(day[0])
        for each in sortDays(day[1:]):
            print(each)
        print('')

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
    try:
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
            printClasses(classes)
            while(true):
                i = input()            
            #print(classes)
        
        
    except: 
        #print("ERROR")
        main()
    
main()
