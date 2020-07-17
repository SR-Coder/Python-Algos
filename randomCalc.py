import random

def randProb(ll, ul, it):
    probList = []
    for j in range(ll,ul+1,1):
        probList.append(0)
        # print(j)


    for i in range(it):
        x = random.randint(ll,ul)
        probList[x-1] = probList[x-1] +1
        # print(i)

    for i in range(len(probList)):
        probList[i] = (probList[i]/it) * 100

    return probList

print(randProb(1,2,10000000))