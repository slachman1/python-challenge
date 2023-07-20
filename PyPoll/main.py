# import modules
import os
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

#row count to count votes and total votes variable
row_count = 0
total_amount = 0

#candidate vote total variables
ccs_votes = 0
dd_votes = 0
rad_votes = 0


with open(csvpath, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip to the second row
    for row in reader:
        row_count += 1
        ballot_id = row[0]
        county = row[1]
        candidate = row[2]
        if candidate == "Charles Casper Stockham": # count for charles
            ccs_votes += 1
            pct_ccs_votes = (ccs_votes / row_count)*100
        if candidate == "Diana DeGette": # count for diana
            dd_votes += 1
            pct_dd_votes = (dd_votes / row_count)*100
        if candidate == "Raymon Anthony Doane": # count for raymond
            rad_votes += 1
            pct_rad_votes = (rad_votes / row_count)*100

# first set of print statements
print("Election Results")
print("----------------------")
print(f"Total Votes: {row_count}")
print("----------------------")
print(f"Charles Casper Stockham: {pct_ccs_votes:.2f}% ({ccs_votes})")
print(f"Diana DeGette: {pct_dd_votes:.2f}% ({dd_votes})")
print(f"Raymon Anthony Doane: {pct_rad_votes:.2f}% ({rad_votes})")
print("----------------------")

# looks at totals and finds winner
if ccs_votes > dd_votes and ccs_votes > rad_votes:
    print("Winner: Charles Casper Stockham")
if dd_votes > ccs_votes and dd_votes > rad_votes:
    print("Winner: Diana DeGette")
if rad_votes > ccs_votes and rad_votes > dd_votes:
    print("Winner: Raymon Anthony Doane")
print("----------------------")