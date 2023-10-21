import os
import csv
from tqdm import tqdm

def extract_company_data(input_file):
    company_data = set()
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Extract the Company Name and Company Number from each row
            company_name = row[0]  # Assuming Company Name is in the first column (index 0)
            company_number = row[1]  # Assuming Company Number is in the second column (index 1)
            company_data.add(company_name)
            company_data.add(company_number)
    return company_data

def search_and_append(input_file, output_file, target_data):
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Check if either the Company Name or Company Number exists in the row
            if row[0] in target_data or row[1] in target_data:
                writer = csv.writer(output_file)  # Use the provided output_file object
                writer.writerow(row)

def main():
    folder_path = 'Results'  # Replace with the path to your folder
    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    output_file_name = 'Rob&Filtered_date.csv'
    
    # Extract Company Name and Company Number from the 1m_net.csv file
    target_data = extract_company_data('1m plus net assets contacts.csv')

    # Create the output file if it doesn't exist
    if not os.path.exists(output_file_name):
        with open(output_file_name, 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            # Write a header row if needed
            # writer.writerow(['Header1', 'Header2', ...])

    # Create a progress bar for the file processing
    for csv_file in tqdm(csv_files, desc="Processing CSV files"):
        input_file_path = os.path.join(folder_path, csv_file)
        with open(output_file_name, 'a', newline='') as output_file:
            search_and_append(input_file_path, output_file, target_data)

if __name__ == "__main__":
    main()
