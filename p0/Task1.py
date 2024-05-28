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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

# Declare variables
all_numbers = []
unique_numbers = []

texts_len = len(texts)
calls_len = len(calls)

max_len = max([texts_len, calls_len])

call_unique_numbers = []
text_unique_numbers = []


# Declare functions
def get_unique_values_from_pair_of_records(record):
    send_number = record[0]
    receive_number = record[1]
    unique_numbers = [send_number]

    if send_number != receive_number:
        unique_numbers = [send_number, receive_number]
        return unique_numbers

    return unique_numbers


def add_unique_records(unique_numbers, list_1):
    if len(list_1) == 1:
        if list_1[0] not in unique_numbers:
            unique_numbers.append(list_1[0])

    if len(list_1) == 2:
        if list_1[0] not in unique_numbers:
            unique_numbers.append(list_1[0])

        if list_1[1] not in unique_numbers:
            unique_numbers.append(list_1[1])

    return unique_numbers

def get_unique_values_from_lists(unique_numbers, list_1, list_2):
    unique_numbers = add_unique_records(unique_numbers, list_1)
    unique_numbers = add_unique_records(unique_numbers, list_2)

    return unique_numbers


# Execution
for p in range(max_len):

    if p < texts_len:
        text = texts[p]
        text_unique_numbers = get_unique_values_from_pair_of_records(text)

    if p < calls_len:
        call = calls[p]
        call_unique_numbers = get_unique_values_from_pair_of_records(text)

    unique_numbers = get_unique_values_from_lists(
        unique_numbers, text_unique_numbers, call_unique_numbers
    )

print(f"There are {len(unique_numbers)} different telephone numbers in the records.")