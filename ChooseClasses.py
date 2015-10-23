import ScheduleOptions as SO

def chooseClass(allClasses, classesChosen):
    length = 0
    try:
        for each in allClasses:
            length += len(each)
        if length <= 5:
            int("hi")
    except ValueError:
        print("Here is your schedule:")
        for each in classesChosen:
            print(each)
        return classesChosen
    printClasses(allClasses)
    try:
        chosen = input("Choose a class to take: ")
        chosenDay = int(chosen.split(':')[0])
        chosenClass = int(chosen.split(':')[1])
    except ValueError:
        print("Enter the number of the class")
        return chooseClass(allClasses, classesChosen)
    classChosen = allClasses[chosenDay-1][chosenClass-1]
    
    d=0
    classesLeft = [[], [], [], [], []]
    for day in allClasses:
            for section in day:
                if section.name == classChosen.name or (section.time.start.hour == classChosen.time.start.hour and section.days == classChosen.days):
                    continue
                classesLeft[d].append(section)
            d+=1    
    classesChosen.append(classChosen)
    chooseClass(classesLeft, classesChosen)
    #return classesChosen
        
def printClasses(classes):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    i = 1
    d =0
    for each in classes:
        print(days[d])
        for item in each:
            print(str(d+1)+':'+str(i), item)
            i+=1
        d+=1
        i = 1 
            
def main():
    Options = SO.main()
    chooseClass(Options, [])
    
main()