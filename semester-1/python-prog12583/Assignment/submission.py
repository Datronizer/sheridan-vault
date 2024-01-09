# Question 0
def whatIsYourName():
    name = input("What is your name?\n> ")
    return name
    
def updateLastMark(marksList, updatedMark):
    marksList[-1] = updatedMark
    return marksList

name = whatIsYourName()
marks = [99, 88, 77, 66]

updateLastMark(marks, 44)
print(name, 'your mark changed from 66 to', marks[3])


# Question 1
ages = [23, 22, 25, 22, 20, 24, 19]

def bubbleSort(someList):
    swapped = True
    listLength = len(someList)
    
    while swapped:
        swapped = False
        for i in range(1, listLength):
            if someList[i - 1] > someList[i]:
                placeholder = someList[i]
                someList[i] = someList[i - 1]
                someList[i - 1] = placeholder
                
                swapped = True
                
    return someList
    
print(bubbleSort(ages))


# Question 2
import math
ages = [23, 22, 25, 20, 25, 22, 23]

def isPalindrome(someList):
    # We don't need to check all the numbers, just halfway through
    # If list is odd, ignore middle number
    if (len(someList) % 2 != 0):
        middlePoint = math.floor(len(someList) / 2) - 1
    else:
        middlePoint = (len(someList) / 2) - 1
    
    for i in range(middlePoint):
        fwd = someList[i]
        bwd = someList[-(i + 1)]
            
        if fwd == bwd:
            continue
        else:
            return False
    return True

print(isPalindrome(ages))