import sys
def main():
    print("Number of command line agruments are :",len(sys.argv))
    print("List of command line arguments are :")


 #   for i in sys.argv:
  #     print(i)

    for i in range(1, len(sys.argv)):
     print(sys.argv[i])
    #i = 0
    #while(i< len(sys.argv)):
   # i = i + 1

  # pass
if __name__ == "__main__":
    main()