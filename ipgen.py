from random import randrange

def generateIP():
    blockOne = randrange(0, 255, 1)
    blockTwo = randrange(0, 255, 1)
    blockThree = randrange(0, 255, 1)
    blockFour = randrange(0, 255, 1)
    print 'Random IP: ' + str(blockOne) + '.' + str(blockTwo) + '.' + str(blockThree) + '.' + str(blockFour)
    if blockOne == 10:
        return self.__generateRandomIP__()
    elif blockOne == 172:
        return self.__generateRandomIP__()
    elif blockOne == 192:
        return self.__generateRandomIP__()
    else:
        return str(blockOne) + '.' + str(blockTwo) + '.' + str(blockThree) + '.' + str(blockFour)


generateIP()
