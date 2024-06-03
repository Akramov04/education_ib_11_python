import datetime as dt
date = dt.datetime.now()
birthday = dt.timedelta(days = int(input()))
print((date + birthday).day, (date + birthday).month)