import pandas as pd
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import f1_score, classification_report
import warnings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#PART_2 Q.2(a):
# #reading hansard40000.csw file from the p2-texts directory (subfolder of cwd)
file_path='p2-texts/hansard40000.csv'
df=pd.read_csv(file_path)

#PART_2 Q 2(a)(i):
#re-naming value:'Labour (Co-op)' in 'party' column to 'Labour' 
df['party'] = df['party'].replace('Labour (Co-op)', 'Labour')

print(df['party'].value_counts())


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
print(f"\nQ.2(a)(iv) Final dataframe dimensions: {df.shape}")


#PART_2 Q.2(b):
# #Vectorise the speeches using TfidfVectorizer from scikit-learn.
# #Initialises TfidfVectorizer with adjusted parameters to 3000 max_features (from standard: None) and to remove stopwords (from standard: no stopword removal)
# tfidf_vectorizer = TfidfVectorizer(max_features=3000, stop_words='english')       
# tfidf = tfidf_vectorizer.fit_transform(df['speech'])

# # Splitting of data into train and test sets using stratified sampling (proprtionally to fit dataset and sample)

# # Split using stratified sampling based on 'party' (target variable)
# # X is the TF-IDF matrix, y is party labels
# y = df['party']         #label to predict

# X_train, X_test, y_train, y_test = train_test_split(
#     tfidf, y, 
#     test_size=0.2,                  #default 80/20split
#     random_state=26,                #for reproducible results
#     stratify=y
# )

# #PART_2 Q.2(c):

warnings.filterwarnings('ignore') #to suppress not helpful warnings about zero division

# #(1) Random forest classifier
# rf_classifier = RandomForestClassifier(n_estimators=300, random_state=26)
# rf_classifier.fit(X_train, y_train)
# rf_predictions = rf_classifier.predict(X_test)      # Predict on test set
# rf_f1_macro = f1_score(y_test, rf_predictions, average='macro')        # Calc macro-average F1 score

# print(f"\nQ.2(c) Random Forest Macro-Average F1 Score: {rf_f1_macro:.4f}")
# print("Q.2(c) Random Forest Classification Report:")
# print(classification_report(y_test, rf_predictions))


# #(2) SVM with Linear Kernel
# svm_classifier = SVC(kernel='linear', random_state=26)
# svm_classifier.fit(X_train, y_train)
# svm_predictions = svm_classifier.predict(X_test)    # Predict on test set
# svm_f1_macro = f1_score(y_test, svm_predictions, average='macro')       # Calc macro-average F1 score

# print(f"\nQ.2(c) SVM Macro-Average F1 Score: {svm_f1_macro:.4f}")
# print("Q.2(c) SVM Classification Report:")
# print(classification_report(y_test, svm_predictions))


# #PART_2 Q.2(d):
# #TfidfVectorizer with parameters as in to Q2(b) & additionally: bi- and tri-grams (n_gram added)

# tfidf_vectorizer=TfidfVectorizer(max_features=3000, stop_words="english", ngram_range=(1,3))
# tfidf=tfidf_vectorizer.fit_transform(df["speech"])

# #splitting data into train & test set
# y=df["party"]           #label to predict
# X_train, X_test, y_train, y_test = train_test_split(
#     tfidf, y, 
#     test_size=0.2,                  #default 80/20split
#     random_state=26,                #for reproducible results
#     stratify=y
# )

# #(1) Random forest classifier
# rf_classifier = RandomForestClassifier(n_estimators=300, random_state=26)
# rf_classifier.fit(X_train, y_train)
# rf_predictions = rf_classifier.predict(X_test)      # Predict on test set
# rf_f1_macro = f1_score(y_test, rf_predictions, average='macro')        # Calc macro-average F1 score

# print(f"\nQ.2(d) Random Forest Macro-Average F1 Score: {rf_f1_macro:.4f}")
# print("Q.2(d) Random Forest Classification Report:")
# print(classification_report(y_test, rf_predictions))


# #(2) SVM with Linear Kernel
# svm_classifier = SVC(kernel='linear', random_state=26)
# svm_classifier.fit(X_train, y_train)
# svm_predictions = svm_classifier.predict(X_test)    # Predict on test set
# svm_f1_macro = f1_score(y_test, svm_predictions, average='macro')       # Calc macro-average F1 score

# print(f"\nQ.2(d) SVM Macro-Average F1 Score: {svm_f1_macro:.4f}")
# print("Q.2(d) SVM Classification Report:")
# print(classification_report(y_test, svm_predictions))


#PART_2 Q.2(e):
#create my_toenizer to try to improve performance of ppppprevious function output for palamentary speeches

def my_tokenizer(text):
    tokens =word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    parliamentary_stops={"speaker", "order", "hear", "colleague", "colleagues"} 
    stop_words.update(parliamentary_stops)
    return[token for token in tokens if token.isalpha() and token not in stop_words]


tfidf_vectorizer=TfidfVectorizer(tokenizer=my_tokenizer, max_features=3000, 
                                 ngram_range=(1,3), # uni- and bigrams only
                                  min_df=2,         #ignore terms occuring in less than 2 docs
                                  max_df=0.95,      #ignore frequent terms/in more than 95% of docs
                                  sublinear_tf=True)

tfidf=tfidf_vectorizer.fit_transform(df["speech"])

#splitting data into train & test set
y=df["party"]           #label to predict
X_train, X_test, y_train, y_test = train_test_split(
    tfidf, y, 
    test_size=0.2,                  #default 80/20split
    random_state=26,                #for reproducible results
    stratify=y
)


#class_weight='balanced'  # classes are strongly imbalanced, thus handle class imbalance

#(1) Random forest classifier
rf_classifier = RandomForestClassifier(n_estimators=300, random_state=26)  
rf_classifier.fit(X_train, y_train)
rf_predictions = rf_classifier.predict(X_test)      # Predict on test set
rf_f1_macro = f1_score(y_test, rf_predictions, average='macro')        # Calc macro-average F1 score

print(f"\nQ.2(e) Random Forest Macro-Average F1 Score: {rf_f1_macro:.4f}")
print("Q.2(e) Random Forest Classification Report:")
print(classification_report(y_test, rf_predictions))


#(2) SVM with Linear Kernel
svm_classifier = SVC(kernel='linear', random_state=26) 
svm_classifier.fit(X_train, y_train)
svm_predictions = svm_classifier.predict(X_test)    # Predict on test set
svm_f1_macro = f1_score(y_test, svm_predictions, average='macro')       # Calc macro-average F1 score

print(f"\nQ.2(e) SVM Macro-Average F1 Score: {svm_f1_macro:.4f}")
print("Q.2(e) SVM Classification Report:")
print(classification_report(y_test, svm_predictions))