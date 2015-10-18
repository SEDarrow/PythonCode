import time
    
#Reset budget for the month
def monthlyAddition():
    record = open("LastOpened.txt", 'r')
    lastMonth = int(record.readline())
    lastYear = int(record.readline())
    record.close()
    thisMonth = int(time.strftime("%m"))
    thisYear = int(time.strftime("%Y"))
    
    if(thisMonth != lastMonth or thisYear != lastYear):
        budget = open("budget.txt", 'r+')
        
        #Record surplus budget
        funds = budget.readlines[-1] 
        
        #Reset budget
        budget.write("\n100")
        budget.close()
        
        #add surplus budget and missed monthly stipends to savings
        savings = open("overallSavings.txt", 'r+')
        savedFunds = savings.readlines()[-1]
        savedFunds+= funds + 100*(thisMonth-lastMonth + 12*(thisYear-lastYear) -1)
        savings.write(savedFunds)
        savings.close()
        
    return
 
#Reduce budget by amount spent  
def budget(spent):
    budget = open("budget.txt", 'r+')
    funds = float(budget.readlines()[-1])
    funds-= spent
    budget.write('\n'+str(funds))
    budget.close()
    
    print("Remaining budget is: $"+str(round(funds,2)))
    
    global tasks
    tasks.append(('budget', spent))
    return

#Update savings fund
def savings(money):
    budget = open("overallSavings.txt", 'r+')
    funds = float(budget.readlines()[-1])
    funds+= money
    budget.write('\n'+str(funds))
    budget.close()
        
    print("Savings are: $"+str(round(funds, 2)))
    
    global tasks
    tasks.append(('savings', money))    
    return    

#print the budget and savings
def report():
    savings = open("overallSavings.txt", 'r')
    saved = float(savings.readlines()[-1])
    savings.close()

    budget = open("budget.txt", 'r')
    funds = float(budget.readlines()[-1])
    budget.close()
    
    if saved > 500:
        modifier = ' :D'
    elif saved < 0:
        modifier = ' :/'
    else:
        modifier = ''
    
    print("Savings: $"+str(round(saved, 2))+modifier)
    
    if funds >= 100:
            modifier = ' :D'
    elif funds < 0:
            modifier = ' :/'
    else:
            modifier = ''    
    
    print("Budget: $"+str(round(funds, 2))+modifier)
    return

#Calsulate the amount of money that can be spent each week
def weekly():
    day = int(time.strftime("%d"))
    month = int(time.strftime("%m"))
    year =  int(time.strftime("%Y"))
    
    #Determine how many days in the current month
    if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
        lastDay = 31
    elif month == 2:
        if year%4 == 0:
            lastDay = 29
        else:
            lastDay = 28
    else:
        lastDay == 30
    
    budget = open("budget.txt", "r")
    funds = float(budget.readlines()[-1])
    budget.close()
    
    daysToGo = lastDay - day
    perDay = funds/daysToGo
    
    print("$"+str(round(funds, 2))+" remaining")
    for each in range(day+7, lastDay+1, 7):
        print("You can spend $"+str(round(perDay*7, 2))+" from "+str(month)+"/"+str(each-7)+" to "+str(month)+"/"+str(each))
    if each != lastDay:
        print("You can spend $"+str(round(perDay*(lastDay-(each)), 2))+" from "+str(month)+"/"+str(each-7)+" to "+str(month)+"/"+str(lastDay))
    return
            
def main():
    print("Hello!")
    monthlyAddition()
    while(True):
        
        print("\n1: Record budget spending", \
              "\n2: Record savings spending", \
              "\n3: Record savings",\
              "\n4: View funds", \
              "\n5: View weekly budget", \
              "\n6: Undo", \
              "\nEnter to exit")
        choice = input("Enter the number of what you wish to do: ")
        
        #Validate input
        try:
            choice = int(choice)
        except ValueError:
            if(choice == ""):
                break
            else:
                print("ERROR! NUMBER NOT ENTERED!")
                continue
        
        if choice == 1: #Record budget spending
            spent = input("Enter amount spent: $")
            try:
                spent = float(spent)
                budget(spent)
            except ValueError:
                print("ERROR! INVALID INPUT")
                continue
        elif choice == 2: #Record savings spending
            spent = input("Enter amount spent: $")
            try:
                spent = float(spent)
                savings(-1*spent)
            except ValueError:
                print("ERROR! INVALID INPUT")
                continue            
        elif choice == 3: #record savings
            spent = input("Enter amount saved: $")
            try:
                spent = float(spent)
                savings(spent)
            except ValueError:
                print("ERROR! INVALID INPUT")
                continue  
        elif choice == 4: #View funds
            report()
        elif choice == 5: #View weekly budget
            weekly()
        elif choice == 6: #Undo change in funds
            global tasks
            if(len(tasks) == 0): 
                print("Nothing to undo.")
            else: 
                toUndo = tasks.pop()
                validation = input("Undo $"+str(abs(toUndo[1]))+" from "+toUndo[0]+"? Y/N: ")
                if(validation == "Y"):
                    if toUndo[0] == 'budget':
                        budget(-1*toUndo[1])
                    else:
                        savings(-1*toUndo[1])
                    tasks.pop()
                elif(validation == "N"):
                    print("Aborted.")
                else:
                    print("ERROR! INVALID INPUT!")          
        else: #Input validation
            print("ERROR! NUMBER OUT OF RANGE!")
     
    print("Goodbye!")
    time.sleep(1)
    
    #Record date of running program for future use
    record =  open('LastOpened.txt', 'w')
    record.write(time.strftime("%m")+"\n")
    record.write(time.strftime("%Y"))
    record.close()
 
tasks = []
main()