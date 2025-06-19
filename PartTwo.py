import pandas as pd
import os

#PART_2 Q.2(a):
# #reading hansard40000.csw file from the p2-texts directory (subfolder of cwd)
file_path='p2-texts/hansard40000.csv'
df=pd.read_csv(file_path)

#PART_2 Q 2(a)(i):
#re-naming value:'Labour (Co-op)' in 'party' column to 'Labour' 
df['party'] = df['party'].replace('Labour (Co-op)', 'Labour')

#print(df['party'].value_counts())


#PART_2 Q.2(a)(ii):
#Removing any rows where party column has value: 'Speaker' 
df = df[df['party'] != 'Speaker']

#Filtering for the 4 most common party names
top_4_parties = df['party'].value_counts().head(4).index.tolist()       

#Removes any row where the value of 'party' column is not on of the 4 most common party names
df = df[df['party'].isin(top_4_parties)]


#PART_2 Q.2(a)(iii):
# Removes any rows where the value in the column 'speech_class' is not 'Speech'
df = df[df['speech_class'] == 'Speech']


#PART_2 Q.2(a)(iv):
# Removes any rows where the text in the column 'speech' is less than 1.000 characters long
df = df[df['speech'].str.len() >= 1000]
#prints dimensions of the resulting dataframe using shape methode
print(f"\nFinal dataframe dimensions: {df.shape}")

