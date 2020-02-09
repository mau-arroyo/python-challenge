import csv
import os

with open('budget_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    csv_header = next(csv_reader)
    numbermonths=0
    total = 0
    
    dictionary = {}
    
    for row in csv_reader:
        numbermonths+=1
        total+=int(row[1])
        
        
        if numbermonths == 1:
            inicial = int(row[1])
            
        else:
            actual = int(row[1])
            change = actual - inicial
            inicial = actual
            
            dictionary[row[0]] = change
    
    average_change = (sum(dictionary.values())/(numbermonths - 1))
    greatest_increase = (max(dictionary.values()))
    greatest_decrease = (min(dictionary.values()))


    print("Financial Analysis")
    print("--------------------------------------")
    print("Total Months = " + str(numbermonths)) 
    print("Total = $" + str(total))
    print("average change = " + str(average_change))
    print("Greatest Increase in Profits = $" + str(greatest_increase))
    print("Greatest Decrease in Profits = $" + str(greatest_decrease))