import datetime

# print today
today = datetime.datetime.now()

# today
datetime.datetime(2023, 8, 4, 18, 14, 5, 604539)
type(today)
# <class 'datetime.datetime'>

someday = datetime.datetime(2023, 8, 3)
pass

someday - today
# datetime.timedelta(days=-5, seconds=50532, microseconds=495141)

datetime.datetime(2012, 2, 2)
# datetime.datetime(2012, 2, 2, 0, 0)

50532 / (24 * 60 * 60) # 하루를 나타내는 초 
# 0.5848611111111112

somedelta = someday - today
type(somedelta)
# <class 'datetime.timedelta'>

classday = datetime.datetime(2023, 4, 26)
pass
today - classday
datetime.timedelta(days=103, seconds=36663, microseconds=939026)