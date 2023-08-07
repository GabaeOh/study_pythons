# slicing
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# 길이 출력
len(thislist)
# 7

#type을 알고 싶을때 / 변수의 형태 알고 싶을때 
type(thislist)
# <class 'list'>

thislist[:3]
# ['apple', 'banana', 'cherry']

# 역순
thislist[::-1]
# ['mango', 'melon', 'kiwi', 'orange', 'cherry', 'banana', 'apple']

# 역순으로 하고 mango만 추출하기
thislist[::-1][0] 
# 'mango'
thislist[-1:-2:-1]
#['mango']

# 셋번째 칸이 간격 첫번째 칸부터 +2씩 커지는 커지면서 홀수만 뽑기
thislist[1::2]
# ['banana', 'orange', 'melon']

#change value in list
thislist[1]= "watermelon"

# 2개의 값 바꾸기
thislist[1:3] = ["cherry", "watermelon"]

#sort 정렬
thislist.sort() # 알파벳 순서대로 정렬시킴

thislist.sort(reverse=True) #역순으로 정렬시킴

pass