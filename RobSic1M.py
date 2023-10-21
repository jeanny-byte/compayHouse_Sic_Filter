import os
import csv
from tqdm import tqdm

def search_and_append(input_file, output_file):
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Modify this section to perform your search for SIC codes or company names.
            # For example, you can check if the SIC code or company name is in 'row'.
            # If the row qualifies, write it to the output file.
            if 'your_search_condition' in row:
                with open(output_file, 'a', newline='') as output_file:
                    writer = csv.writer(output_file)
                    writer.writerow(row)

def main():
    folder_path = '/Results'  # Replace with the path to your folder
    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    output_file_name = 'Rob&Filtered_date.csv'

    # Create the output file if it doesn't exist
    if not os.path.exists(output_file_name):
        with open(output_file_name, 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            # Write a header row if needed
            # writer.writerow(['Header1', 'Header2', ...])

    # Create a progress bar for the file processing
    for csv_file in tqdm(csv_files, desc="Processing CSV files"):
        input_file_path = os.path.join(folder_path, csv_file)
        search_and_append(input_file_path, output_file_name)

if __name__ == "__main__":
    main()
