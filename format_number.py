import pandas as pd
import re
import sys
import os

def normalize_phone_number(phone):
    # Handle non-string or missing values
    if pd.isna(phone) or not isinstance(phone, (str, int, float)):
        return "Invalid"
    
    # Convert to string and remove non-digit characters except +
    phone = str(phone).strip()
    phone = re.sub(r'[^0-9+]', '', phone)
    
    # Skip empty or non-numeric entries
    if not phone or phone == 'nan':
        return "Invalid"
    
    # Standardize phone number formats
    if phone.startswith("+610"):
        phone = "+61" + phone[4:]  # +610xxxxxxxxx → +61xxxxxxxxx
    elif phone.startswith("+61") and len(phone) == 12:
        pass  # Already correct: +61xxxxxxxxx
    elif phone.startswith("0") and len(phone) == 10:
        phone = "+61" + phone[1:]  # 0xxxxxxxxx → +61xxxxxxxxx
    elif phone.startswith("61") and len(phone) == 11:
        phone = "+" + phone  # 61xxxxxxxxx → +61xxxxxxxxx
    elif phone.isdigit() and len(phone) == 9:
        phone = "+61" + phone  # xxxxxxxxx → +61xxxxxxxxx
    else:
        return "Invalid"
    
    # Validate: must be +61 followed by 9 digits
    if re.match(r'^\+61\d{9}$', phone):
        return phone
    return "Invalid"

def process_phone_numbers(input_file, output_file):
    # Verify input file exists
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file '{input_file}' does not exist")
    
    # Read CSV file
    try:
        df = pd.read_csv(input_file, dtype=str, encoding='utf-8-sig')
    except Exception as e:
        raise ValueError(f"Failed to read CSV file: {e}")
    
    # Check for required columns
    if not {"Name", "Phone"}.issubset(df.columns):
        raise ValueError("CSV file must contain 'name' and 'phoneno' columns")
    
    # Rename columns for output
    df = df[["Name", "Phone"]].rename(columns={"Name": "Name", "Phone": "Mobile Number"})
    
    # Format phone numbers
    df["Mobile Number"] = df["Mobile Number"].apply(normalize_phone_number)
    
    # Write to output CSV
    try:
        df.to_csv(output_file, index=False, encoding='utf-8-sig')
        print(f"Formatted Name and Phone numbers saved to '{output_file}'")
    except Exception as e:
        raise ValueError(f"Failed to write output CSV: {e}")

def main():
    # Default paths in /Users/manishkafle/Developer/GitHub/Python Scripts
    default_dir = "/Users/manishkafle/Developer/GitHub/Python Scripts/Number Format"
    default_input = os.path.join(default_dir, "Name_Phone_Address.csv")
    default_output = os.path.join(default_dir, "Final_Name_Phone.csv")
    
    # Use command-line arguments if provided, else defaults
    input_file = sys.argv[1] if len(sys.argv) > 1 else default_input
    output_file = sys.argv[2] if len(sys.argv) > 2 else default_output
    
    try:
        process_phone_numbers(input_file, output_file)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()