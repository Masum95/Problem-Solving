#!/bin/python3


stepTaken = 1 
def printTowers(towers, step):
    print('Step ', step)
    for i in range(len(towers)):
        print('Tower ',i,' -> ', towers[i])
    print('--------------')

def getWhereToMove(frm,to):
    return list(set(range(3)) - set([frm, to]))[0]

def move(towers, indexList, frm, to):
    # print(towers)
    # print(indexList)
    global stepTaken
    if len(indexList) == 1:
        disc = towers[frm].pop()
        towers[to].append(disc)
        printTowers(towers, stepTaken)
        stepTaken += 1
        return

    move(towers, indexList[1:] , frm, getWhereToMove(frm, to))
    move(towers, [indexList[0]], frm, to) 
    move(towers, indexList[1:], getWhereToMove(frm, to), to )


def moveDiscs(discs, whereToMove):
    towers = [list(reversed(range(1, discs+1)) ), 
                [],
                []]
    move(towers,list(range(discs)),  0, whereToMove-1)

moveDiscs(5, 3)


