import pandas as pd


def process_csv(file_path, target_numbers, chunk_size=1000):
    """
    Process a CSV file, filter rows based on target numbers, and save the filtered data.

    Parameters:
        file_path (str): The path to the CSV file.
        target_numbers (list): List of target numbers to filter rows.
        chunk_size (int, optional): The chunk size for reading the CSV file. Defaults to 1000.

    Returns:
        None
    """
    # Create a dictionary to store data for each target number
    target_data = {number: [] for number in target_numbers}
    processed_rows = 0  # Initialize a counter for processed rows

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

            # Print progress report every 1000 rows (adjust as needed)
            if processed_rows % 1000 == 0:
                print(f"Processed {processed_rows} rows...")

    # Save the filtered data
    save_filtered_data(target_data)


def save_filtered_data(target_data):
    """
    Save the filtered data to separate CSV files for each target number.

    Parameters:
        target_data (dict): Dictionary containing the filtered data for each target number.

    Returns:
        None
    """
    for number, rows in target_data.items():
        df = pd.DataFrame(rows)
        df.to_csv(f'{number}_worksheet.csv', index=False)
        print(f"Saved filtered data for target number: {number}")


if __name__ == "__main__":
    # The actual path to CSV file
    csv_file_path = 'BasicCompanyData-2023-10-04-part6_7.csv'

    # List of target numbers
    main_target_numbers = [91009900, 10110101, 20101301, 2001031, 103201, 103901, 104101, 104201, 10511, 10512, 10519, 10520, 10611, 10612, 10620, 10710, 10720, 10730, 10810, 10821, 110822, 110831, 110832, 110840, 110850, 110860, 110890, 110910, 110920, 111010, 111020, 111030, 111040, 111050, 111060, 111070, 120001, 31001, 32001, 33001, 39101, 39211, 39221, 39231, 39311, 39391, 39401, 39501, 39601, 39901, 41101, 41201, 41310, 41320, 41410, 41420, 41901, 42001, 43101, 43901, 51101, 51201, 52001, 61001, 62101, 62201, 62301, 62401, 62901, 71101, 71201, 72111, 72191, 72200, 72300, 72400, 72901, 81101, 81211, 81291, 81301, 81401, 82011, 82021, 82031, 91001, 92001, 9209, 20110, 20120, 20130, 20140, 20150, 20160, 20170, 20200, 20301, 20302, 20411, 20412, 20420, 20510, 20520, 20530, 20590, 20600, 21100, 21200, 22110, 22190, 22210, 22220, 22230, 22290, 23110, 23120, 23130, 23140, 23190, 23200, 23310, 23320, 23410, 23420, 23430, 23440, 23490, 23510]

    process_csv(csv_file_path, main_target_numbers, chunk_size=1000)
