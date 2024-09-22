import subprocess
import os
import time

def execute_dsmsportable(command, log_file):
    try:
        print(f"Executing command: {command}")
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        log_file.write(f"Success: {command}\n")
        log_file.write(result.stdout + "\n")  # Log stdout
        log_file.write(result.stderr + "\n")  # Log stderr
    except subprocess.CalledProcessError as e:
        log_file.write(f'Error executing dsmsportable: {e}\n')
        log_file.write(f'Stdout: {e.stdout}\n')
        log_file.write(f'Stderr: {e.stderr}\n')
    time.sleep(1)  # Add a delay of 1 second between commands

def main():
    # Example paths (replace with your actual paths)
    dsmsportable_path = 'C:\\Path\\To\\DSMSPortable.exe'   # Example: C:\DSMSPortablev1.8.5\DSMSPortable.exe
    game_path = 'C:\\Path\\To\\GameFolder'  # Example: C:\PS4 Patch Builder 1.3.3\CUSA28863-patch\Image0
    csv_folder = 'C:\\Path\\To\\csv_files'  # Example: C:\DSMSPortablev1.8.5\csv files
    
    # Open a log file for writing
    with open('execution_log.txt', 'w') as log_file:
        # Prepare the command for merging CSV files with verbose flag
        merge_command = f'"{dsmsportable_path}" regulation.bin -G ER -P "{game_path}" -C'
        
        # Gather all CSV files to merge
        csv_files = []
        for filename in os.listdir(csv_folder):
            if filename.endswith(".csv"):
                csv_file_path = os.path.join(csv_folder, filename)
                csv_files.append(csv_file_path)
        
        # Check if there are CSV files to merge
        if csv_files:
            # Append all CSV file paths to the merge command
            merge_command += ' ' + ' '.join(f'"{file}"' for file in csv_files)
            merge_command += ' -V'  # Add verbose flag

            # Execute the merge command
            execute_dsmsportable(merge_command, log_file)
        else:
            log_file.write("No CSV files found to merge.\n")
            print("No CSV files found to merge.")

    # Check for the existence of regulation.bin
    regulation_file_path = os.path.join(game_path, 'regulation.bin')
    if os.path.exists(regulation_file_path):
        log_file.write("regulation.bin created successfully.\n")
    else:
        log_file.write("regulation.bin not found after merge.\n")

    # Keep the script open until the user presses Enter
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
