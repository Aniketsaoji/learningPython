import random
def forLoop():
    nums = [1,2,3,4,5,6]

    for num in nums:
        print (num)

def forLoopWithRange():
    for i in range(3):
        print (i)

def nestedForLoops():
    teams = [["A, B"], ["C", "D"], ["E", "F"]]
    for team in teams:
        print (team)
        for name in team:
            print (name)

def whileLoops():
    coin = True
    counter = 1

    while(coin):
        print(counter)
        result = random.randint(0, 1)
        if result == 0:
            coin = False;
        else:
            coin = True;
        counter+=1

def infiniteLoops():
    while True:
        print ("leave")



def main():
    # forLoop()
    # forLoopWithRange()
    # print()
    # nestedForLoops()
    whileLoops()
    # infiniteLoops()

if __name__ == '__main__':
    main()

