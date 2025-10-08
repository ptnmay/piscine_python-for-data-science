import time
from datetime import datetime

# Get the current timestamp
timestamp = time.time()

# Print seconds since Jan 1, 1970 in both normal and scientific format
print(f"Seconds since January 1, 1970: {timestamp:,.4f} or {timestamp:.2e} in scientific notation")

# Get the current date and format as "Mon DD YYYY"
current_date = datetime.now().strftime("%b %d %Y")
print(current_date + "\n")
