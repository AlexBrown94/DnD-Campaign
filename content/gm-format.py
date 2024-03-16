import os
import re
import logging

def preprocess_markdown(file_content):
    # Remove content between BEGIN HIDDEN and END HIDDEN markers
    return re.sub(r'<!-- BEGIN HIDDEN -->.*?<!-- END HIDDEN -->', '', file_content, flags=re.DOTALL)

def process_directory(directory):
    # Iterate over files and directories in the current directory
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.md'):
                file_path = os.path.join(root, filename)
                print(f'Processing {file_path}')
                # Read original Markdown file
                with open(file_path, 'r') as file:
                    markdown_content = file.read()

                # Preprocess Markdown content
                processed_content = preprocess_markdown(markdown_content)

                # Write processed Markdown content back to the file
                with open(file_path, 'w') as file:
                    file.write(processed_content)

if __name__ == "__main__":
    logger = logging.getLogger()
    directory_path = "C:/Users/alexd/Git/quartz/content"  # Set your directory path here
    process_directory(directory_path)