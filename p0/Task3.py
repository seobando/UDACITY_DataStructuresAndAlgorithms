"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""

import csv

with open("texts.csv", "r") as f:
    reader = csv.reader(f)
    texts = list(reader)

with open("calls.csv", "r") as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

fixed_lines = []
mobile_numbers = []
telemarketers = []
banglore_caller = 0
banglore_receiver = 0

for call in calls:
    if call[0].startswith("(080)"):
        banglore_caller+=1
        receiver_call = call[1]
        if receiver_call.startswith("(140)"):
            telemarketer = receiver_call[1:4]
            if telemarketer not in telemarketers:
                telemarketers.append(telemarketer)
        elif receiver_call.startswith("("):
            fixed_line = receiver_call[0:receiver_call.find(')')+1]
            if fixed_line not in fixed_lines:
                fixed_lines.append(fixed_line)
        elif " " in receiver_call:
            mobile_number = receiver_call[0:4]
            if mobile_number not in mobile_numbers:
                mobile_numbers.append(mobile_number)
        if receiver_call.startswith("(080)"):
          banglore_receiver+=1

#telemarketers.sort()
fixed_lines.sort()
mobile_numbers.sort()

# Part A
print("The numbers called by people in Bangalore have codes:")
for fixed_line in fixed_lines:
    print(fixed_line)
for mobile_number in mobile_numbers:
    print(mobile_number)

# Part B
banglore_percentage = round((banglore_receiver/banglore_caller)*100,2)
print(f"{banglore_percentage} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")