import csv

# Define the input and output file paths
input_file = 'RobSIC.csv'
output_file = 'output.txt'

# Initialize a dictionary to store the data
data = {}

# Read the CSV file and populate the dictionary
with open(input_file, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if len(row) >= 2:
            industry_code = row[0]
            description = row[1]
            
            # Check if the industry code is a number
            if industry_code.isdigit():
                data[industry_code] = description

# Generate the output in the specified format
output = ""
for code, description in data.items():
    output += f'{code} : "{description}",\n'

# Write the output to a text file
with open(output_file, 'w') as textfile:
    textfile.write(output)

print("Script completed successfully. Output saved to", output_file)
