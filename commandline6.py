import sys
def addition(no1,no2):
    ans = 0 
    ans = no1 + no2
    return ans
def main():
    if(len(sys.argv != 3)):
       print("Insufficicent number of arguments")
       return

    value1 = int(input(len(sys.argv)))
    value2 = int(input(len(sys.argv)))
    result =  addition (value1,value2)

    print("addition is :", result)
    print("Command line arg are : ",len(sys.argv))
    for i in range(0, len(sys.argv)):
     print(sys.argv[i])
    
    

if __name__ == "__main__":
    main()