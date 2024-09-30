### Regulation Bin Utilities: Usage Instructions

**Note:** The CSV Extractor W.I.P may not function properly out of the box due to updates in Elden Ring or other factors. Modifications have been made to ensure compatibility with the latest version of the game. Provided all requirements are met and paths are correct, this tool is now fully operational. It is particularly useful for Souls games, especially FromSoftware titles, for extracting and rebuilding `regulation.bin` files. Use this if you cannot utilize DSmapStudio or Smithbox.

### Changes/Updates:
- **Import Function:** New functionality for easier import of parameter files into the extraction process.
- **Optimization:** Enhanced for streamlined modifications of `regulation.bin`, simplifying parameter management and updates.

### Requirements:
- The provided .rar file named `RegulationMergeToolsv1.0`.

### Steps:

1. **Install the Tool:**
   - Extract the contents of `RegulationMergeToolsv1.0` onto your PC. To make this easier, simply drag and drop the `RegulationBinUtilities` folder (inside the .rar) to your C Drive.

2. **Run the Installer:**
   - Inside the extracted folder, run `install_python_and_panda.bat`. When prompted, allow the app to make changes to your device. Wait for the installation to complete.

3. **Update File Paths:**
   - You no longer need separate directories, and a `gamepath.txt` is included, so manual game path entry won't be required. Example paths:
     - `C:\RegulationBinUtilities\normal` – Place your unmodded regulation.bin here.
     - `C:\RegulationBinUtilities\regulation` – Place your modded regulation.bin here.

4. **Modify Param Names:**
   - The `param_names.txt` file includes commonly used parameters. You can add or remove entries as necessary. Adding `:modified` at the end of a param name will only extract data if modified content exists in the corresponding `regulation.bin`. If not, nothing will be extracted for that param. Without `:modified`, the entire param will be extracted.

5. **Modify Param Names II:**
   - If you do not wish to use `param_names.txt`, delete or remove it from the folder. The fallback script inside `ExtractAndLogParams.py` will be used instead (located at Line 99). The same rule applies as in step 4.

6. **Prepare the Regulation Folder:**
   - Place the `regulation.bin` file you wish to extract parameters from into the `regulation` folder.

7. **Run the Extraction Script:**
   - Execute `ExtractAndLogParams.py`. This will create a `csv_files` folder and log the process.

8. **Check Extracted Params:**
   - The extracted parameters will be located in the `csv_files` folder. An `extraction_log.txt` file will also be created to log the events during extraction.

9. **Run the Merge Tool:**
   - Execute `ParamMergeTool.py`. An `execution_log.txt` file will also be created to log the events during merging.

10. **Locate the Updated File:**
    - In your `RegulationBinUtilities` folder, you will find a newly created `regulation.bin` file. This is your updated and merged `regulation.bin`.

11. **Completion:**
    - Congratulations! You have successfully merged `regulation.bin` files without using DSMapStudio or Smithbox.

### Troubleshooting

**(Only if path directories were manually changed)**  
Ensure the following paths are correctly set in the scripts:

- **ExtractAndLogParams.py**:
  Edit **lines 14, 15, and 82** for file paths.

- **ParamMergeTool.py**:
  Edit **lines 76, 77, and 78** for file paths.

### CSV Execution Errors:

Check `execution_log.txt` for potential issues, such as:

- Incorrect values
- Wrong data types

(Although this is unlikely, as the script is designed to fix such issues before merging.) 

### Summary/Notes/Important:
- Ensure all paths are correctly set for optimal functionality.
- Monitor the extraction log for any issues.

### Credits:
- **DSMSPortable**: Developed by mountlover.
- **CSV Extractor W.I.P**: Developed by WindShadowRuins.
- **Modifications and updates**: Developed by Tbonex28b.
