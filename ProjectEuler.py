import time
from math import *

def problem1():
    total = 0
    for each in range (3, 1000):
        if each%3 == 0 or each%5 == 0:
            total += each
    return total

def problem2():
    first = 1
    second = 2
    temp = 0
    total = 0
    while second < 4000000:
        if second%2 == 0:
            total += second
        temp = first + second
        first = second
        second = temp
    return total
    
def largestPrimeFactor(x):
    lpf = 2;
    while (x > lpf):
        if (x%lpf==0):
            x = x/lpf
            lpf = 2
        else:
            lpf+=1;
    return lpf

def isPalandrome(num):
    i = 0
    while i < len(str(num))/2:
        if(str(num)[i] != str(num)[-i-1]):
            return False
        i+=1
    return True

def largestPalindrome():
    for first in range (999, 100, -1):
        for second in range(999, 100, -1):
            if(isPalandrome(first*(second))):
                return first*second, first, second
    return 0

def divisibleByAll20():
    result = 2520
    factors = {11:11, 13:13, 16:2, 17:17, 19:19}
    while(True):
        done = True
        for each in factors:
            if result%each != 0:
                done = False
                result*=factors[each]
                break
        if done:
            return result
        
def sumSquareDifference():
    total = 0
    totalSquared = (101*50) ** 2
    for each in range(1, 101):
        total += each ** 2
    return totalSquared - total, totalSquared, total
    
def nPrime(n):
    primes = [1]
    prime = 1
    while(len(primes) < n):
        prime+=2  
        for each in range(3,prime, 2):
            if(prime%each == 0):
                break
            if each+1 == prime:
                primes.append(prime)
    return primes[-1]
 
def greatestProduct(n):
    number = str(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)
    greatest = 0
    curr = 1
    for each in range(0, len(number)-n):
        for num in range(each, each+n):
            curr*= int(number[num])
            if num == 0:
                break
        if curr > greatest:
            greatest = curr
        curr = 1
    return greatest

def pTripplet():
    for a in range(1, 1000):
        for b in range(a, 1000):
            if sqrt(a**2 + b**2) == int(sqrt(a**2 + b**2)) and a + b + sqrt(a**2 + b**2) == 1000:
                return a*b*sqrt(a**2 + b**2)

def findPrimes(limit):
    nums = [True] * limit
    nums[1], nums[0] = [False]*2
    for i,val in enumerate(nums):
        if nums[i]:
            nums[i*2::i] = [False]*len(nums[i*2::i])
    return nums

def primeSum():
    primes = findPrimes(2000000)
    total = 0
    for prime, val in enumerate(primes):
        if val:
            total+=prime
    return total

def gridProduct():
    grid = [[8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8], \
    [49, 49, 99, 40, 17, 81, 18, 57, 60, 87,17, 40, 98, 43, 69, 48, 4, 56, 62, 0], \
    [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65], \
    [52, 70, 95, 23, 4 ,60 ,11 ,42 ,69 ,24 ,68 ,56 ,1 ,32 ,56 ,71, 37 ,2 ,36 ,91], \
    [22 ,31 ,16 ,71 ,51 ,67 ,63 ,89 ,41 ,92 ,36 ,54 ,22 ,40 ,40 ,28 ,66 ,33 ,13 ,80], \
    [24 ,47 ,32 ,60 ,99 ,3 ,45 ,2 ,44 ,75 ,33 ,53 ,78 ,36 ,84 ,20 ,35 ,17 ,12, 50], \
    [32 ,98 ,81 ,28 ,64 ,23 ,67 ,10 ,26 ,38 ,40 ,67 ,59 ,54 ,70 ,66 ,18 ,38, 64, 70], \
    [67, 26 ,20 ,68 ,2 ,62 ,12 ,20 ,95 ,63 ,94 ,39 ,63 ,8 ,40 ,91, 66 ,49 ,94 ,21], \
    [24 ,55 ,58 ,5 ,66 ,73 ,99 ,26 ,97 ,17 ,78 ,78 ,96 ,83 ,14, 88, 34, 89, 63 ,72], \
    [21, 36 ,23 ,9 ,75 ,0 ,76 ,44 ,20 ,45 ,35 ,14 ,0 ,61, 33 ,97, 34 ,31, 33, 95], \
    [78 ,17 ,53 ,28 ,22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92], \
    [16 ,39, 5, 42, 96, 35 ,31 ,47 ,55 ,58 ,88 ,24 ,0 ,17 ,54, 24, 36 ,29, 85 ,57], \
    [86 ,56, 0, 48, 35, 71, 89, 7 ,5, 44, 44, 37, 44, 60, 21 ,58, 51, 54, 17, 58], \
    [19 ,80, 81 ,68, 5, 94 ,47, 69, 28, 73, 92, 13, 86, 52 ,17 ,77, 4, 89, 55, 40], \
    [4 ,52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66], \
    [88 ,36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63 ,93, 53, 69], \
    [4 ,42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32 ,40 ,62, 76, 36], \
    [20 ,69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69 ,82, 67, 59, 85, 74 ,4 ,36, 16], \
    [20 ,73, 35 ,29, 78, 31, 90 ,1 ,74 ,31 ,49 ,71 ,48 ,86 ,81 ,16 ,23 ,57 ,5, 54], \
    [1 ,70, 54, 71, 83, 51, 54 ,69 ,16 ,92 ,33 ,48 ,61 ,43 ,52 ,1, 89, 19, 67, 48]]
    
    greatest = 0
    greatestPos = [1, 2]
    currH = 1
    currV = 1
    currD = 1
    currD2 = 1
    for row in range (20):
        for col in range (20):
            for mod in range (4):
                try:
                    currH*= grid[col][row+mod]
                except IndexError:
                    currH = 0
                try:
                    currV*= grid[col+mod][row]
                except IndexError:
                    currV = 0
                try:
                    currD*= grid[col+mod][row+mod]
                except IndexError:
                    currD = 0
                try:
                    currD2*= grid[col-mod][row+mod]
                except IndexError:
                    currD2 = 0                
                    
            if currH > greatest:
                greatest = currH
                greatestPos = [col, row]
            if currV > greatest:
                greatest = currV
                greatestPos = [col,row]
            if currD > greatest:
                greatest = currD
                greatestPos = [col, row]
            if currD > greatest:
                greatest = currD2
            currH = 1
            currV = 1
            currD = 1
            currD2 = 1
    return greatest

def getNumDivisors(num):
    divisors = 2
    
    while num%2 == 0:
        num/=2
        divisors+=1
   
    p = 3
    while num != 1:
        count = 0
        while num%p == 0:
            num/=p
            count+=1
        divisors*=(count+1)
        p+=2
    return divisors
        
        
def divisibleTriangle():
    n = 1
    lnum, rnum = getNumDivisors(n), getNumDivisors(n+1)
    while lnum * rnum < 500:
        n += 1
        lnum, rnum = rnum, getNumDivisors(n+1)
    return n

def first10Sum():
    data = [37107287533902102798797998220837590246510135740250,
    46376937677490009712648124896970078050417018260538,
    74324986199524741059474233309513058123726617309629,
    91942213363574161572522430563301811072406154908250,
    23067588207539346171171980310421047513778063246676,
    89261670696623633820136378418383684178734361726757,
    28112879812849979408065481931592621691275889832738,
    44274228917432520321923589422876796487670272189318,
    47451445736001306439091167216856844588711603153276,
    70386486105843025439939619828917593665686757934951,
    62176457141856560629502157223196586755079324193331,
    64906352462741904929101432445813822663347944758178,
    92575867718337217661963751590579239728245598838407,
    58203565325359399008402633568948830189458628227828,
    80181199384826282014278194139940567587151170094390,
    35398664372827112653829987240784473053190104293586,
    86515506006295864861532075273371959191420517255829,
    71693888707715466499115593487603532921714970056938,
    54370070576826684624621495650076471787294438377604,
    53282654108756828443191190634694037855217779295145,
    36123272525000296071075082563815656710885258350721,
    45876576172410976447339110607218265236877223636045,
    17423706905851860660448207621209813287860733969412,
    81142660418086830619328460811191061556940512689692,
    51934325451728388641918047049293215058642563049483,
    62467221648435076201727918039944693004732956340691,
    15732444386908125794514089057706229429197107928209,
    55037687525678773091862540744969844508330393682126,
    18336384825330154686196124348767681297534375946515,
    80386287592878490201521685554828717201219257766954,
    78182833757993103614740356856449095527097864797581,
    16726320100436897842553539920931837441497806860984,
    48403098129077791799088218795327364475675590848030,
    87086987551392711854517078544161852424320693150332,
    59959406895756536782107074926966537676326235447210,
    69793950679652694742597709739166693763042633987085,
    41052684708299085211399427365734116182760315001271,
    65378607361501080857009149939512557028198746004375,
    35829035317434717326932123578154982629742552737307,
    94953759765105305946966067683156574377167401875275,
    88902802571733229619176668713819931811048770190271,
    25267680276078003013678680992525463401061632866526,
    36270218540497705585629946580636237993140746255962,
    24074486908231174977792365466257246923322810917141,
    91430288197103288597806669760892938638285025333403,
    34413065578016127815921815005561868836468420090470,
    23053081172816430487623791969842487255036638784583,
    11487696932154902810424020138335124462181441773470,
    63783299490636259666498587618221225225512486764533,
    67720186971698544312419572409913959008952310058822,
    95548255300263520781532296796249481641953868218774,
    76085327132285723110424803456124867697064507995236,
    37774242535411291684276865538926205024910326572967,
    23701913275725675285653248258265463092207058596522,
    29798860272258331913126375147341994889534765745501,
    18495701454879288984856827726077713721403798879715,
    38298203783031473527721580348144513491373226651381,
    34829543829199918180278916522431027392251122869539,
    40957953066405232632538044100059654939159879593635,
    29746152185502371307642255121183693803580388584903,
    41698116222072977186158236678424689157993532961922,
    62467957194401269043877107275048102390895523597457,
    23189706772547915061505504953922979530901129967519,
    86188088225875314529584099251203829009407770775672,
    11306739708304724483816533873502340845647058077308,
    82959174767140363198008187129011875491310547126581,
    97623331044818386269515456334926366572897563400500,
    42846280183517070527831839425882145521227251250327,
    55121603546981200581762165212827652751691296897789,
    32238195734329339946437501907836945765883352399886,
    75506164965184775180738168837861091527357929701337,
    62177842752192623401942399639168044983993173312731,
    32924185707147349566916674687634660915035914677504,
    99518671430235219628894890102423325116913619626622,
    73267460800591547471830798392868535206946944540724,
    76841822524674417161514036427982273348055556214818,
    97142617910342598647204516893989422179826088076852,
    87783646182799346313767754307809363333018982642090,
    10848802521674670883215120185883543223812876952786,
    71329612474782464538636993009049310363619763878039,
    62184073572399794223406235393808339651327408011116,
    66627891981488087797941876876144230030984490851411,
    60661826293682836764744779239180335110989069790714,
    85786944089552990653640447425576083659976645795096,
    66024396409905389607120198219976047599490197230297,
    64913982680032973156037120041377903785566085089252,
    16730939319872750275468906903707539413042652315011,
    94809377245048795150954100921645863754710598436791,
    78639167021187492431995700641917969777599028300699,
    15368713711936614952811305876380278410754449733078,
    40789923115535562561142322423255033685442488917353,
    44889911501440648020369068063960672322193204149535,
    41503128880339536053299340368006977710650566631954,
    81234880673210146739058568557934581403627822703280,
    82616570773948327592232845941706525094512325230608,
    22918802058777319719839450180888072429661980811197,
    77158542502016545090413245809786882778948721859617,
    72107838435069186155435662884062257473692284509516,
    20849603980134001723930671666823555245252804609722,
    53503534226472524250874054075591789781264330331690]
    
    total = 0
    for each in data:
        total += each
    return str(total)[0: 10]

def collatzSequence():
    longest = (1, 0)
    starters = { 2:[1] }
    
    for each in range(3, 1000000):
        starters[each] = [each]
        while starters[each][-1] != 1:
            if starters[each][-1]%2 == 0:
                starters[each].append(starters[each][-1]/2)
            else:
                starters[each].append(3*starters[each][-1] + 1)            
            if starters[each][-1] in starters:
                starters[each].extend(starters[starters[each][-1]][1:])
                
                if len(starters[each]) > longest[1]:
                    longest = (starters[each][0], len(starters[each]))
                    print(longest[0])
                break
    return longest[0]

def gridPaths(size):
    grid = [[0] * size]*size
    grid[0] = [1]*size
    for row in range (1,size):
        for col in range(0,size):
            if col == 0:
                grid[row][col] = 1
            else:
                grid[row][col] = grid[row-1][col] + grid[row][col-1]

    return grid[size-1][size-1]

def sumOfDigits(num):
    output = 0 
    while(num > 1):
        output+= num%10
        num = num // 10
    return output

def numLetters(num):
    letters = 0
    number = [num%10,(num//10) %10,(num//100) %10,num//1000]
    if number[3] == 1:
        return 11
    
    if number [2] != 0:
        letters += len('hundred') + numLetters(number[2])
        if(number[1] != 0 or number[0] != 0):
            letters += len('and')
    
    if number[1] ==1:
        if number[0] == 0:
            letters += len('ten')
        elif number[0] == 1 or number[0] == 2:
            letters += 6
        elif number[0] == 3 or number[0] == 4 or number[0] == 8 or number[0] == 9:
            letters += 8
        elif number[0] == 5 or number[0] == 6:
            letters += 7
        else:
            letters += 9
    else:
        if number[1] == 2 or number[1] == 3 or number[1] == 8 or number[1] == 9:
            letters+= 6
        elif  number[1] == 4 or number[1] == 5 or number[1] == 6:
            letters+= 5
        elif number[1] == 7:
            letters+= 7
        
        if number[0] == 1 or number[0] == 2 or number[0] == 6:
            letters +=3
        elif number[0] == 4 or number[0] == 5 or number[0] == 9:
            letters += 4
        elif number[0] == 3 or number[0] == 7 or number[0] == 8:
            letters += 5

    return letters
    
def lettersToThousand():
    total = 0
    for each in range (1, 1001):
        total += numLetters(each)
    return total  

def greatestSumTriangle(triangle):
    for row in range (len(triangle) - 2, -1, -1):
        for col in range (len(triangle[row])):
            if triangle[row+1][col] > triangle[row+1][col+1]:
                triangle[row][col] += triangle[row+1][col]
            else: 
                triangle[row][col] += triangle[row+1][col+1]
                
    return triangle[0][0]
    
    
def getTriangle18():
    tri = [[75] , \
           [95, 64], \
           [17, 47, 82], \
           [18, 35, 87, 10], \
           [20, 4, 82, 47, 65], \
           [19, 1, 23, 75, 3, 34], \
           [88, 2, 77, 73, 7, 63, 67], \
           [99, 65, 4, 28, 6, 16, 70, 92], \
           [41, 41, 26, 56, 83, 40, 80, 70, 33], \
           [41, 48, 72, 33, 47, 32, 37, 16, 94, 29], \
           [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14], \
           [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57], \
           [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48], \
           [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31], \
           [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]
    
    return tri
def leapYear(year, month):
    if month != 'Feb':
        return 0
    if year % 100 == 0:
        if year % 400 == 0:
            return 1
        return 0
    if year%4 == 0:
        return 1
    return 0

def howManySundays(): #?
    count = 0;
    months = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr':30, 'May':31, 'Jun':30, 'Jul':31, 'Aug': 31, 'Sep' : 30, 'Oct' : 31, 'Nov' : 30, 'Dec':31}
    numDay = 1
    for year in range(1900, 2001):
        for month in months:
            for day in range (1, months[month]+leapYear(year, month)):
                if numDay %12 == 0 and day == 1:
                    count +=1
                numDay+=1
    return count

def factorialDigits(num):
    factorial = 1
    for each in range(1, num+1):
        factorial*=each
    total = 0 
    for each in str(factorial):
        total += int(each)
    return total

def findPrimesUnder(num):
    primes = []
    for i, val in enumerate(findPrimes(num)):
        if val:
            primes.append(i)
        #if len(primes) >= num:
            #break
    return primes

def d(n): #sum of proper factors of n
    s = 0
    for each in range(1, n):
        if n%each == 0:
            s+= each
    return s

def sumAmicible(limit):
    total = 0 
    sums = [d(i) for i in range(0, limit+1)]
    for i in range(1, limit+1):
        if sums[i] < i and i == sums[sums[i]]:
            total+= i + sums[i]
        
    return total

def getNames():
    text = open('p022_names.txt', 'r+')
    names = text.readlines()
    text.close()
    nameList = []
    currName = ''
    for each in names[0]:
        if each == '''"''' and len(currName) != 0:
            nameList.append(currName)
            currName = ''
        if each != '''"''' and each != ',':
            currName+=each
    return nameList
def fix(stuff):
    output = []
    for each in stuff:
        try:
            if len(each) == 0:
               continue
            if len(each) > 1:
                for item in each:
                    output.append(item)
            else:
                output.append(each)
        except TypeError:
            continue
    
    return output
    
def sortNames(names, index):
    if len(names) == 0:
        return
    if len(names) == 1:
        return names
    letters = {'A': [], 'B': [],'C': [],'D': [],'E': [],'F': [],'G': [],'H': [],'I': [],'J': [],'K': [],'L': [],'M': [],'N': [],'O': [],'P': [],'Q': [],'R': [],'S': [],'T': [],'U': [],'V': [],'W': [],'X': [],'Y': [],'Z': [], ' ': []}
    for each in names:
        if index >= len(each):
            letters[' '].append(each)
        else:
            letters[each[index]].append(each)
    return fix([letters[' '], sortNames(letters['A'],index+1), sortNames(letters['B'],index+1), sortNames(letters['C'],index+1), sortNames(letters['D'],index+1), sortNames(letters['E'],index+1), sortNames(letters['F'],index+1), sortNames(letters['G'],index+1), sortNames(letters['H'],index+1), sortNames(letters['I'],index+1), sortNames(letters['J'],index+1), sortNames(letters['K'],index+1), sortNames(letters['L'],index+1), sortNames(letters['M'],index+1), sortNames(letters['N'],index+1), sortNames(letters['O'],index+1), sortNames(letters['P'],index+1), sortNames(letters['Q'],index+1), sortNames(letters['R'],index+1), sortNames(letters['S'],index+1), sortNames(letters['T'],index+1), sortNames(letters['U'],index+1), sortNames(letters['V'],index+1), sortNames(letters['W'],index+1), sortNames(letters['X'],index+1), sortNames(letters['Y'],index+1), sortNames(letters['Z'],index+1)])

def letterVal(letter):
    letters = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
    return letters[letter]

def scores(names):
    total = 0 
    letterSum = 0 
    for each in range (0, len(names)):
        for letter in names[each][0]:
            letterSum+= letterVal(letter)
        total += letterSum*(each+1)
        letterSum = 0
    return total

def getAbundantNumbers(limit):
    nums = []
    sumOfDivisors = 0
    for number in range(2, limit):
        for divisor in range(number//2, 1, -1):
            if number%divisor == 0:
                sumOfDivisors+= divisor
                if sumOfDivisors > number:
                    nums.append(number)
                    break
        sumOfDivisors = 0
    return nums

def factorial(num):
    output = 1
    for each in range(1, num+1):
        output*= each
    return output

def lexicographicPermutation():
    perm = []
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    goal = 1000000
    for each in range(9, -1, -1):
        perm.append(numbers[goal // factorial(each)])
        numbers.pop(goal//factorial(each))
        goal -= (goal//factorial(each))*factorial(each)
        print(numbers)
    
    return perm
    
def getPrimeMultiples(limit):
    nums = [True]*limit
    primes = []
    nums[0] = [False]
    nums[1] = [False]
    for i in range(2, limit):
        if nums[i]:
                primes.append(i)
                nums[i+i::i] = [False]*len(nums[i+i::i])
    
    primes.remove(2)
    primes.remove(5)

    for each in range(0, limit):
        nums[each] = each
        
    primeMultiples = []
    for prime in primes:
        primeMultiples.append(nums[prime::prime])
    
    return primeMultiples
        
def longFibonacci(nums):
    sequence = [0,1]
    
    while len(str(sequence[-1])) != nums:
        sequence.append(sequence[-1] + sequence[-2])
    
    return len(sequence)

def diagonalSums(size):
    total = 1
    for each in range (3, size+1, 2):
        total += 4*(each**2)-6*each+6
    return total

def distinctPowers(a, b):
    powers = {}
    
    for base in range(a, 1, -1):
        for exponent in range(b, 1, -1):
            try:
                powers[base**exponent] = 1
            except:
                break
    return len(powers)

def fifthPowers():
    total = 0
    fifths = 0
    number = 100
    while (time.time() - start_time) < 3:
        for each in str(number):
            fifths += int(each)**5
        if fifths == number:
            total += number
        fifths = 0
        number+=1
    return total


def main():
    print(fifthPowers())


import time
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
