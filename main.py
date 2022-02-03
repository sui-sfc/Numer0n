import numbers
import random

numbers = [0,1,2,3,4,5,6,7,8,9]
answer =random.sample(numbers,4)
answer_times = 1

while True:
    eat = 0
    bite = 0
    predict = int(input("予測値を入力してください\n>>"))
    for i in range(4):
        if int(str(predict)[i])==answer[i]:
            eat+=1
        if int(str(predict)[i]) in answer:
            bite+=1
            if eat >=0:
                bite=bite - eat
    
    if eat == 4:
        break
    print("eat:",eat)
    print("bite:",bite)
    answer_times += 1

print("的中です 思考回数:",answer_times)
