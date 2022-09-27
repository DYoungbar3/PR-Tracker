#!/usr/bin/env python3

#This is my idea for a first decent sized project.
#I want to track lifting PR's with different lifts,
#able to create any name for the lifts, as many as
#lifts I want, notes available for every one.

import csv
import pandas as pd

#Rep to 1RM Formula: weight/(1.0278 - 0.0278*reps)'

def main():
    #Either input new info, or have the option to just look at current info
    yes_no = input('Are you inputting a new PR? (type yes or no): ')
    if yes_no.lower() == 'no' or yes_no.lower() == 'n':
        print_table()
    elif yes_no.lower() =='yes' or yes_no.lower() =='y':
        new_pr()
        print_table()

def new_pr():
    #Get the new info from user
    lift = input('Name of lift: ')
    date = input('Date lift was completed: ')
    weight = input('Weight completed on the lift: ')
    reps = input('Number of reps done with the lift: ')
    notes = input('Short notes: ')

    #Create dictionary of the input
    pr_dict = [{'Lift':lift, 'Date':date, 'Weight':weight, 'Reps':reps, 'Notes':notes}]

    #Use dict to create DataFram and put it into the table
    df = pd.DataFrame(pr_dict)
    df.to_csv('pr_table.csv', mode='a', index=False, header=False)

def print_table():
    #Read table, sort by date, then print
    my_table = pd.read_csv('pr_table.csv')
    my_table = my_table.sort_values('Date', ascending=False)
    print(my_table)

#Call main function
if __name__ == '__main__':
    main()
