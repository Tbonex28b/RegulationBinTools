### Regulation Bin Utilities: Usage Instructions

**Note:** The CSV Extractor W.I.P may not function properly out of the box due to updates in Elden Ring or other factors. Modifications have been made to ensure compatibility with the latest version of the game. Provided all requirements are met and paths are correctly configured, this tool is fully operational. It is particularly useful for Souls games, especially FromSoftware titles, for extracting and rebuilding `regulation.bin` files. This is an ideal option if you cannot utilize DSmapStudio or Smithbox.

### Changes/Updates:
- **Import Function:** Added new functionality for easier and more intuitive importing of parameter files into the extraction process.
- **Optimization:** Enhanced performance for streamlined modifications of `regulation.bin`, making parameter management and updates significantly simpler.
- **GUI Enhancements:** With the introduction of `RegulationBinUtilities_GUI` and `Utility_Hub_GUI`, you can now more easily update `regulation.bin` and other related files through a user-friendly interface.

### Requirements:
- The provided `.rar` file named `RegulationMergeTools(version#)`.

### Steps:

1. **Install the Tool:**
   - Extract the contents of the `RegulationMergeTools` onto your PC. To simplify this process, drag and drop the `RegulationBinUtilities` folder (located inside the .rar) directly to your C Drive.

2. **Run the Installer:**
   - Inside the extracted folder, execute `install_python_and_panda.bat`. When prompted, allow the application to make changes to your device. Wait for the installation to complete successfully.

3. **Update File Paths:**
   - You no longer need separate directories, as a `gamepath.txt` is included. Manual entry of game paths is now unnecessary. Example paths:
     - `C:\RegulationBinUtilities\normal` – Place your unmodded `regulation.bin` file here.
     - `C:\RegulationBinUtilities\regulation` – Place your modded `regulation.bin` file here.

4. **Modify Param Names:**
   - The `param_names.txt` file contains commonly used parameters. You can add or remove entries as needed. Adding `:modified` at the end of a param name will restrict extraction to only those parameters with modified content in the corresponding `regulation.bin`. If there are no modifications, nothing will be extracted for that param. Omitting `:modified` will result in the entire param being extracted.

5. **Modify Param Names II:**
   - If you choose not to use `param_names.txt`, delete or remove it from the folder. The fallback script within `ExtractAndLogParams.py` (located at Line 134) will then be used. The same extraction rules apply as outlined in step 4.

6. **Prepare the Regulation Folder:**
   - Place the `regulation.bin` file you wish to extract parameters from into the `regulation` folder.

7. **Run the Extraction Script:**
   - Execute `ExtractAndLogParams.py`. This will generate a `csv_files` folder and log the extraction process.

8. **Check Extracted Params:**
   - The extracted parameters will be located in the `csv_files` folder. An `extraction_log.txt` file will also be created to log events that occurred during extraction.

9. **Run the Merge Tool:**
   - Execute `ParamMergeTool.py`. An `execution_log.txt` file will be created to document the events that transpired during the merging process.

10. **Locate the Updated File:**
    - In your `RegulationBinUtilities` folder, you will find a newly created `regulation.bin` file. This file represents your updated and merged `regulation.bin`.

11. **Completion:**
    - Congratulations! You have successfully merged `regulation.bin` files without the need for DSMapStudio or Smithbox.

### Troubleshooting

**(Only if path directories were manually changed)**  
Ensure the following paths are correctly set in the scripts:

- **ExtractAndLogParams.py**:
  Edit **lines 15, 16, and 112** to specify the correct file paths.

- **ParamMergeTool.py**:
  Edit **lines 76, 77, and 78** to set the correct file paths.

### CSV Execution Errors:

Check `execution_log.txt` for potential issues, including:

- Incorrect values.
- Wrong data types.

(While these issues are unlikely, as the script is designed to handle such errors before merging.)

### Summary/Notes/Important:
- Ensure all paths are correctly set to achieve optimal functionality.
- Monitor the extraction log for any errors or warnings.

### Credits:
- **DSMSPortable**: Developed by mountlover.
- **CSV Extractor W.I.P**: Developed by WindShadowRuins.
- **Modifications and updates**: Developed by Tbonex28b.