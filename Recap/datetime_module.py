import datetime as dt

now = dt.datetime.now()

year = now.year
month = now.month
day = now.day
minute = now.minute
second = now.second
weekday = now.weekday()

''' YOU CAN SET YOUR OWN TIME '''

date_of_birth = dt.datetime(year=1987, month=8, day=7, hour=10, minute=30)
print(date_of_birth)