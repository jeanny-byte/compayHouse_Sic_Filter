import pandas as pd
from tqdm import tqdm  # Import tqdm for progress bar

# Create a dictionary mapping SIC codes to human-readable names
sic_code_to_name = {
    91009900: "Farming and Fishing",
    10110101: "Agriculture",
    20101301: "Fisheries",
    # Add more SIC codes and names as needed
}

# Modify the main_target_numbers to use SIC codes
main_target_numbers = list(sic_code_to_name.keys())

def process_csv(file_path, target_numbers, chunk_size=1000):
    """
    Process a CSV file, filter rows based on target numbers, and save the filtered data.

    Parameters:
        file_path (str): The path to the CSV file.
        target_numbers (list): List of target numbers (SIC codes) to filter rows.
        chunk_size (int, optional): The chunk size for reading the CSV file. Defaults to 1000.

    Returns:
        None
    """
    # Create a dictionary to store data for each target number
    target_data = {number: [] for number in target_numbers}
    processed_rows = 0  # Initialize a counter for processed rows

    # Calculate the total number of rows in the CSV file
    total_rows = sum(1 for _ in open(file_path))

    # Create a tqdm progress bar
    progress_bar = tqdm(total=total_rows, unit=" rows")

    # Read the CSV file in chunks and process each chunk
    for chunk in pd.read_csv(file_path, chunksize=chunk_size):
        for _, row in chunk.iterrows():
            for col in ['SICCode.SicText_1', 'SICCode.SicText_2', 'SICCode.SicText_3', 'SICCode.SicText_4']:
                sic_code_str = str(row[col]).split('-')[0].strip()
                try:
                    sic_code = int(sic_code_str)
                    if sic_code in target_numbers:
                        target_data[sic_code].append(row)
                except ValueError:
                    pass
            processed_rows += 1
            progress_bar.update(1)  # Update the progress bar

    # Close the progress bar
    progress_bar.close()

    # Save the filtered data using SIC codes in the filename
    save_filtered_data(target_data, sic_code_to_name)


def save_filtered_data(target_data, sic_code_to_name):
    """
    Save the filtered data to separate CSV files with SIC codes in the filename.

    Parameters:
        target_data (dict): Dictionary containing the filtered data for each target number.
        sic_code_to_name (dict): Dictionary mapping SIC codes to human-readable names.

    Returns:
        None
    """
    for sic_code, rows in target_data.items():
        if len(target_data) == 1:
            # If only one SIC code was used, save the file as SIC_Code_Human-Readable-Name.csv
            name = sic_code_to_name.get(sic_code, f"SIC_Code_{sic_code}")
            filename = f"{sic_code}_{name}.csv"
        else:
            # If multiple SIC codes were used, save the file with a common name
            name = "Filtered_Worksheet.csv"
            filename = name
        df = pd.DataFrame(rows)
        df.to_csv(filename, index=False)
        print(f"Saved filtered data for target: {name} in {filename}")


if __name__ == "__main__":
    # The actual path to CSV file
    csv_file_path = 'BasicCompanyDataAsOneFile-2023-10-04.csv'

    process_csv(csv_file_path, main_target_numbers, chunk_size=1000)
