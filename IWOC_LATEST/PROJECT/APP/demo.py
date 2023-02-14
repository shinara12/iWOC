
import datetime
from datetime import datetime
from datetime import date
date1= date.today()  # date today
now = datetime.now() # time now
process_start_time = now.strftime("%H:%M:%S")
print(process_start_time,'stime')
print(date1)
now = datetime.now() # time now
process_end_time = now.strftime("%H:%M:%S")
print(process_end_time)


