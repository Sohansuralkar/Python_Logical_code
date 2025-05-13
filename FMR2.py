from functools import reduce

checkEven = lambda No : (No % 2 == 0)

Increase = lambda No : No + 1 

Sum = lambda A, B : A + B

Data = [7,10,15,12,4,6,9,8,12,16]     # list is like array
print("input Data : ",Data)

FData = list(filter(checkEven, Data))
print("Filter output :", FData)

MData = list(map(Increase, FData))
print("Maped Data : ", MData)

RData = reduce(Sum, MData)
print("Reduced data is last output :", RData)