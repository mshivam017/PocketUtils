import zipfile
import os
import argparse
import sys

def extract_zip(zip_path, extract_to=None, password=None):
    """
    Extracts a zip file to a specified directory.

    Args:
        zip_path (str): The path to the zip file.
        extract_to (str): The directory to extract to. Defaults to a folder named after the zip file.
        password (str): Optional password for encrypted zip files.
    """
    # 1. Validate if the zip file exists
    if not os.path.exists(zip_path):
        print(f"Error: The file '{zip_path}' does not exist.")
        return

    # 2. Validate if it is actually a zip file
    if not zipfile.is_zipfile(zip_path):
        print(f"Error: The file '{zip_path}' is not a valid zip file.")
        return

    # 3. Determine the extraction directory
    if extract_to is None:
        # Default to a folder named after the zip file (without extension) in the same directory
        base_name = os.path.splitext(os.path.basename(zip_path))[0]
        extract_to = os.path.join(os.path.dirname(zip_path), base_name)

    # Create the directory if it doesn't exist
    if not os.path.exists(extract_to):
        try:
            os.makedirs(extract_to)
            print(f"Created directory: {extract_to}")
        except OSError as e:
            print(f"Error creating directory '{extract_to}': {e}")
            return

    # 4. Attempt extraction
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # Handle password if provided
            if password:
                # set_password expects bytes
                zip_ref.setpassword(password.encode('utf-8'))
            
            print(f"Extracting '{zip_path}' to '{extract_to}'...")
            
            # Extract all files
            zip_ref.extractall(extract_to)
            
            print("Extraction complete successfully!")
            
            # List extracted files (optional)
            print("\nExtracted files:")
            for file_name in zip_ref.namelist():
                print(f" - {file_name}")

    except RuntimeError as e:
        if 'Bad password' in str(e):
             print("Error: Incorrect password provided for encrypted zip file.")
        else:
            print(f"Runtime Error during extraction: {e}")
    except zipfile.BadZipFile:
        print("Error: The file is a bad or corrupted zip file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    # Set up argument parser for command line usage
    parser = argparse.ArgumentParser(description="Extract contents of a ZIP file.")
    
    # nargs='?' makes the argument optional
    parser.add_argument("zip_file", nargs='?', help="Path to the ZIP file. If omitted, searches for a .zip in current dir.")
    parser.add_argument("-o", "--output", help="Directory to extract files to (optional)")
    parser.add_argument("-p", "--password", help="Password for encrypted ZIP files (optional)")

    args = parser.parse_args()
    
    target_zip = args.zip_file

    # If no zip file provided, look in the current directory
    if target_zip is None:
        print("No ZIP file specified. Searching current directory...")
        # List all files ending with .zip (case insensitive)
        zip_files = [f for f in os.listdir('.') if f.lower().endswith('.zip')]
        
        if len(zip_files) == 1:
            target_zip = zip_files[0]
            print(f"Found one ZIP file: '{target_zip}'")
        else:
            if not zip_files:
                print("No ZIP files found in the current directory.")
            else:
                print("Multiple ZIP files found:")
                for z in zip_files:
                    print(f" - {z}")
            
            # Ask user for input if auto-detection failed or was ambiguous
            target_zip = input("Please enter the zip file name: ").strip()
            if not target_zip:
                print("No file entered. Exiting.")
                return

    # call the extraction function
    extract_zip(target_zip, args.output, args.password)

if __name__ == "__main__":
    main()