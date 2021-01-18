#import libraries
import os
import csv
import pandas as pd

#create data frame 
csv_path = os.path.join('Resources', 'week-3-python_homework_PyPoll_Resources_election_data.csv')
poll_df = pd.read_csv(csv_path, low_memory=False)

#calculating results
tot_votes = len(poll_df)

can_votes = poll_df.groupby(['Candidate'],sort=False).agg({'Voter ID': 'count'},index=True)
can_votes["Percent"] = can_votes.apply(lambda x:  100*x / x.sum())

#print results
print(f"Election Results ")
print(f"***********************" )
print(f"Total Votes: {tot_votes}")
print(f"***********************" )
print(can_votes)
print(f"***********************" )
print(f"Winner: {can_votes.index[0]}")


#writing to file
file1 = open("Output.txt","w") 
file1.write(f"Election Results \n")
file1.write(f"***********************\n" )
file1.write(f"Total Votes: {tot_votes}\n")
file1.write(f"***********************\n" )
file1.write(str(can_votes)+"\n")
file1.write(f"***********************\n" )
file1.write(f"Winner: {can_votes.index[0]}\n")
file1.close()