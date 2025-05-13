checkEven = lambda No : (No % 2 == 0)
Increase = lambda No : No + 1 
Sum = lambda A, B : A + B

def filterX(Task,Values):
    Result = []
    for no in Values:
        Ret =  Task(no)
        if (Ret == True) :
            Result.append(no)
    return Result
def mapX(Task,Values):
    Result = []
    for no in Values:
        Ret = Task(no)
        Result.append(Ret)
    return Result
def reduceX(Task,Values):
    Result = 0 
    for no in Values:
        Result = Task(Result,no)    # dry and run code
    return Result


def main():
    Data = [7,10,15,12,4,6,9,8,12,16]
    print("input Data : ",Data)

    FData = list(filterX(checkEven, Data))
    print("Filter output :", FData)

    MData = list(mapX(Increase, FData))
    print("Maped Data : ", MData)

    RData = reduceX(Sum, MData)
    print("Reduced data is last output :", RData)

if __name__ == "__main__":
    main()