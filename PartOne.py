#Student ID: 12517261_Claudia Herring-Roehn

import nltk
import spacy
import os
import glob
from pathlib import Path
import pandas as pd
import csv
import pickle

nlp = spacy.load("en_core_web_sm")      #load spacy pre-trained model
nlp.max_length = 2000000                #for Q1(e)(iv):needed to implemented/increase limit to avoid exceeding max leng of spaCy model

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
    # print(f"Found {len(txt_files)} files to process:")          #not required but useful check if all files processed

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
            # print(f"Processed: {title} -> TTR: {ttr:.4f}")      #not required but useful check

        except Exception as e:
            print(f"Error processing {txt_file}: {e}")

    print(f"Q1.(b)Total entries in dictionary: {len(ttr_dict)}\n")  # to check if all processed 
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
        vowels = "aeiouy"    #vowel letters +y
        syllables = 0
        prev_was_vowel = False
        for char in word:
            is_vowel = char.lower() in  vowels
            if is_vowel and not prev_was_vowel:
                syllables +=1
            prev_was_vowel = is_vowel
        return max(1, syllables)

def fk_level(text, d):
    """Returns the Flesch-Kincaid Grade Level of a text (higher grade: more difficult).
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
 
    # print(f"Sentences: {len(sentences)}")                         #got weird FK-scores added as check to see if those numbers are in expected range
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
# # Part One 1.(e)(ii):

def parse(df, store_path=Path.cwd() / "pickles", out_name="parsed.pickle"):
    """
    Parses the text of a DataFrame using spaCy, stores the parsed docs as a column and writes 
    the resulting  DataFrame to a pickle file"""

    # print(f"Processing {len(df)} texts with spaCy...")
    # df['parsed'] = df['text'].apply(nlp)
    # print("spaCy processing finished! \n")
    
    # print("Serialization...")  # implemented as code didn't run, seems useful to see wher problems occure
    
    try:
        # print("Creating directory...")  # implemented as code didn't run, seems useful to see where problems occure
        store_path.mkdir(exist_ok=True)
        
        filepath = store_path / out_name
        print(f"Serializing DataFrame to {filepath}")
        
        with open(filepath, "wb") as f:
            pickle.dump(df, f)
        
        print(f"DataFrame saved as {out_name} \n")
        
    except Exception as e:
        print(f"Error during serialization: {e}")
    
    # print("Done...")  # confirmation for exceution - felt useful

# Part One 1.(e)(iii):    
    return df
# #----------------------------    


# Part One 1.(f)(i):

from collections import Counter

def syntactic_objects_counts(doc):
    """Extracts the most common syntactic objects (dependency labels) for each novel."""
    syntactic_objects= Counter()
    
    for token in doc:
        syntactic_objects[token.dep_] += 1
        
    return syntactic_objects.most_common(10)


# Part One 1.(f)(ii):
def subjects_by_verb_count(doc, verb):
#     """Extracts the most common subjects of a given verb in a parsed document. Returns a list."""
    subjects = Counter()

    for token in doc:
        if token.lemma_ == verb:
            for child in token.children:
                if child.dep_ == "nsubj":
                    subjects[child.lemma_]+=1
    return subjects.most_common(10)


# Part One 1.(f)(iii)
import math
def subjects_by_verb_pmi(doc, target_verb):                               
#     """Extracts the most common subjects of a given verb in a parsed document. Returns a list."""

    # I reuse existing/previous function-subject counts
    subject_count_list=subjects_by_verb_count(doc, target_verb)
    subjects_of_target_verb=dict(subject_count_list)

    # pre calc for PMI
    all_subjects=Counter()
    all_verbs=Counter()
    total_tokens = 0

    for token in doc:
        if token.dep_ == "nsubj":
            all_subjects[token.lemma_] +=1
        if token.pos_ == "VERB":
            all_verbs[token.lemma_] += 1
        total_tokens +=1

    pmi_scores=[]
    for subject, joint_count in subjects_of_target_verb.items():
        p_subject_verb=joint_count/total_tokens
        p_subject=all_subjects[subject]/total_tokens
        p_verb=all_verbs[target_verb]/ total_tokens

        if p_subject>0 and p_verb>0:
            pmi= math.log2(p_subject_verb/(p_subject*p_verb))
            pmi_scores.append((subject, joint_count, pmi))

    pmi_scores.sort(key=lambda x: x[2], reverse=True)

    return [(subject, count) for subject, count, pmi in pmi_scores[:10]]


#==========================================================
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
    print(f"Q1.(a)(ii)_DF sorted by year:")
    print(df.head())
    print()

    

# Part One 1.(b)
   
    # Calculate TTR for all novels
    ttr_results = calculate_ttr_dict()
    print(f"Q1.(b)_TTRs:")
    print(get_ttrs(df))
    print()

    
    # # Shows results formated / cleaner view
    # print("Novel TTR Results:")
    # print("-" * 50)
    # for title, ttr in ttr_results.items():
    #     print(f"{title:<30}: {ttr:.4f}")

# Part One 1.(c)
    print(f"Q1.(c)_Flesch_Kincaide_scores:")
    print(get_fks(df))
    print()

# # Part One 1.(e)(i) & 1.(e)(iii): 

    df_parsed = parse(df) # to add parsed column to existing df and saves to pickle file


# Part One 1.(e)(iv): 

    df= pd.read_pickle(Path.cwd() / "pickles" / "parsed.pickle")        #load Df from pickle file
    
    print(f"\nQ1.(e)(iv)_Loaded DataFrame with {len(df)} texts:")          # To make sure DataFrame loaded
    print(f"Columns: {list(df.columns)}")
    print(df.head())
    
    # print("\nTTR scores from loaded DataFrame:")      #to compare to nltk approach not required 
    # print(get_ttrs(df))
    

    # print("\nFlesch-Kincaid scores from loaded DataFrame:") #to compare to nltk approach not required
    # print(get_fks(df))
    # print()

    # first_doc = df.iloc[0]['parsed']                        #just to get a overview for the data
    # print(f"First novel has {len(first_doc)} tokens")
    # print(f"Sample tokens: {[token.text for token in first_doc[:10]]}")

# Part One 1.(f)(i):

    df = pd.read_pickle(Path.cwd() / "pickles" / "parsed.pickle")
    print("\nQ1.(f)(i)_syntactic_objects_counts:")          
    for i, row in df.iterrows():
        print(row["title"])
        print(syntactic_objects_counts(row["parsed"]))
        print("\n")


# Part One 1.(f)(ii):
    # df = pd.read_pickle(Path.cwd() / "pickles" / "parsed.pickle")
    print("subjects_by_verb_count:")
    for i, row in df.iterrows():
        print(row["title"])
        print(subjects_by_verb_count(row["parsed"], "hear"))
        print("\n")


# Part One 1.(f)(iii):
    print("subjects_by_verb_pmi:")
    for i, row in df.iterrows(): 
        print(row["title"])
        print(subjects_by_verb_pmi(row["parsed"], "hear"))
        print("\n")


if __name__ == "__main__":
    main()
    

   