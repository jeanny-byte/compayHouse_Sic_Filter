# CSV File Processing Script

This Python script is designed to process a CSV file, filter rows based on specific target numbers (SIC codes), and save the filtered data to separate CSV files. The script also provides the option to save the CSV output files using the SIC code and description in the filename.

## Features

- Filters rows in a CSV file based on target SIC codes.
- Saves the filtered data to separate CSV files.
- Supports appending new data to existing files if a file with the same name already exists.
- Handles low memory situations when working with large CSV files.

## Requirements

To run this script, you'll need the following dependencies:

- Python 3.x
- Pandas (for data manipulation)
- tqdm (for progress bars)

You can install these dependencies using pip with the following commands:

```bash
pip install pandas
pip install tqdm

Usage
Place the script in the same directory as the CSV file you want to process.
Modify the sic_code_to_name dictionary to specify the SIC codes and their human-readable names.
Set the main_target_numbers variable to the list of target SIC codes you want to filter.
Run the script using the following command:
bash
Copy code
python your_script_name.py
The script will process the CSV file, filter rows based on the specified SIC codes, and save the filtered data to separate CSV files in a "Results" folder.

Configuration
You can adjust the chunk_size parameter in the process_csv function to control the chunk size when reading the CSV file.
The script is set up to handle low memory situations when concatenating data from existing files. You can modify the chunk size in the pd.read_csv function to further control memory usage.
License
This script is provided under the MIT License.

Contact
For any questions or feedback, feel free to contact [Jean-Claude] at [Jeanclaude17052000@gmail.com].

Enjoy using the script!
