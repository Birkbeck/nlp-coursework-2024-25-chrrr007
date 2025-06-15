
import nltk
import spacy
import os
import glob
from pathlib import Path
import pandas as pd
import csv
import pickle

nlp = spacy.load("en_core_web_sm")      #load spacy pre-trained model
nlp.max_length = 2000000

# Part One 1.(a)(i):
def read_novels(path):
    #txt_files = list(path.glob("*.txt"))
    all_files = list(path.glob("*.*"))
    txt_files= list(path.glob("*.txt"))    
    print(f"Files with any extension: {[f.name for f in all_files]}\n")

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

#Part One 1.(b):
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
    print(f"Found {len(txt_files)} files to process:")

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

    print(f"Total entries in dictionary: {len(ttr_dict)}\n")  # to check as it didn't work 
    return ttr_dict
    
#----------------------------    
# Part One 1.(c):

def count_syl(word, d):
    """Counts the number of syllables in a word given a dictionary of syllables per word.
    if the word is not in the dictionary, syllables are estimated by counting vowel clusters

    Args:
        word (str): The word to count syllables for.
        d (dict): A dictionary of syllables per word.

    Returns:
        int: The number of syllables in the word.
    """
    word = word.lower()
    if word in d:
        return len([phoneme for phoneme in d[word][0] if phoneme[-1].isdigit()])
    else:
        vowels = "aeiouy"
        syllables = 0
        prev_was_vowel = False
        for char in word:
            is_vowel = char.lower() in  vowels
            if is_vowel and not prev_was_vowel:
                syllables +=1
            prev_was_vowel = is_vowel
        return max(1, syllables)

def fk_level(text, d):
    """Returns the Flesch-Kincaid Grade Level of a text (higher grade is more difficult).
    Requires a dictionary of syllables per word.

    Args:
        text (str): The text to analyze.
        d (dict): A dictionary of syllables per word.

    Returns:
        float: The Flesch-Kincaid Grade Level of the text. (higher grade is more difficult)
    """
    sentences = nltk.sent_tokenize(text)
    tokens = nltk.word_tokenize(text)

    filtered_tokens = []
    for token in tokens:
        if token.isalpha() and not token.isspace():
            filtered_tokens.append(token.lower())

    if len(sentences)== 0 or len(filtered_tokens) ==0:
        return 0

    avg_sentence_length = len(filtered_tokens)/len(sentences)

    total_syllables=0
    for word in filtered_tokens:
        total_syllables += count_syl(word, d)

    avg_syllables_per_word=total_syllables/len(filtered_tokens)

    grade_level = (0.39 * avg_sentence_length) + (11.8 * avg_syllables_per_word) - 15.59
 
    # print(f"Sentences: {len(sentences)}")                         #got weird FK-scores added as a check to see if those numbers are in expected range
    # print(f"Filtered tokens: {len(filtered_tokens)}")
    # print(f"Avg sentence length: {avg_sentence_length}")
    # print(f"Total syllables: {total_syllables}")
    # print(f"Avg syllables per word: {avg_syllables_per_word}")

    return grade_level
    

def get_fks(df):
    """helper function to add fk scores to a dataframe"""
    results = {}
    cmudict = nltk.corpus.cmudict.dict()
    for i, row in df.iterrows():
        results[row["title"]] = round(fk_level(row["text"], cmudict), 4)
    return results

#----------------------------    
# Part One 1.(e)(i):

def parse_texts(df):
    """
    Process texts with spaCy's tokenizer and parser, and store the processed texts.
    Use spaCy nlp method to add new column to the dataframe that contains parsed and tokenized Doc objects.
    """
    print(f"Processing {len(df)} texts with spaCy...")
    df['parsed'] = df['text'].apply(nlp)        
    
    print("spaCy processing finished! \n")         # thougt it's useful to see when process finished
    return df

#----------------------------    
# Part One 1.(e)(ii):
def parse(df, store_path=Path.cwd() / "pickles", out_name="parsed.pickle"):
    """
    Parses the text of a DataFrame using spaCy, stores the parsed docs as a column and writes 
    the resulting  DataFrame to a pickle file"""




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
    print(path)
    print()
    df=read_novels(path)
    print(df.head())
    print()

    

# Part One 1.(b)
   
    # Calculate TTR for all novels
    ttr_results = calculate_ttr_dict()
    print(f"TTRs:")
    print(get_ttrs(df))
    print()

    
    # # Shows results formated / cleaner view
    # print("Novel TTR Results:")
    # print("-" * 50)
    # for title, ttr in ttr_results.items():
    #     print(f"{title:<30}: {ttr:.4f}")

# Part One 1.(c)
    print(f"Flesch_Kincaide_scores:")
    print(get_fks(df))
    print()

# Part One 1.(e)(i)

    df_parsed = parse_texts(df) # to add parsed column to existing df



if __name__ == "__main__":
    main()
    