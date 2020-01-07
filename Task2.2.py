import time
start_time = time.time()
import random
numOfValues = 8000
upperLimit = 13660
lowerLimit = -3550
noDuplicates = True




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
            print(result)
            print(len(result))
    else:
        noDuplicates==True
        print(result)
        print(len(result))

        def quickSort(result):
            if result == []:
                return []
            else:
                pivot = result[0]
                lesser = quickSort([x for x in result[1:] if x < pivot])
                greater = quickSort([x for x in result[1:] if x >= pivot])
                result = lesser + [pivot] + greater
                return result
        quickSort(result)
        print(quickSort(result))
        print(len(quickSort(result)))

        #写入文本
        def saveToFile():
         R='\n'.join(str(i) for i in result)
         open('test2_3.txt', 'w').write(R)
        saveToFile()

rNGenerator(lowerLimit, upperLimit, numOfValues, noDuplicates)
end_time = time.time()
print("Running time: %s seconds"%(end_time - start_time))

