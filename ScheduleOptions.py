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
    
def sortDays(classes):
    pm = []
    am = []
    added = False
    
    for each in classes:
        if each[3].start.name == 'pm':
            pm.append(each)
            continue
            if(len(pm) == 0):
                pm.append(each)
            else:
                for i in range(0, len(pm)):
                    if(each[3].start.hour%12 <pm[i][3].start.hour%12):
                        print("New element added at", i)
                        pm.insert(each, i)
                        added = True
                        break
                if not added:
                    pm.append(each)
                added = False
        else:
                am.append(each)  
    return am+pm

def printClasses(classes):
    Monday = [["Monday:"]]
    Tuesday = [["Tuesday:"]]
    Wednesday = [["Wednesday:"]]
    Thursday = [["Thursday:"]]
    Friday = [["Friday:"]]
    
    for each in classes:
        for section in classes[each]:
            if 'M' in section[0]:
                Monday.append([each[0], each[1], section[0], TimePeriod(section[1]), section[2], section[3]])
            if 'T' in section[0]:
                Tuesday.append([each[0], each[1], section[0], TimePeriod(section[1]), section[2], section[3]])
            if 'W' in section[0]:
                Wednesday.append([each[0], each[1], section[0], TimePeriod(section[1]), section[2], section[3]])
            if 'R' in section[0]:
                Thursday.append([each[0], each[1], section[0], TimePeriod(section[1]), section[2], section[3]])
            if 'F' in section[0]:
                Friday.append([each[0], each[1], section[0], TimePeriod(section[1]), section[2], section[3]])                 
    days = [Monday, Tuesday, Wednesday, Thursday, Friday]
    
    for day in days:
        print(day[0])
        try:
            for item in sortDays(day[1:]):
                print(item[0], item[1], "\n\t", end = '')
                for each in item[2:]:
                    print(str(each)+"\t", end='')
                print('')
        except:
            continue
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
