import datetime
from datetime import datetime
from datetime import date

# mytime = datetime.time(13,20,1,20)

# print(mytime)

# today = datetime.date.today()
# print(today)

# print(today.ctime())

# mydatetime = datetime(2021,10,3,14,20,1)



# mydatetime = mydatetime.replace(year=2023)
# print(mydatetime)


date1 = date(2021,11,3)
date2 = date(2020,11,3)

result = date1 - date2

print(result)

datetime1 = datetime(2021,11,3,22,0)
datetime2 = datetime(2020,11,3,12,0)

datetime1 - datetime2
