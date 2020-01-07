import time
start_time = time.time()
import random
numOfValues = 5000
upperLimit = 3660
lowerLimit = -3550


def rNGenerator (lowerLimit,upperLimit,numOfValues):
    #1.生成一个list from lower to upper
    Sequence = list(range(lowerLimit,upperLimit))
    #2. 获取numOfValues个随机数
    result = random.sample(Sequence,numOfValues)
    print(result)
    print(len(result))

        #写入文本
    def saveToFile():
        R='\n'.join(str(i) for i in result)
        open('test1_1.txt', 'w').write(R)
        saveToFile()



rNGenerator(lowerLimit, upperLimit, numOfValues)

end_time = time.time()
print("Running time: %s seconds"%(end_time - start_time))
