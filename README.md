# FILE SCANNER

## Installation

  Install dependencies using pip:

  pip install pytest      # to run test file
  pip install termcolor   # to color text in terminal output

## Description:

  This program scans a file for a specific phrase, highlights matches in red in the terminal, and optionally saves the results to a JSON file.

  By default, it searches the file auth.log for the phrase "fail", but both the file and phrase can be customized through command-line arguments.

  Usage:
  python file_scanner.py -f <filename> -s <phrase> 

### Arguments:

  It takes two optional arguments on the command line:
  -f - input file name (default "auth.log")
  -s - search phrase to look for in the file, case-insensitive (default "fail")

### Functions:

  The program contains five functions plus main:
  * main(): - reads command-line arguments, if no arguments are given, the program runs with default values. Program validates the file extension, scans the file for the phrase, prints matches with line numbers and highlights the phrase in red. Asks if the user wants to save results. If yes, prompts for a valid filename (must have allowed extension) and saves as JSON.

  * file_extension_check(file): - validates the file extension against the allowed list: "log", "txt", "csv", "json", "md", raises ValueError if the extension is invalid.

  * file_scanner(file, phrase): - Scans the file for the phrase (case-insensitive). Prints line numbers and lines containing the phrase, with matches highlighted in red.

  * contains_phrase(line, phrase): - checks if the given phrase (case-insensitive) appears in the given line.

  * save_found(found, input_file): - saves pairs of {line_number : line} to the JSON file.

  * highlights(line, phrase): - highlights all occurrences of the given phrase in red.

## "Auth.log", "authentication_failure.json" and "test.json" files

  These are supplemental files.

### "Auth.log"

  Sample log file for testing searches (contains phrases like "wbcLogonUser failed" and "authentication failure").

### "Authentication_failure.json"

  Example output when running the program with -s "authentication failure"

### "Test.json"

  Created when running pytest test_file_scanner.py to verify the save_found() function

# TEST FILE "test_file_scanner.py"

  This file tests functions from file_scanner.py. It contains five test functions:

  * test_file_extension_check() - validates extension checking.
  * test_file_scanner() - verifies correct detection of phrases.
  * test_contains_phrase() - checks phrase matching logic.
  * test_save_found() - ensures results are correctly saved to JSON.
  * test_highlights() - tests red highlighting of phrases.
