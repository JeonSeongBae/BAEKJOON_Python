# 오늘은 2007년 1월 1일 월요일이다. 그렇다면 2007년 x월 y일은 무슨 요일일까? 이를 알아내는 프로그램을 작성하시오.

month, date = map(int,input().split())

if month >= 2:
    date += 31
if month >= 3:
    date += 28
if month >= 4:
    date += 31
if month >= 5:
    date += 30
if month >= 6:
    date += 31
if month >= 7:
    date += 30
if month >= 8:
    date += 31
if month >= 9:
    date += 31
if month >= 10:
    date += 30
if month >= 11:
    date += 31
if month >= 12:
    date += 30

date = date % 7
if date is 0:
    print('SUN')
elif date is 1:
    print('MON')
elif date is 2:
    print('TUE')
elif date is 3:
    print('WED')
elif date is 4:
    print('THU')
elif date is 5:
    print('FRI')
elif date is 6:
    print('SAT')