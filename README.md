# Number Format Project

## Overview
The Number Format project is designed to normalize and format phone numbers according to specific rules. It provides functionality to validate phone numbers and process them from a CSV file, ensuring that they adhere to the Australian phone number format.

## Features
- Normalize phone numbers from various formats to a standard format.
- Validate phone numbers to ensure they meet specific criteria.
- Process phone numbers from a CSV file and output the results to a new CSV file.

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd Number Format
   ```
3. Install the required dependencies (if any):
   ```
   pip install pandas
   ```

## Usage
To use the script, run the following command in your terminal:
```
python format_number.py [input_file] [output_file]
```
- `input_file`: The path to the CSV file containing names and phone numbers.
- `output_file`: The path where the formatted output CSV file will be saved.

### Example
```
python format_number.py Name_Phone_Address.csv Final_Name_Phone.csv
```

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.