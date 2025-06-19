import pandas as pd
import os

#reading hansard40000.csw file from the p2-texts directory (subfolder of cwd)
file_path='p2-texts/hansard40000.csv'
df=pd.read_csv(file_path)

#to show basic indformation of data
print("Dataset shape:", df.shape)
print("\nColumn names:")
print(df.head())


#re-naming 'Labour (Co-op)' to 'Labour' in column: "party"
df['party'] = df['party'].replace('Labour (Co-op)', 'Labour')

print("\nUnique values in 'party' column:")
print(df['party'].value_counts())

#Removing rows where party column has value: 'Speaker' 
print(f"\nBefore removing 'Speaker' rows: {len(df)} rows")      #remove once final df outpt as requested
df = df[df['party'] != 'Speaker']
print(f"After removing 'Speaker' rows: {len(df)} rows")         #remove once final df outpt as requested

print(df['party'].value_counts())                               #remove once final df outpt as requested