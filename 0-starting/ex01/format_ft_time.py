import time
from datetime import datetime

# Get the current timestamp
timestamp = time.time()

# print seconds in format , and scientific notation
# 1 Jan 1970 is beginning of time that developer chose
print(f"Seconds since January 1, 1970: {timestamp:,.4f} or \
      {timestamp:.2e} in scientific notation")

# date_time is class that have year, month, day, hr, mins, sec, millisec
date_time = datetime.fromtimestamp(timestamp)

# strftime() need class datetime to use this format.
print(date_time.strftime("%b %d %Y"))

"""
print in format Month Day Year
the reason of %b is
%b	Sep	Month as locale’s abbreviated name.
%B	September	Month as locale’s full name.
if you wanna know more -> https://strftime.org/
"""
