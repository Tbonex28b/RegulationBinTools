import subprocess
import os
import logging

# Set up logging
logging.basicConfig(
    filename='extraction_log.txt',  # Log file name
    level=logging.INFO,              # Log level
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log message format
)

def execute_dsmsportable(command):
    try:
        logging.info(f"Executing command: {command}")
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        logging.error(f'Error executing DSMSPortable: {e}')
        logging.error(f'Stdout: {e.stdout}')
        logging.error(f'Stderr: {e.stderr}')
        return None

def execute_second_script():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    second_script_path = os.path.join(script_directory, 'CSV Deleter.py')

    if os.path.exists(second_script_path):
        logging.info(f"Running second script: {second_script_path}")
        subprocess.run(['python', second_script_path], check=True)
    else:
        logging.error(f"Second script not found: {second_script_path}")

def get_gamepath():
    try:
        with open('gamepath.txt', 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

def set_gamepath(gamepath):
    with open('gamepath.txt', 'w') as file:
        file.write(gamepath)

def extract_modified_params(gamepath, param_name):
    # Create "Delete_Me" folder if it doesn't exist
    if not os.path.exists('Delete_Me'):
        os.makedirs('Delete_Me')

    csv_file_path = f'Delete_Me/{param_name}_modified_params.csv'

    # Full path to regulation.bin
    regulation_bin_path = r'C:\RegulationBinUtilities\regulation\regulation.bin'
    dsmsportable_command = f'C:\\RegulationBinUtilities\\DSMSPortable.exe "{regulation_bin_path}" -G ER -P "{gamepath}" -X {param_name} > "{csv_file_path}"'

    result = execute_dsmsportable(dsmsportable_command)

    if result:
        logging.info(f"Successfully extracted {param_name} to {csv_file_path}")
    else:
        logging.error(f"Failed to extract {param_name}. Check the output CSV at {csv_file_path}.")

def main():
    # Create "Delete_Me" folder if it doesn't exist
    if not os.path.exists('Delete_Me'):
        os.makedirs('Delete_Me')

    # Get the gamepath or prompt the user
    gamepath = get_gamepath()
    if gamepath is None:
        gamepath = input("Enter the gamepath: ")
        set_gamepath(gamepath)

    # Read param names from the param_names.txt file
    try:
        with open('param_names.txt', 'r') as param_file:
            param_names = [line.strip() for line in param_file if line.strip()]
    except FileNotFoundError:
        logging.error("Error: param_names.txt not found.")
        return

    # Iterate through each param_name
    for param_name in param_names:
        logging.info(f"Extracting param: {param_name}")

        # Extract modified params for the specified param name
        extract_modified_params(gamepath, param_name)

        # Check if the CSV file was created
        csv_file_path = f'Delete_Me/{param_name}_modified_params.csv'
        if os.path.exists(csv_file_path):
            logging.info(f"CSV file for {param_name} found at {csv_file_path}")
        else:
            logging.error(f"CSV file for {param_name} not found. Something went wrong.")

    # Execute the second script
    execute_second_script()

    # Keep the script open until user presses Enter
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()