# Calibre Library Export Script

This Python script is designed to assist users in exporting their ebook collections from a Calibre library to another folder. It's a straightforward and efficient tool for backing up, transferring, or simply reorganizing your ebook files.

## Features

- **Support for Multiple Formats**: The script currently supports `.epub`, `.mobi`, `.pdf`, and `.azw` files, which covers most of the ebooks managed by Calibre.
- **Duplicate Handling**: If an ebook file with the same name already exists in the destination directory, the script will automatically rename the file to avoid overwriting it.
- **Recursive Search**: The script will search through all subdirectories of the provided source directory to find ebook files.
- **User-Friendly**: The script prompts for source and destination directories, making it easy for those with little technical knowledge to use.

## Prerequisites

To run this script, you will need:

- Python installed on your system.
- Access to the command-line interface (CLI) or terminal on your computer.

## Installation

1. Clone the repository or download the script file to your local machine.
2. Open your terminal or command-line interface.
3. Navigate to the directory where the script is located.

## Usage

1. Run the script using your Python interpreter:

    ```bash
    python calibre_export.py
    ```

2. When prompted, enter the full path of your Calibre library's source directory.
3. When prompted, enter the full path to the destination directory where you want the ebooks to be copied.

The script will then start processing your files, copying them from the source to the destination. Any duplicate files will be automatically renamed.

## Example

```
Enter the path of the source directory: /Users/yourusername/Calibre Library
Enter the path of the destination directory: /Users/yourusername/Documents/Ebook_Backup
```

After you've entered the paths, the script will begin copying the ebook files, and you will see printed messages in the CLI for each file that is successfully copied.
