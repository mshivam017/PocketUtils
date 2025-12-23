import zipfile
import os

def extract_zip(zip_file, extract_to):
    try:
        # Ensure the output directory exists
        os.makedirs(extract_to, exist_ok=True)

        # Open the zip file in read mode
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            # Extract all contents to the target directory
            zip_ref.extractall(extract_to)

        print(f"Successfully extracted {zip_file} to {extract_to}")
    except Exception as e:
        print(f"Error extracting {zip_file}: {str(e)}")

# Example usage
zip_file = 'simple-search-engine-master.zip'  # Replace with your zip file path
extract_to = '/home/runner/WhirlwindPeruMarketing'  # Replace with the directory where you want to extract files

extract_zip(zip_file, extract_to)
# print("\nCurrent Working Directory:", os.getcwd(),)