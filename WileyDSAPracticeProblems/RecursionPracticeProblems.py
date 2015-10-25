from random import *
import sys

#C-4.9
def findMaxMin(sequence, maximum = -1*sys.maxsize - 1, minimum = sys.maxsize):
    if len(sequence) <=0:
        return maximum, minimum
    if sequence[0] < minimum:
        minimum = sequence[0] 
    if sequence[0] > maximum:
        maximum = sequence[0]
    return findMaxMin(sequence[1:], maximum, minimum)

# C-4.11
def unique(sequence, n=1):
    if len(sequence) <=1:
        return True
    if n >= len(sequence):
        return unique(sequence[1:], 1)
    if sequence[0] == sequence[n]:
        return False, sequence[0]
    return unique(sequence, n+1)

# C-4.12
def product(m, n):
    if n == 0:
        return 0
    if(n < 0 and m < 0) or (n > 0 and m > 0):
        if(n > 0):
            return abs(m) + product(m, n-1)
        return abs(m) + product(m, n+1)
    if(n > 0):
        return -abs(m)+ product(m, n-1)
    return -abs(m) + product(m, n+1)

#C-4.15
def subsets(sequence, end =1, subsetList=[]):
    if len(sequence) <= 0:
        return subsetList
    if end > len(sequence):
        return subsets(sequence[1:], 1, subsetList)
    subsetList.append(sequence[:end])
    return subsets(sequence, end+1, subsetList)

def subsets(sequence, end =1):
    if len(sequence) <= 0:
        return
    if end > len(sequence):
        return subsets(sequence[1:])
    return sequence[0:end], subsets(sequence, end+1)

#C-4.16
def reverse(string):
    if len(string) <=0:
        return ''
    return reverse(string[1:])+ string[0]

def randomSequence(length, lower=0, upper=100):
    sequence = [0] * length
    for each in range(0, length):
        sequence[each] = randint(lower, upper)
    return sequence

#C-4.18
def moreVowels(string, count=None):
    if count ==None:
        count = len(string)/2
    if len(string) <= 0:
        return count > 0
    if string[0].lower() in ['a', 'e', 'i', 'o', 'u']:
        return moreVowels(string[1:], count)
    return moreVowels(string[1:], count-1)

sequence = randomSequence(20)
print(sequence)
print(moreVowels("EEdeded"))