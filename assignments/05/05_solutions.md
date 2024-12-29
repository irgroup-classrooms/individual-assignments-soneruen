# 05_solutions, soneruen

## Overview
This document outlines the steps taken to clean and analyze the `lotr_scripts.csv` dataset, we had to download from kaggle for the lab assignment 05.
I also uploaded the following files into this repository (05):
- `05_data_set_cleaner.py` which is my code for cleaning the csv
- `cleaned_lotr_scripts.csv`, as an example when using the code
- `lotr_scripts.csv`, the "dirty" data set, just as a reference

## Data Fields Description

- **char**: The character who is speaking the dialogue.
- **dialog**: The actual spoken words or dialogue of the character.
- **movie**: The title of the movie from which the dialogue is taken.

## Data Cleaning Steps (05_dataset_cleaner.py): Using Python with Regex including documentation for the dirty datafields of the csv in the code block
```python
import re
import csv
# Define the input and output file names
input_file = r"C:\Users\Soner\OneDrive\DIS\WS24-25\DIS08\individual-assignments-soneruen\assignments\05\lotr_scripts.csv"  # Use raw string for my Windows path
output_file = r"C:\Users\Soner\OneDrive\DIS\WS24-25\DIS08\individual-assignments-soneruen\assignments\05\cleaned_lotr_scripts.csv"  # Output path for cleaned data

# Open the input CSV file for reading
with open(input_file, 'r', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    cleaned_rows = []

    for row in reader:
        cleaned_row = []
        for cell in row:
            # Apply regex transformations
            
            # Remove extra commas
            cell = re.sub(r',,', ',', cell)
            
            # Replace multiple consecutive commas with a single comma
            cell = re.sub(r',,{2,}', ',', cell)  # New line added here
            
            # Trim leading and trailing whitespace
            cell = cell.strip()
            
            # Remove leading commas
            cell = re.sub(r'^,+', '', cell)
            
            # Collapse multiple spaces into a single space
            cell = re.sub(r'\s+', ' ', cell)
            
            # Remove space before commas
            cell = re.sub(r'\s+,', ',', cell)
            
            # Standardize quotation marks (optional)
            cell = re.sub(r"[‘’]", '"', cell)  # Replace smart quotes with double quotes
            

            cleaned_row.append(cell)
        cleaned_rows.append(cleaned_row)

# Write the cleaned data to a new CSV file
with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(cleaned_rows)

print("Cleaning complete! Cleaned data saved to", output_file) # Cleaned dataset appears, and gives the feedback!
```

# Analysis of LOTR Scripts Dataset
This document outlines the commands used to analyze the LOTR scripts dataset. The analysis includes counting lines, unique words, film distribution, and identifying top characters.

## 1. Total Number of Lines and Unique Words
To find the total number of lines and unique words used in dialogs:
```bash
# Count total number of lines
total_lines=$(wc -l < "C:\Users\Soner\OneDrive\DIS\WS24-25\DIS08\individual-assignments-soneruen\assignments\05\cleaned_lotr_scripts.csv")
echo "Total number of lines: $total_lines"
```

```bash
# Extract dialog column, split into words, sort, and count unique words
unique_words=$(cut -d ',' -f3 "C:\Users\Soner\OneDrive\DIS\WS24-25\DIS08\individual-assignments-soneruen\assignments\05\cleaned_lotr_scripts.csv" | tr ' ' '\n' | tr -d '[:punct:]' | sort | uniq | wc -l)
echo "Total number of unique words: $unique_words"
```

## 2. Distribution across films.
```bash
# Count distribution of movies (assuming it's the fourth column)
cut -d ',' -f4 "C:\Users\Soner\OneDrive\DIS\WS24-25\DIS08\individual-assignments-soneruen\assignments\05\cleaned_lotr_scripts.csv" | sort | uniq -c
```

## 3. Top 5 characters in the dataset.
```bash
# Find top 5 characters in the 'char' column 
cut -d ',' -f2 "C:\Users\Soner\OneDrive\DIS\WS24-25\DIS08\individual-assignments-soneruen\assignments\05\cleaned_lotr_scripts.csv" | sort | uniq -c | sort -nr | head -n 5
```

## 4. Top 5 chracter names in the dialogues
```bash
# Extract top 5 character names in the dialogues
cut -d ',' -f3 "C:\Users\Soner\OneDrive\DIS\WS24-25\DIS08\individual-assignments-soneruen\assignments\05\cleaned_lotr_scripts.csv" | tr ' ' '\n' | grep -Eo '[A-Z][a-z]+' | sort | uniq -c | sort -nr | head -n 5
```


