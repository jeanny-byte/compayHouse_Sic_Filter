import os
import pandas as pd

# Get a list of all CSV files in the current directory
csv_files = [file for file in os.listdir() if file.endswith(".csv")]

# Create a dictionary to store combined data for files with the same name
combined_data = {}

# Loop through the CSV files
for file in csv_files:
    file_name = os.path.splitext(file)[0]  # Extract the base file name without extension

    # Read the CSV data
    df = pd.read_csv(file)

    # Check if the file name is already a key in the dictionary
    if file_name in combined_data:
        combined_data[file_name] = combined_data[file_name].append(df, ignore_index=True)
    else:
        combined_data[file_name] = df

# Save combined data for each group of files with the same name
for file_name, df in combined_data.items():
    combined_file_name = f"{file_name}_combined.csv"
    df.to_csv(combined_file_name, index=False)
    print(f"Combined data for {file_name} saved to {combined_file_name}")
