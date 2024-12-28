# Aufgabenbearbeitung Dokumentation / Exercises for Task: 05

## Description of Data Fields in "lotr_characters.csv"

    birth: The birth date of the character. This is be a specific date or a time period (e.g., late Third Age).
    death: The death date of the character, if known. Some dates may be imprecise (e.g., "February 26" without a year).
    gender: The gender of the character, if available (Male, Female).
    hair: The hair color of the character, if known.
    height: The height of the character, if measured or described.
    name: The full name of the character.
    race: The race of the character (e.g., Men, Elves, Orcs, etc.).
    realm: The realm or place with which the character is associated.
    spouse: The name of the character's spouse, if married.

## Issues with Data Quality

While working with the "lotr_characters.csv" file, I encountered some issues related to data quality, such as incorrect character names. For instance, some names are improperly encoded, like "Ar-AdÃ»nakhÃ´r," which appears due to character encoding problems.
To address these issues, I took the following steps:

    Text Editor (Notepad++): I opened the CSV file in Notepad++ and re-encoded it to UTF-8 format to ensure proper character representation.
    Excel: I then imported the file into Excel using the "Get Data" feature to load it properly. The file was structured into tabs, including the data and the "data retrieval" process.
    Excel Formatting: This method allowed the columns and formats to be automatically detected, as seen in datasets like those from Kaggle.
    Whille working with the data i left many open data fields with no value in it to match it with the input file of kaggle where we have downloaded the content from.