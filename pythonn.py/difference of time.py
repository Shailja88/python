# import datetime as dt 
 
# current_time=dt.datetime.now()
# next_new_year=dt.datetime(2023,1,1)

# time_remaining =next_new_year-current_time

# print(time_remaining)
# print(type(time_remaining))

# import  datetime as dt

# current_datetime=dt.datetime.now()

# print(current_datetime)

# string_date=current_datetime.strftime("%A,%B,%D,%Y")
# print(string_date)
# string_date=current_datetime.stftime("%b %-d,%I%p")
# print(string_date)

import datetime as dt 
date_string ="21 June, 2021"

date_object=dt.datetime.strptime(date_string,"%d %B, %Y")

print("Date object ",date_object)