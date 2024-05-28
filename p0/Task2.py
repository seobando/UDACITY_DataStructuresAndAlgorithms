"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

phone_dict={}

for call in calls:
	phone_dict[call[0]] = phone_dict.get(call[0], 0) + int(call[3])
	phone_dict[call[1]] = phone_dict.get(call[1], 0) + int(call[3])
     
max_telephone_number = max(phone_dict, key=phone_dict.get)
max_duration = phone_dict[max_telephone_number]

print(f"{max_telephone_number} spent the longest time, {max_duration} seconds, on the phone during September 2016.")