import sys
import argparse
import re
import json
from termcolor import colored

def main():
    parser = argparse.ArgumentParser(description="Finds lines that contain specified phrase in a file, optionally saves results to JSON file")

    parser.add_argument("-f", default="auth.log", help="input file")
    parser.add_argument("-s", default="fail", help="search phrase")

    args = parser.parse_args()

    input_file = args.f
    file_extension_check(input_file)
    search_phrase = args.s.lower()

    found = file_scanner(input_file,search_phrase)
    #print(found)

    if (input("Would you like to save this information to the JSON file? (yes/no): ").lower()) == "yes":
        f = True
        while f:
            output_file = input("File name: ")
            if output_file.lower().endswith("json"):
                f = False
            else:
                print("Not a JSON file")
        save_found(found,output_file)
    else:
        sys.exit("Bye!")

# checks if file given on command line is of specific extension
def file_extension_check(file):
    extensions = ("log", "txt", "csv", "json","md")
    if  not file.lower().endswith(extensions):
        raise ValueError("File format not supported. \nTry: .log, .txt, .scv, .json or .md files.")
    else:
        return


# scans lines in spacific file for specific phrase ( both given at command line)
def file_scanner(file,phrase):
    logs = []
    try:
        with open (file, "r") as file:
            for line_number, line in enumerate(file, start=1):
                if contains_phrase(line,phrase):
                    print(line_number,highlights(line, phrase),end="")
                    logs.append({line_number:line.strip()})
        return logs
    except FileNotFoundError:
        sys.exit("File not found.")


# checks if line contains phrase
def contains_phrase(line,phrase):
    if re.search(f".*{phrase}.*",line,re.IGNORECASE):
        return True
    else:
        return False


# saves found information to JSON file
def save_found(found,output_file):
    try:
        with open(output_file, "w") as file:
            json.dump(found, file,indent=4)
            print("Saved!")
    except Exception:
        sys.exit("Error")


# highlights phrase case insensitive
def highlights(line, phrase):
    pattern = re.compile(re.escape(phrase),re.IGNORECASE)
    return pattern.sub(lambda c: colored(c.group(0),"red"), line)



if __name__ == "__main__":
    main()
