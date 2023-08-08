# 일반적인 import
import modules
result_sum = modules.add(8, 1)

# alias 을 부여해서 import 사용
import modules as mdls # 별칭을 부여 
result_sum = mdls.multiply(8, 1)

# 맵핑된 그룹핑이 된 class가 있을경우 from으로 선택하고 import
from modules import person1 as ps
print(ps['country'])
pass 