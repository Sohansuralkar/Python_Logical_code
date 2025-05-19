#input : 4 
#output : 24 (4*3*2*1)
sum = 0
def fact(no):
    fact = 1 
    while (no>=1):
        fact = fact * no
        no = no - 1
    return fact
    

def main():
    ret = fact(4)
    print(ret)

if __name__== "__main__":

    main()