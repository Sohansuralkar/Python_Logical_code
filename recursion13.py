#input : 4 
#output : 24 (4*3*2*1)
fact = 1   #global declare kela variable
def factorial(no):
    global fact          # global keyword which is used to access global variable
    if(no>=1):
        fact = fact * no
        no = no - 1
        factorial(no)
       
    return fact
    

def main():
    ret = factorial(4)
    print(ret)

if __name__== "__main__":

    main()