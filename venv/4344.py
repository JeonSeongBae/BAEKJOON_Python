# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

size = int(input()) # C 5
array = [[0] * size for i in range(size)]

for i in range(0, size):
    array[i] = list(map(int, input().split())) # 5 50 50 70 80 100
average = count = 0
for i in range(0, size):
    for j in range(1, len(array[i])):
        average = sum(array[i][1:len(array[i])])/array[i][0]
        if(average < array[i][j]):
            count += 1
    print('%.3f%%' %(count/array[i][0]*100))
    count = 0
