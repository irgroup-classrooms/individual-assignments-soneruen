import re
import csv

# Define the input and output file names
input_file = r"C:\Users\Soner\OneDrive\DIS\WS24-25\DIS08\individual-assignments-soneruen\assignments\05\lotr_scripts.csv"  # Use raw string for Windows path
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

print("Cleaning complete! Cleaned data saved to", output_file)
