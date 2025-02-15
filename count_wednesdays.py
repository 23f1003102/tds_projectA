from datetime import datetime

# Possible date formats
date_formats = [
    "%Y-%m-%d",      # 2004-07-17
    "%d-%b-%Y",      # 14-Jun-2014, 06-Feb-2004, 12-May-2017
    "%b %d, %Y",     # Jun 03, 2020, Jan 21, 2006, Feb 22, 2002
    "%Y/%m/%d %H:%M:%S"  # 2002/03/30 23:08:32, 2020/03/10 00:06:37
]

# Read dates from the file
with open("dates.txt", "r") as file:
    dates = file.readlines()

wednesday_count = 0

for date in dates:
    date = date.strip()
    for fmt in date_formats:
        try:
            if datetime.strptime(date, fmt).weekday() == 2:  # Wednesday = 2
                wednesday_count += 1
            break  # Stop trying formats once we find a match
        except ValueError:
            continue  # Try the next format

# Write the result
with open("dates-wednesdays.txt", "w") as output_file:
    output_file.write(str(wednesday_count))
