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
    - Words organized by parts of speech
    - Occurrence Comparison, based on Persona 4
    - Occurrence Comparison, based on Persona 5
    - Recurring phrases


## Changelog

### 20240326
1) Initializing repository.
2) Currently still "playing" with the data. I am unsure of what sorts of insights I might gleam.


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
1) I'm still struggling with the comparisons, so I',m going to attempt a completely different approach.