import time
start_time = time.time()
import random
numOfValues = 8000
upperLimit = 9680
lowerLimit = -1380
noDuplicates = True


def insertionSort(result):
    r_len = len(result)
    for i in range(1, r_len):
        key = result[i]
        for j in range(1, i+1)[::-1]:
            if j > 0 and key < result[j-1]:
                result[j] = result[j-1]
                result[j-1] = key
    return result


def rNGenerator (lowerLimit,upperLimit,numOfValues,noDuplicates):
    #1.生成一个list from lower to upper
    Sequence = list(range(lowerLimit,upperLimit))
    #2. 获取numOfValues个随机数
    result = random.sample(Sequence,numOfValues)
    #3. 如果result的长度！=不重复集合的长度就是有重复/反之没重复
    if len(result) != len(set(result)):
        noDuplicates==False
        result = []
        for i in result:
         if result.count(i) != 1:
          result.append(random.randint(Sequence))
        else:
            print(insertionSort(result))
            print(len(insertionSort(result)))
    else:
        noDuplicates==True
        print(insertionSort(result))
        print(len(insertionSort(result)))


        #写入文本
        def saveToFile():
         R='\n'.join(str(i) for i in result)
         open('test2_2.txt', 'w').write(R)
        saveToFile()

rNGenerator(lowerLimit, upperLimit, numOfValues, noDuplicates)

end_time = time.time()
print("Running time: %s seconds"%(end_time - start_time))

