#Re-assessment template 2025

# Note: The template functions here and the dataframe format for structuring your solution is a suggested but not mandatory approach. You can use a different approach if you like, as long as you clearly answer the questions and communicate your answers clearly.

import nltk
import spacy
import os
import glob
from pathlib import Path
import pandas

nlp = spacy.load("en_core_web_sm")      #load spacy pre-trained model
nlp.max_length = 2000000


# Determine the directory containing the .txt files - path to the txt file
directory_path = r'C:\Users\ClaudiaRoehn\Desktop\New folder\OneDrive - Home\0_NLP\p1-texts\novels'

# print("contents of directory:")                     #quick test/check to see content of directory and if all txt
# try:
#     files = os.listdir(directory_path)
#     for i, file in enumerate(files, 1):
#         file_path = os.path.join(directory_path, file)
#         is_file = os.path.isfile(file_path)
#         file_size = os.path.getsize(file_path) if is_file else "N/A"
#         print(f"{i}. {file} ({'File' if is_file else 'Directory'}) - Size: {file_size} bytes")
# except FileNotFoundError:
#     print("Directory not found!")


# Part One 1(a): Read the contents of each .txt file
def read_novels(path=Path.cwd() / "p1-texts" / "novels"):
    """Reads texts from a the specified directory of .txt files and returns a DataFrame with the text, title,
    author, and year"""

# Create lists to store data for df
    texts = []
    titles = []
    authors = []
    years = []
    
    # Get all  .txt files in the cwd
    txt_files = list(path.glob("*.txt"))

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

                texts.append(text_content)
                titles.append(title)
                authors.append(author)
                years.append(year_str)

            else:
                print(f"Error: Filename '{filename}' not in format (title-author-year)")

        except Exception as e:
            print(f"Error processing file '{file_path}: {e}")
    df = pd.dataFrame({
        "text": texts,
        "title": titles,
        "author": authors,
        "year": years
    })    
    
    df = df.sort_values("year").reset_index(drop=True)
        
    return df



pass 

def fk_level(text, d):
    """Returns the Flesch-Kincaid Grade Level of a text (higher grade is more difficult).
    Requires a dictionary of syllables per word.

    Args:
        text (str): The text to analyze.
        d (dict): A dictionary of syllables per word.

    Returns:
        float: The Flesch-Kincaid Grade Level of the text. (higher grade is more difficult)
    """
    pass


def count_syl(word, d):
    """Counts the number of syllables in a word given a dictionary of syllables per word.
    if the word is not in the dictionary, syllables are estimated by counting vowel clusters

    Args:
        word (str): The word to count syllables for.
        d (dict): A dictionary of syllables per word.

    Returns:
        int: The number of syllables in the word.
    """
    pass


def read_novels(path=Path.cwd() / "texts" / "novels"):
    """Reads texts from a directory of .txt files and returns a DataFrame with the text, title,
    author, and year"""
    pass


def parse(df, store_path=Path.cwd() / "pickles", out_name="parsed.pickle"):
    """Parses the text of a DataFrame using spaCy, stores the parsed docs as a column and writes 
    the resulting  DataFrame to a pickle file"""
    pass


def nltk_ttr(text):
    """Calculates the type-token ratio of a text. Text is tokenized using nltk.word_tokenize."""
    pass


def get_ttrs(df):
    """helper function to add ttr to a dataframe"""
    results = {}
    for i, row in df.iterrows():
        results[row["title"]] = nltk_ttr(row["text"])
    return results


def get_fks(df):
    """helper function to add fk scores to a dataframe"""
    results = {}
    cmudict = nltk.corpus.cmudict.dict()
    for i, row in df.iterrows():
        results[row["title"]] = round(fk_level(row["text"], cmudict), 4)
    return results


def subjects_by_verb_pmi(doc, target_verb):
    """Extracts the most common subjects of a given verb in a parsed document. Returns a list."""
    pass



def subjects_by_verb_count(doc, verb):
    """Extracts the most common subjects of a given verb in a parsed document. Returns a list."""
    pass



def adjective_counts(doc):
    """Extracts the most common adjectives in a parsed document. Returns a list of tuples."""
    pass



if __name__ == "__main__":
    """
    uncomment the following lines to run the functions once you have completed them
    """
    #path = Path.cwd() / "p1-texts" / "novels"
    #print(path)
    #df = read_novels(path) # this line will fail until you have completed the read_novels function above.
    #print(df.head())
    #nltk.download("cmudict")
    #parse(df)
    #print(df.head())
    #print(get_ttrs(df))
    #print(get_fks(df))
    #df = pd.read_pickle(Path.cwd() / "pickles" /"name.pickle")
    # print(adjective_counts(df))
    """ 
    for i, row in df.iterrows():
        print(row["title"])
        print(subjects_by_verb_count(row["parsed"], "hear"))
        print("\n")

    for i, row in df.iterrows():
        print(row["title"])
        print(subjects_by_verb_pmi(row["parsed"], "hear"))
        print("\n")
    """

