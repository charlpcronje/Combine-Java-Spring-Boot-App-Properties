# Combine App Properties Explained

## Overview
This Python script is designed to read content from a series of specified files and combine this content into a single markdown file. It is particularly useful for consolidating configuration files or code files from different parts of a project into one document for easier viewing and sharing.

## Script Structure
The script consists of several parts: variable initialization, function definitions, and a main execution block.

### 1. Variable Initialization: `file_info`
- The `file_info` variable is a list of tuples. Each tuple contains three elements:
  1. The relative path to the file (`file_path`).
  2. A heading that will be used in the combined markdown file (`heading`).
  3. The type of code or configuration file (`code_type`) which will be used for syntax highlighting in the markdown.

### 2. Function Definitions
There are two function definitions in the script:

#### 2.1. `read_file(file_path)`
- Purpose: To read and return the content of a file specified by `file_path`.
- Parameters: `file_path` - a string representing the path to the file.
- Process:
  - Tries to open the file in read mode.
  - If the file is found, its content is returned.
  - If the file is not found, a "File not found" message is returned.

#### 2.2. `write_combined_file(combined_content, output_file)`
- Purpose: To write the combined content into a markdown file.
- Parameters:
  - `combined_content` - a string containing the combined content of all files.
  - `output_file` - a string specifying the path of the output file.
- Process: Writes `combined_content` to the file specified by `output_file`.

### 3. Main Function: `combine_files(file_info, output_file="combinedAppProperties.md")`
- Purpose: To combine the contents of various files into a single markdown file.
- Parameters:
  - `file_info` - a list of tuples containing file paths, headings, and code types.
  - `output_file` (optional) - the name of the output file. Default is "combinedAppProperties.md".
- Process:
  - Starts with a predefined string as the initial content.
  - Iterates over each tuple in `file_info`.
  - For each file, it adds a markdown heading and the file content (obtained using `read_file`) in a code block formatted for the appropriate code type.
  - Calls `write_combined_file` to write the combined content to the output file.

### 4. Main Script Execution
- Calls the `combine_files` function with the `file_info` list to execute the file combination process.

## Usage
The script can be used to combine content from different files (like configuration files, XML files, and Java source files) into a single markdown file. This is particularly helpful in documentation and review processes where multiple files need to be consolidated for easier access.

