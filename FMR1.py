from functools import reduce

def checkEven(No):
    return (No % 2 == 0)

def Increase(No):
    return No + 1


def Sum(A,B):
    return A+B


Data = [7,10,15,12,4,6,9,8,12,16]
print("input Data : ",Data)

FData = list(filter(checkEven, Data))
print("Filter output :", FData)

MData = list(map(Increase, FData))
print("Maped Data : ", MData)

RData = reduce(Sum, MData)
print("Reduced data is last output :", RData)