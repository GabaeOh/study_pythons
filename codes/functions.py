# package == module(python)

# 기본 function 구성
def function_name() :  
    pass
    return 0

function_name()
pass

# 평범한 params 이용한 결과값 받기
def add(first, second):
    sum = first + second
    return sum

result_sum = add(4, 6)
pass 

# set defualt value with params
def minus(first, second=0): # second=0 defalt값으로 값이 없으면 0으로 인지하게끔
    result = first - second
    return result

minus(3, 5)
minus(3)

# return tuple datatype
def multiply(first, second=1):
    multiply = first * second
    # like list[multiply, first, second]
    return (multiply, first, second) # tuple로 return

result_tuple =  multiply(3,4)
multiply, first, second = multiply(4)
pass