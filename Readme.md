# Japanese Linguistics (LIN 520) - Final Project


## Project Outline:
- Independent research project in Japanese Linguistics.
- I have decided to combine my interests in video games and programming for this project, by writing this program to analyze the scripts of the video games in the Persona series.
    - Persona is developed by the video game company Atlus, based in Tokyo Japan.


## Notes:
- Using fugashi, a Cython wrapper for the Japanese tokenizer MeCab.
    - GIT: https://github.com/polm/fugashi


## MVP:
- Read in lines from the scripts for Persona 4 and Persona 5.
- Parse out individual words, and tokenize them.
- Tally the occurance of each token within each game's script.
- Writes data to csv files for comparison.
    - Word occurrences in each game.
    - Lemma occurrences in each game.
    - Occurrence Comparison, based on Persona 4
    - Occurrence Comparison, based on Persona 5


## Changelog

### 20240326
1) Initializing repository.
2) Currently still "playing" with the data. I am unsure of what sorts of insights I might glean.


### 20240408
1) After spending some time messing around with Fugashi and acquiring a better understanding of how it works, I've determined that none of my "fixup" code was necessary.
    - Instead, I am using Fugashi's built-in POS categorization to complete this operation.
2) Refactored the code to separate Persona 4 script operations from Persona 5 script operations.

**NOTE:** I may have to abandon my goal of determining the occurrences of repeated phrases in each game.


### 20240409
1) Refactored code to use methods where code was being repeated for different operations.
2) Created a method to determine occurrences by *LEMMA*, rather than by *WORD*.
3) Created a method to translate the POS provided by Fugashi into English.
4) Created method to facilitate comparison of lists.
    - Some quirk about how Python methods are instantiated has been resulting in erroneous errors in the data handling.
    - Removed method, and separated operations into individual for loops as a workaround.
    - **NOTE:** Didn't work. Will troubleshoot tomorrow.

### 20240410
1) I'm still struggling with the comparisons, so I'm attempting a completely different approach using the BubbleSort method I've already written.
    - Success! **MVP COMPLETE** *celebration noises*
2) Used data from CSV files to create .xlsx files.
3) Refactored project, for organization.
4) Created occurrence lists for *POS*.
    - Considerations:
        - Do I want to incorporate the necessary code into current parsing function?
            - ~~Yes? I'm trying it.~~
            - Tried it, but it's going to be easier to just create a new Python file for this secondary proceedure.
    - Complete
5) Created comparison lists, based on *POS*.
6) Separated the different list creations out into separate Python programs, and moved by BubbleSort method into a separate file containing only a "Global Methods" class.
7) Refactored program to use separate applications.
    - Operated through a "shell" terminal application.
8) Added a small module to determine total word count for each game.

### 20240411
1) Updated *BuildTotalWorldCounts.py* to output the wordcount datasets both including and excluding the total count of particles.


## Citations
- Atlus. “Persona 4.” Atlus., 2008.
- Atlus. “Persona 5.” Atlus., 2016.
- McCann, Paul. Fugashi, 2020, https://pypi.org/project/fugashi/. Accessed 2024.
- McCann, Paul. “Fugashi, a tool for tokenizing Japanese in python.” Proceedings of Second Workshop for NLP Open Source Software (NLP-OSS), 2020, https://doi.org/10.18653/v1/2020.nlposs-1.7.