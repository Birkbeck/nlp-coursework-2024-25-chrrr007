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
I decided to create a new "test.py" document to develop my code to start from a blank page aand copy the provided starter code snippets in order as needed. This appeared cleaner and allowed me to keep the starter code and cleary mark developed parts as done. The commit history will show on the test.py, rather than on the PartOne.py. Once all code is developed I am planning on renaming the test.py to PartOne.py



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


Result output: Part One 1.(d):
```
Flesch_Kincaide_scores:
{'Sense and Sensibility': 10.8894, 'North and South': 6.6553, 'A Tale of Two Cities': 9.843, 'Erewhon': 14.6793, 'The American': 7.9875, 'Dorian Gray': 4.9493, 'Tess of the DUrbervilles': 7.6292, 'The Golden Bowl': 12.4424, 'The Secret Garden': 4.6525, 'Portrait of the Artist': 6.4493, 'The Black Moth': 4.2087, 'Orlando': 9.5421, 'Blood Meridian': 5.6345}
```

Result output: Part One 1.(e)(ii):
```
About to start serialization...
Creating directory...
Serializing DataFrame to C:\Users\ClaudiaRoehn\Desktop\New folder\OneDrive - Home\0_NLP\nlp-coursework-2024-25-chrrr007\pickles\parsed.pickle

DataFrame saved as parsed.pickle

Function ending...
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