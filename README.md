[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/8qgh5WxD)
# nlp-cw-template25
template for NLP module coursework

__Student ID: 12517261__

Academic Declaration:
“I have read and understood the sections of plagiarism in the College Policy
on assessment oences and confirm that the work is my own, with the work
of others clearly acknowledged. I give my permission to submit my report
to the plagiarism testing database that the College is using and test it using
plagiarism detection software, search engines or meta-searching software.”


General note:
I decided to create a new "test.py" document to develop my code to start from a blank page and copy the provided starter code snippets in order as needed. This appeared cleaner and allowed me to keep the starter code and cleary mark developed parts as done. The commit history will show on the test.py, rather than on the PartOne.py. Once all code is developed I am planning on renaming the test.py to PartOne.py



Result output: Part One 1.(a)(i):
```DF before sorting by year:

                                                text                 title    author  year
0  Book the First--Recalled to Life\n\n\n\n\nI. T...  A Tale of Two Cities   Dickens  1858
1  Your ideas are terrifying and your hearts are ...        Blood Meridian  McCarthy  1930
2  \nThe Picture of Dorian Gray\n\nby\n\nOscar Wi...           Dorian Gray     Wilde  1890
3  SAMUEL BUTLER.\nAugust 7, 1901\n\nCHAPTER I: W...               Erewhon    Butler  1872
4  'Wooed and married and a'.'\n'Edith!' said Mar...       North and South   Gaskell  1855
```

Result output: Part One 1.(a)(ii):

DF after sorting by year:
```
                                               text                  title   author  year
0  \nCHAPTER 1\n\nThe family of Dashwood had long...  Sense and Sensibility   Austen  1811
1  'Wooed and married and a'.'\n'Edith!' said Mar...        North and South  Gaskell  1855
2  Book the First--Recalled to Life\n\n\n\n\nI. T...   A Tale of Two Cities  Dickens  1858
3  SAMUEL BUTLER.\nAugust 7, 1901\n\nCHAPTER I: W...                Erewhon   Butler  1872
4  THE AMERICAN\n\nby Henry James\n\n\n1877\n\n\n...           The American    James  1877
```

Result output: Part One 1.(b):

```<class 'dict'>
{'A_Tale_of_Two_Cities': 0.07072694469399422, 'Blood_Meridian': 0.08568897067593587, 'Dorian_Gray': 0.08355234620193412, 'Erewhon': 0.09151270564132943, 'North_and_South': 0.0549040694681204, 'Orlando': 0.1137245917497168, 'Portrait_of_the_Artist': 0.10472745625841184, 'Sense_and_Sensibility': 0.052847302442989776, 'Tess_of_the_DUrbervilles': 0.07778957979554696, 'The_American': 0.06381607058523676, 'The_Black_Moth': 0.07866588875923765, 'The_Golden_Bowl': 0.047475476259872806, 'The_Secret_Garden': 0.05847231570812455}
```
```
Novel TTR Results:
--------------------------------------------------
A_Tale_of_Two_Cities          : 0.0707
Blood_Meridian                : 0.0857
Dorian_Gray                   : 0.0836
Erewhon                       : 0.0915
North_and_South               : 0.0549
Orlando                       : 0.1137
Portrait_of_the_Artist        : 0.1047
Sense_and_Sensibility         : 0.0528
Tess_of_the_DUrbervilles      : 0.0778
The_American                  : 0.0638
The_Black_Moth                : 0.0787
The_Golden_Bowl               : 0.0475
The_Secret_Garden             : 0.0585
```


Result output: Part One 1.(c):
```
Flesch_Kincaide_scores:
{'Sense and Sensibility': 10.8894, 'North and South': 6.6553, 'A Tale of Two Cities': 9.843, 'Erewhon': 14.6793, 'The American': 7.9875, 'Dorian Gray': 4.9493, 'Tess of the DUrbervilles': 7.6292, 'The Golden Bowl': 12.4424, 'The Secret Garden': 4.6525, 'Portrait of the Artist': 6.4493, 'The Black Moth': 4.2087, 'Orlando': 9.5421, 'Blood Meridian': 5.6345}
```

Part One 1.(d): see answer.txt


Result output: Part One 1.(e)(ii):
```
Serializing DataFrame to C:\Users\ClaudiaRoehn\Desktop\New folder\OneDrive - Home\0_NLP\nlp-coursework-2024-25-chrrr007\pickles\parsed.pickle
DataFrame saved as parsed.pickle
```


Result output: Part One 1.(e)(iii):
```
                                                text                  title   author  year                                             parsed
0  \nCHAPTER 1\n\nThe family of Dashwood had long...  Sense and Sensibility   Austen  1811  (\n, CHAPTER, 1, \n\n, The, family, of, Dashwo...
1  'Wooed and married and a'.'\n'Edith!' said Mar...        North and South  Gaskell  1855  (', Wooed, and, married, and, a, ', ., ', \n, ...
2  Book the First--Recalled to Life\n\n\n\n\nI. T...   A Tale of Two Cities  Dickens  1858  (Book, the, First, --, Recalled, to, Life, \n\...
3  SAMUEL BUTLER.\nAugust 7, 1901\n\nCHAPTER I: W...                Erewhon   Butler  1872  (SAMUEL, BUTLER, ., \n, August, 7, ,, 1901, \n...
4  THE AMERICAN\n\nby Henry James\n\n\n1877\n\n\n...           The American    James  1877  (THE, AMERICAN, \n\n, by, Henry, James, \n\n\n...

```

Result output: Part One 1.(e)(iv) spaCy:
```
TTR scores from loaded DataFrame:
{'Sense and Sensibility': 0.052847302442989776, 'North and South': 0.0549040694681204, 'A Tale of Two Cities': 0.07072694469399422, 'Erewhon': 0.09151270564132943, 'The American': 0.06381607058523676, 'Dorian Gray': 0.08355234620193412, 'Tess of the DUrbervilles': 0.07778957979554696, 'The Golden Bowl': 0.047475476259872806, 'The Secret Garden': 0.05847231570812455, 'Portrait of the Artist': 0.10472745625841184, 'The Black Moth': 0.07866588875923765, 'Orlando': 0.1137245917497168, 'Blood Meridian': 0.08568897067593587}

Flesch-Kincaid scores from loaded DataFrame:
{'Sense and Sensibility': 10.8894, 'North and South': 6.6553, 'A Tale of Two Cities': 9.843, 'Erewhon': 14.6793, 'The American': 7.9875, 'Dorian Gray': 4.9493, 'Tess of the DUrbervilles': 7.6292, 'The Golden Bowl': 12.4424, 'The Secret Garden': 4.6525, 'Portrait of the Artist': 6.4493, 'The Black Moth': 4.2087, 'Orlando': 9.5421, 'Blood Meridian': 5.6345}
```


Result output example: Part One 1.(f)(i):
```
syntactic_objects_counts:
Sense and Sensibility
[('punct', 20299), ('prep', 13332), ('pobj', 12073), ('nsubj', 11990), ('advmod', 8822), ('det', 8666), ('aux', 7436), ('dobj', 6325), ('poss', 4948), ('cc', 4712)]


North and South
[('punct', 36410), ('nsubj', 20761), ('prep', 18414), ('pobj', 16921), ('det', 13572), ('advmod', 12094), ('aux', 11384), ('dobj', 10180), ('ROOT', 9183), ('amod', 8242)]


A Tale of Two Cities
[('punct', 29933), ('prep', 15924), ('pobj', 15176), ('det', 13524), ('nsubj', 12858), ('dep', 12569), ('advmod', 7973), ('amod', 6957), ('dobj', 6883), ('ROOT', 6660)]


Erewhon
[('punct', 9488), ('prep', 9194), ('pobj', 8484), ('det', 7713), ('nsubj', 7628), ('advmod', 5578), ('aux', 4748), ('dobj', 4051), ('amod', 3879), ('conj', 3871)]


Result output example: Part One 1.(f)(ii):
```
subjects_by_verb_count:
Sense and Sensibility
[('I', 32), ('you', 19), ('she', 14), ('they', 6), ('Elinor', 6), ('he', 6), ('Jennings', 3), ('we', 2), ('Brandon', 1), ('both', 1)]


North and South
[('she', 59), ('I', 47), ('he', 23), ('you', 15), ('they', 13), ('Margaret', 10), ('we', 5), ('Thornton', 3), ('who', 3), ('yo', 2)]


A Tale of Two Cities
[('I', 23), ('he', 19), ('you', 12), ('she', 11), ('they', 5), ('Monseigneur', 2), ('one', 1), ('Jerry', 1), ('we', 1), ('mother', 1)]
```

Result output example: Part One 1.(f)(iii):
```
subjects_by_verb_pmi:
Sense and Sensibility
[('both', 1), ('Jennings', 3), ('you', 19), ('Brandon', 1), ('I', 32), ('Elinor', 6), ('they', 6), ('we', 2), ('she', 14), ('he', 6)]


North and South
[('yo', 2), ('she', 59), ('they', 13), ('I', 47), ('Margaret', 10), ('you', 15), ('we', 5), ('Thornton', 3), ('he', 23), ('who', 3)]


A Tale of Two Cities
[('mother', 1), ('Monseigneur', 2), ('she', 11), ('Jerry', 1), ('one', 1), ('you', 12), ('I', 23), ('he', 19), ('they', 5), ('we', 1)]
```


__PART TWO__

Record of data before and after applying changes to keep track:

Q 2(a): Dataset loaded and DF head output:
```
Dataset shape: (40000, 8)

Column names:
                                              speech         party               constituency        date speech_class      major_heading  year     speakername
0  Unemployment is soaring, uptake in benefits ha...        Labour           Portsmouth South  2020-09-14       Speech  Work and Pensions  2020  Stephen Morgan
1  I thank the hon. Gentleman for raising issues ...  Conservative                 Mid Sussex  2020-09-14       Speech  Work and Pensions  2020     Mims Davies
2  As my hon. Friend the Member for Portsmouth So...        Labour     Warwick and Leamington  2020-09-14       Speech  Work and Pensions  2020    Matt Western
3  I thank the hon. Gentleman for raising the nee...  Conservative                 Mid Sussex  2020-09-14       Speech  Work and Pensions  2020     Mims Davies
4  There is no doubt that the unemployment situat...        Labour  Ellesmere Port and Neston  2020-09-14       Speech  Work and Pensions  2020  Justin Madders
```

Q 2(a)(i):unique values BEFORE renaming:
```
Unique values in 'party' column:
party
Conservative                        25079
Labour                               6995
Scottish National Party              2303
Labour (Co-op)                       1043
Speaker                               878
Liberal Democrat                      803
Democratic Unionist Party             639
Independent                           243
Plaid Cymru                           173
Social Democratic & Labour Party       75
Alliance                               65
Green Party                            55
Alba Party                              2
Name: count, dtype: int64
```

AFTER renaming Labour (Co-op) to Labour:
```
Unique values in 'party' column:
party
Conservative                        25079
Labour                               8038
Scottish National Party              2303
Speaker                               878
Liberal Democrat                      803
Democratic Unionist Party             639
Independent                           243
Plaid Cymru                           173
Social Democratic & Labour Party       75
Alliance                               65
Green Party                            55
Alba Party                              2
Name: count, dtype: int64
```

Q 2(a)(ii):
Checked row number before/after removing all rows related to value "Speaker in party column:

Before removing 'Speaker' rows: 40000 rows
After removing 'Speaker' rows: 39122 rows
Conservative                        25079
Labour                               8038
Scottish National Party              2303
Liberal Democrat                      803
Democratic Unionist Party             639
Independent                           243
Plaid Cymru                           173
Social Democratic & Labour Party       75
Alliance                               65
Green Party                            55
Alba Party                              2

Check before removing all other than 4 top party's:
Before filtering to top 4 parties: 39122 rows
Top 4 most common parties: ['Conservative', 'Labour', 'Scottish National Party', 'Liberal Democrat']

After filtering to top 4 parties: 36223 rows
party
Conservative               25079
Labour                      8038
Scottish National Party     2303
Liberal Democrat             803

Q 2(a)(iii):
speech classes before removing rows:

speech_class
Speech        38457
Procedural     1394
Division        149

Q 2(a)(iv):
Before filtering by speech length: 36223 rows
Speeches < 1000 characters: 28139
After filtering to speeches >= 1000 characters: 8084 rows


Dataset shape: (40000, 8)
Dataset shape: (8084, 8)

```
Q.2(a)(iv) Final dataframe dimensions: (8084, 8)
```

Q 2(c):
REQUIRED PRINT:

``Random Forest Macro-Average F1 Score: 0.4547
Random Forest Classification Report:
                         precision    recall  f1-score   support

           Conservative       0.72      0.98      0.83       964
                 Labour       0.75      0.44      0.56       463
       Liberal Democrat       0.00      0.00      0.00        54
Scottish National Party       0.87      0.29      0.43       136

               accuracy                           0.73      1617
              macro avg       0.59      0.43      0.45      1617
           weighted avg       0.72      0.73      0.69      1617


SVM Macro-Average F1 Score: 0.5933
SVM Classification Report:
                         precision    recall  f1-score   support

           Conservative       0.83      0.92      0.87       964
                 Labour       0.74      0.71      0.72       463
       Liberal Democrat       1.00      0.07      0.14        54
Scottish National Party       0.78      0.54      0.64       136

               accuracy                           0.80      1617
              macro avg       0.84      0.56      0.59      1617
           weighted avg       0.81      0.80      0.79      1617
```
RF results:
Bias towards Cobnservatives: Predicts Conservative 98% of the time for actual Conservative speeches, which seems great but given the overwhelming amount of conservative speeches (dominace in the data) this is not surprising.
Completely fails Lib Dems: 0% precision, recall, F1 (class never predicted)
Poor performance on: 29% recall for Scottish National Party
Pretty unbalanced overall.

SVM outperforms RF:
Performance has better balance,and better performance on Lib Dem speeches.
Better predictions on Lib Dems (100%) but 7% recall means 93% of Liberal Democrat speeches wre missed, still low performanc. But no of Lib Dem speeches was low (54).  

Overall SVM better macro F1: 59.3% vs 45.5% - Far from impressiv


Q 2(d):
REQUIRED PRINT:

Overall SVM still better performance macro F1: 58.54% vs 47.93% - But whilst Rf improved slightly, SVM performance got worse with n_grams.

Required prints only:
```
Random Forest Macro-Average F1 Score: 0.4793
Random Forest Classification Report:
                         precision    recall  f1-score   support

           Conservative       0.74      0.96      0.83       964
                 Labour       0.75      0.48      0.58       463
       Liberal Democrat       0.00      0.00      0.00        54
Scottish National Party       0.84      0.35      0.50       136

               accuracy                           0.74      1617
              macro avg       0.58      0.45      0.48      1617
           weighted avg       0.72      0.74      0.71      1617


SVM Macro-Average F1 Score: 0.5854
SVM Classification Report:
                         precision    recall  f1-score   support

           Conservative       0.84      0.92      0.88       964
                 Labour       0.75      0.73      0.74       463
       Liberal Democrat       1.00      0.04      0.07        54
Scottish National Party       0.78      0.56      0.65       136

               accuracy                           0.81      1617
              macro avg       0.84      0.56      0.59      1617
           weighted avg       0.81      0.81      0.79      1617
```
RF results:  
Still completely fails on Liberal Democrats (0.00 across all metrics)
Poor recall other than for conservatives
SVM:      
Class imbalace in speechse seems to be a bottleneck, as before.
Poor recall other than for conservatives

Q 2(e):
REQUIRED PRINT:




Q.2(e) SVM Macro-Average F1 Score: 0.6762
Q.2(e) SVM Classification Report:
                         precision    recall  f1-score   support

           Conservative       0.84      0.93      0.88       964
                 Labour       0.78      0.71      0.74       463
       Liberal Democrat       0.92      0.22      0.36        54
Scottish National Party       0.83      0.64      0.72       136

               accuracy                           0.82      1617
              macro avg       0.84      0.63      0.68      1617
           weighted avg       0.82      0.82      0.81      1617

