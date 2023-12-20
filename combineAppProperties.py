import os

# File paths and their respective headings
file_info = [
    ("ignite\\pom.xml", "1.1. ignite\\pom.xml", "xml"),
    ("ignite-api\\pom.xml", "1.2. ignite-api\\pom.xml", "xml"),
    ("ignite-library\\pom.xml", "1.3. ignite-library\\pom.xml", "xml"),
    ("ignite\\src\\main\\resources\\application.local.properties", "2.1. ignite\\src\\main\\resources\\application.local.properties", "conf"),
    ("ignite-api\\src\\main\\resources\\application.local.properties", "2.2. ignite-api\\src\\main\\resources\\application.local.properties", "conf"),
    ("ignite\\src\\main\\java\\net\\integrategroup\\ignite\\security\\WebSecurityConfig.java", "3.1. ignite\\src\\main\\java\\net\\integrategroup\\ignite\\security\\WebSecurityConfig.java", "java"),
    ("ignite-api\\src\\main\\java\\net\\integrategroup\\ignite\\security\\ApiSecurityConfig.java", "3.2. ignite-api\\src\\main\\java\\net\\integrategroup\\ignite\\security\\ApiSecurityConfig.java", "java")
]

# Function to read file content
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"File not found: {file_path}"

# Function to write combined content to a file
def write_combined_file(combined_content, output_file):
    with open(output_file, 'w') as file:
        file.write(combined_content)

# Main function to combine files
def combine_files(file_info, output_file="combinedAppProperties.md"):
    combined_content = "# Application Properties\n\nThe application has multiple sub-projects\n\n"
    for file_path, heading, code_type in file_info:
        combined_content += f"## {heading}\n\n```{code_type}\n\n{read_file(file_path)}\n```\n\n"
    write_combined_file(combined_content, output_file)

# Combine the files
combine_files(file_info)