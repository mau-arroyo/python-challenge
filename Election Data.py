import pandas as pd
import os
import csv
import operator

file_path = "election_data.csv"
election_df = pd.read_csv(file_path)

with open("election_data.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    
    csv_header = next(csv_reader)
    num_votes = 0
    dictionary = {}
    cand1 = 0
    cand2 = 0
    cand3 = 0
    cand4 = 0
    
    for row in csv_reader:
        num_votes+=1
        
        if row[2] == "Khan":
            cand1+=1
            
        elif row[2] == "Correy":
            cand2+=1
            
        elif row[2] == "Li":
            cand3+=1
            
        elif row[2] == "O'Tooley":
            cand4+=1
            
        
            
    dictionary = {"Khan":cand1, "Correy":cand2, "Li":cand3, "O'Tooley":cand4}
    
    winner = max(dictionary.items(), key=operator.itemgetter(1))[0]
    
    
    print("Election Results")
    print("---------------------------------")
    print("Total Votes = " + str(num_votes))
    print("---------------------------------")
    print("Khan: " + str(cand1))
    print("Correy: " + str(cand2))
    print("Li: " + str(cand3))
    print("O'Tooley: " + str(cand4))
    print("---------------------------------")
    print("Winner = " + str(winner))