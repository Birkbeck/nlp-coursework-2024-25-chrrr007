
import nltk
import spacy
import os
import glob
from pathlib import Path
import pandas as pd
import csv


#Part One 1.(a)(i)
def read_novels(path):
    txt_files = list(path.glob("*.txt"))
    #print(f"Files with any extension: {[f.name for f in txt_files]}")
    
    texts = []
    titles = []
    authors = []
    years = []
       
    for file_path in txt_files:
        try:
            with open (file_path, 'r', encoding='utf-8') as file:
                text_content = file.read()                            # Read entire file content
            #print(f"Contents of {txt_file}:\n{content}\n")         # Print the content
    
            filename = file_path.stem   # removes .txt, keeps only part from path we need

            parts = filename.split('-')

            if len(parts) >= 3:
                title = parts[0].strip().replace("_", " ")
                author = parts[1].strip().replace("_", " ")
                year_str = parts[2].strip().replace("_", " ")

                # Convert year to integer
                year = int(year_str)                

                texts.append(text_content)
                titles.append(title)
                authors.append(author)
                years.append(year)

            else:
                print(f"Error: Filename '{filename}' not in format (title-author-year)")
            
        except Exception as e:
            print(f"Error processing file '{file_path}': {e}")
    df = pd.DataFrame({
        "text": texts,
        "title": titles,
        "author": authors,
        "year": years
    })    

# Part One 1.(a)(ii)
    
    df = df.sort_values("year").reset_index(drop=True) 
    return df






def main():


    path = Path.cwd() / "p1-texts" / "novels"
    #print(path)
    df=read_novels(path)
    print(df.head())

    
    # print(df.head())     # First 5 rows
    # print(df.head(3))    # First 3 rows
    # print(df.shape)






if __name__ == "__main__":
    main()
    