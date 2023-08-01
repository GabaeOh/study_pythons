string = "Yojulab !"
len(string) #길이를 알수 있게끔
pass # 코드의 동작을 알고 싶을때 쓰임

len(string)
9
# 값이 있는지 없는지 확인하는 코드 
"ju" in string
True
"not" in string
False
"Not" not in string
True

#slicing
print(string[1:3])

string[3]
pass
# 'u'

#원하는 값만 추출하는 법
string[3:6] 
#'ula'
string[3:] # 3번째부터 끝까지
#'ulab !'
string[:-2] # 끝에서 
#'Yojulab'
string[::-1]
#'! balujoY'
string[:-1]
#'Yojulab '


# format
age = 36
txt = "My name is John, I am " + str(age) 
print(txt)

txt_second = "My name is John, I am {}."
txt_second
# 'My name is John, I am {}.'
txt_second .format(age)
# 'My name is John, I am 36.'


quantity = 3    # index 0
itemno = 567    # index 1
price = 49.95   # index 2
myorder = "I want {0} pieces of item {1} for {2} dollars. I have just {2}."
myorder.format(quantity,itemno,price)
#'I want 3 pieces of item 567 for 49.95 dollars. I have just 49.95.'

myorderx = "I want {} pieces of item {} for {} dollars. I have just {}."
myorderx.format(quantity,itemno,price,"1526")
# 'I want 3 pieces of item 567 for 49.95 dollars. I have just 1526.'
pass 


