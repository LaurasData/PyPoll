# PyPoll
Perform analysis+ to include audit of election_results.csv data for the Colorado Board of Elections

## Overview of Project
      Four Deliverables: Three technical deliverables and a One written summary  
      1. Total number of votes cast
      2. A complete list of candidates who received votes
      3. Percentage of votes each candidate won
      4. The winner of the election based on popular vote

   https://github.com/LaurasData/PyPoll/blob/main/Election_Analysis/PyPoll.py
   https://github.com/LaurasData/PyPoll/blob/main/Election_Analysis/election_results.png
   https://github.com/LaurasData/PyPoll/blob/main/Election_Analysis/election_results.txt


### Resources
      - Data Source: election_Results.csv
      - Software:  Python 3.9.12, Visual Studio Code 1.71.2

  
### Summary
      - The analysis of the election show that:
      - there were 369,711 votes cast in the election
      - The candidates were:
            - Charles Casper Stockham
            - Diana DeGette
            - Raymon Anthony Doane
      - The candidates results were:
            - Candidate Charles Casper Stockham recieved 23.0% of the vote and 85,213 number of the votes.
            - Candidate Diana DeGette recieved of the 73.8% vote and 272,892 number of the votes.
            - Candidate Raymon Anthony Doane recieved 3.1% of the vote and 11,606 number of the votes.
      - The winner of the election was:
            - Candidate Diana DeGette, who recieved of the 73.8% vote and 272,892 number of the votes.

### Analysis and Challenges 
      - Indenting changes how Python executes modules and varibles need to be set early in modules
      -  Python uses '\' for window's path separators
      -  Type 'python' on the gitbash terminal command line to activate python libraries '>>>' (command line prompt). 
            Type in command line 'exit()' to quit python and close the terminal window.
      -  To paste text in gitbash terminal windows (shift+Ctrl+V)
      -  To run python code >>> exit() to $commandlineprompt and type 'python'  and the file. ie. $ python PyPoll.py
      
### Challenges and Difficulties Encountered
      - to complete Section 3.4.3, additional directories had to be created 
                        Resources and Analysis had to be created on the local root homework directory
      - Setup immediatly after the root directory or the coding doesn't work
      - PyPoll.py file stays in the root homework directory
                        

## Results on Development Processes
      - What are two development observations?
            - 1. StreamLine two refactor steps into one.
                 b. The readme.md file creation provides a Logic-Flow-Outline for pseudocode development.
                 a. Document observations in readme.md and as one does the assignment
                        i. Logic-scaffolding for pseudocode development is completed.
            - 2. Refactor Python 
                  a. Use 'with' instead of open() and close() to daisy-chain dependenies and clean up coding
                  b. Refactor scaffolding into #To Do: comment sections in the python code to notate next steps 
                  with completion comment developer's initials and date last edited '(LS.09252022)'
             
             
      - What can you conclude about this development process?
            - 1. Understanding the logic behind Module.Class.Method was my uh-ha moment. A drill-down just like a directoy tree
            - 2. Hance the dependencies are the directory trees (bread-crumbs) to drill down
                   to activate functions within each module.  ie datetime.datetime.now()
    
      - What are some limitations of this dataset?
            - 1. Do not have trusted source code to Convert from default(Windows-1252) to UTF-8
            - 2.  #To do: Convert from Windows-1252 to UTF-8 (LS.09252022 'Recommendation ')
                        https://stackoverflow.com/questions/15502619/correctly-reading-text-from-windows-1252cp1252-file-in-python
                              import sys
                              reload(sys)
                              sys.setdefaultencoding('utf-8')

                        Needs instructors review before added to PyPoll.py
