import pandas as pd
import csv

spreadsheet = pd.read_excel('Roles.xlsx')  # create dataset
records = {}  # create dictionary for values
records_array = []
non_unique = []  # create array for non-unique lines index
non_unique_array = []
row_number = spreadsheet.shape[0]

print(str(row_number) + ' rows')

# using array
for i in range(1, row_number+1):
    key1 = spreadsheet.iloc[i-1, 0] + spreadsheet.iloc[i-1, 1]
    key2 = spreadsheet.iloc[i - 1, 1] + spreadsheet.iloc[i - 1, 0]

    try:
        non_unique_index = records_array.index(key1)
        non_unique_array.append(i+1)
    except ValueError:
        records_array.append(key1)
        records_array.append(key2)

# using dictionary
    # if records.get(key1) is None and records.get(key2) is None:
    #     records[key1] = i+1  # save excel index as a value
    #     records[key2] = i+1
    # else:  # found non-unique key
    #     # # if only one combination is non-unique
    #     # if records.get(key1) is None:
    #     #     records[key2] = 'Non-unique'
    #     # elif records.get(key2) is None:
    #     #     records[key1] = 'Non-unique'
    #     # else:  # both combinations are non-unique
    #     non_unique_index = records[key1]
    #     records[key1] = records[key2] = 'Non-unique ' + str(key1) + ' index ' + str(non_unique_index)
    #     non_unique.append(i + 1)  # save excel index of non-unique line

# print(non_unique)
print(non_unique_array)

# save to excel via pandas
# save_df = pd.DataFrame(data=records, index=[0])
# save_df = (save_df.T)
# save_df.to_excel('records.xlsx')

# save to excel via csv
# with open('records.csv', 'w', newline='') as records_csv:
#     writer = csv.DictWriter(records_csv, fieldnames=records.keys())
#     writer.writeheader()
#     writer.writerow(records)
