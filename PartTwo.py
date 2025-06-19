import pandas as pd
import os

#PART 2Q. 2(a):
# #reading hansard40000.csw file from the p2-texts directory (subfolder of cwd)
file_path='p2-texts/hansard40000.csv'
df=pd.read_csv(file_path)

#to show basic indformation of data
print("Dataset shape:", df.shape)
print("\nColumn names:")
print(df.head())

#PART 2Q. 2(a)(i):
#re-naming 'Labour (Co-op)' to 'Labour' in column: "party"
df['party'] = df['party'].replace('Labour (Co-op)', 'Labour')

#print(df['party'].value_counts())

#PART 2Q. 2(a)(ii):
#Removing rows where party column has value: 'Speaker' 
df = df[df['party'] != 'Speaker']

# Getting 4 most common party names
top_4_parties = df['party'].value_counts().head(4).index.tolist()       

# Filter dataframe to keep only rows with these four parties
df = df[df['party'].isin(top_4_parties)]
