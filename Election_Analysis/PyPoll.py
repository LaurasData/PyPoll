# the data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes (Directory)
# 3. The percentage (of the whole) of votes each canadidate won
# 4. the total number of votes each candidate won (count by candidate)
# 5. the winner of the election based on popluat votes (max)



# Add our dependencies (modules)
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
    
    
     #txt_file.write("Counties in the Election\n--------------------------\n")
     #txt_file.write("Arapahoe\nDenver\nJefferson")
     #To do: Convert from Windows-1252 to UTF-8