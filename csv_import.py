# A Program to import a segment of data from a large dataset file to another file 
import csv
import os

file = 'annex2.csv'
output_file = 'annex.csv'

print(file)
selected_rows = []

# Open the input CSV file for reading
with open(file, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    
    # Read and store the rows you want to copy
    for row_num, row in enumerate(reader, start=1):
        if row_num < 31:
            print(f"row num is {row_num}")
            selected_rows.append(row)
        else : break

# Open the output CSV file for writing
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    # Write the selected rows to the output CSV file
    print("writing to output.csv")
    writer.writerows(selected_rows)
    print("done")

print(f"Selected rows copied from {file} to {output_file}.")
