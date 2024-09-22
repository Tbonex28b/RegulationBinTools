import subprocess
import os
import shutil
import logging

# Set up logging
logging.basicConfig(
    filename='extraction_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def execute_command(command):
    try:
        logging.info(f"Executing command: {command}")
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        logging.info(f"Command output: {result.stdout}")
        return result.stdout
    except subprocess.CalledProcessError as e:
        logging.error(f'Error executing command: {e}')
        logging.error(f'Stdout: {e.stdout}')
        logging.error(f'Stderr: {e.stderr}')
        return None

def get_gamepath():
    try:
        with open('gamepath.txt', 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

def set_gamepath(gamepath):
    with open('gamepath.txt', 'w') as file:
        file.write(gamepath)

def move_csv_to_folder(csv_file_path, csv_files_folder, final_name):
    try:
        destination_path = os.path.join(csv_files_folder, final_name)
        logging.info(f"Moving {csv_file_path} to {destination_path}")
        shutil.move(csv_file_path, destination_path)
        logging.info(f"Moved {csv_file_path} to {destination_path}")
    except Exception as e:
        logging.error(f"Error moving file {csv_file_path} to {csv_files_folder}: {e}")

def extract_and_move_param(gamepath, param_name, delete_me_folder, csv_files_folder):
    # Full path to regulation.bin
    regulation_bin_path = 'C:\\Path\\To\\DSMSPortable\\regulation\\regulation.bin'
    clean_param_name = param_name.split(':')[0]
    # Adjust to use the correct expected output filenames
    if ':' in param_name:
        temp_file_name = f'{clean_param_name}.csv'  # Use normal name for modified params
    else:
        temp_file_name = f'{clean_param_name}_modified_params.csv'  # Keep this for non-modified ones

    csv_file_path_in_delete_me = os.path.join(delete_me_folder, temp_file_name)

    # Command execution remains the same
    dsmsportable_command = (
        f'C:\\Path\\To\\DSMSPortable.exe "{regulation_bin_path}" '
        f'-G ER -P "{gamepath}" -X {param_name}'
    )

    if execute_command(dsmsportable_command):
        # Check for both output file possibilities
        regulation_folder = r'C:\Path\To\DSMSPortable\regulation'  # Adjust this as needed
        extracted_csv_path = os.path.join(regulation_folder, temp_file_name)

        if os.path.exists(extracted_csv_path):
            final_csv_name = f'{clean_param_name}.csv'
            move_csv_to_folder(extracted_csv_path, csv_files_folder, final_csv_name)
        else:
            logging.error(f"Extracted CSV file not found: {extracted_csv_path}")
    else:
        logging.error(f"Failed to extract {param_name}. Check output CSV at {csv_file_path_in_delete_me}.")

def main():
    delete_me_folder = r'Delete_Me'
    csv_files_folder = r'csv_files'

    # Create the Delete_Me folder if it doesn't exist
    if not os.path.exists(delete_me_folder):
        os.makedirs(delete_me_folder)

    # Create the csv_files folder if it doesn't exist
    if not os.path.exists(csv_files_folder):
        os.makedirs(csv_files_folder)

    gamepath = get_gamepath()
    if gamepath is None:
        gamepath = input("Enter the gamepath: ")
        set_gamepath(gamepath)

    # Fallback: Define default params if param_names.txt is not available
    try:
        with open('param_names.txt', 'r') as param_file:
            param_names = [line.strip() for line in param_file if line.strip()]
    except FileNotFoundError:
        logging.error("Error: param_names.txt not found. Using fallback parameters.")
        param_names = ['Bullet:modified', 'AtkParam_PC:modified']  # Default parameters

    for param_name in param_names:
        logging.info(f"Extracting param: {param_name}")
        extract_and_move_param(gamepath, param_name, delete_me_folder, csv_files_folder)

    # Cleanup
    if os.path.exists(delete_me_folder):
        shutil.rmtree(delete_me_folder)
        logging.info(f"Deleted the temporary folder: {delete_me_folder}")

    logging.info('CSV extraction and final movement completed.')
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
