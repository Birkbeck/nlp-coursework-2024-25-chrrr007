
import nltk
import spacy
import os
import glob
from pathlib import Path
import pandas as pd
import csv


#Part One 1.(a)(i)
def read_novels(path):
    #txt_files = list(path.glob("*.txt"))
    all_files = list(path.glob("*.*"))
    txt_files= list(path.glob("*.txt"))    
    print(f"Files with any extension: {[f.name for f in all_files]}")

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

#----------------------------

#Part One 1.(b)
def nltk_ttr(text):
#     """Calculates the type-token ratio of a text. Text is tokenized using nltk.word_tokenize."""

    tokens= nltk.word_tokenize(text)
    # Get tokens, filtering out punctuation and spaces
    filtered_tokens = []
    
    for token in tokens:
        if token .isalpha() and not token.isspace():
            filtered_tokens.append(token.lower())

    # Calculate TTR
    if len(filtered_tokens)> 0:
        types = set(filtered_tokens)
        ttr =  len(types)/len(filtered_tokens)
        return ttr
    else:
        return 0
    
def get_ttrs(df):
    results = {}
    for i, row in df.iterrows():
        results[row["title"]] = nltk_ttr(row["text"])
    return results

def calculate_ttr_dict(path=Path.cwd() / "p1-texts" / "novels"):
    ttr_dict ={}

    txt_files = list(path.glob("*.txt"))
    print(f"Found {len(txt_files)} files to process")

    # Process each text file
    for txt_file in txt_files:
        try:
            with open(txt_file, 'r', encoding='utf-8') as file:
                content = file.read()
        
            # Get filename without path for display
            filename = os.path.basename(txt_file)

            #get filenames before hyphen
            title = filename = filename.split("-")[0]   #.replace("_", "")
        
            # Calculate TTR using NLTK
            ttr = nltk_ttr(content)

            ttr_dict[title]=ttr
            print(f"Processed: {title} -> TTR: {ttr:.4f}")

        except Exception as e:
            print(f"Error processing {txt_file}: {e}")

    print(f"Total entries in dictionary: {len(ttr_dict)}")  # to check as it didn't work 
    return ttr_dict
    
#----------------------------    
# Part One 1.(c)








#----------------------------
def main():

    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')

    try:
        nltk.data.find('corpora/cmudict')
    except LookupError:
        nltk.download('cmudict')    

# Part One 1.(a)(i) & (ii)

    path = Path.cwd() / "p1-texts" / "novels"
    #print(path)
    df=read_novels(path)
    print(df.head())

    

# Part One 1.(b)
   
    # Calculate TTR for all novels
    ttr_results = calculate_ttr_dict()
    print(get_ttrs(df))

    
    # Display results formated to get cleaner view
    print("Novel TTR Results:")
    print("-" * 50)
    for title, ttr in ttr_results.items():
        print(f"{title:<30}: {ttr:.4f}")

# Part One 1.(c)




if __name__ == "__main__":
    main()
    