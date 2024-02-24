import os
import shutil

def copy_ebook_files(src_directory, dst_directory, ebook_formats):
    # Make sure destination directory exists, if not, create it
    if not os.path.exists(dst_directory):
        os.makedirs(dst_directory)

    # Walk through the source directory
    for root, dirs, files in os.walk(src_directory):
        for file in files:
            if file.lower().endswith(ebook_formats):
                # Get the path to the source file
                src_file = os.path.join(root, file)
                # Define the path to the new destination file
                dst_file = os.path.join(dst_directory, file)
                
                # Make sure the destination path is unique if the file already exists
                if os.path.exists(dst_file):
                    filename, file_extension = os.path.splitext(file)
                    i = 1
                    # Append a number to the file's name if a duplicate exists
                    new_dst_file_name = f"{filename}_{i}{file_extension}"
                    new_dst_file_path = os.path.join(dst_directory, new_dst_file_name)
                    while os.path.exists(new_dst_file_path):
                        i += 1
                        new_dst_file_name = f"{filename}_{i}{file_extension}"
                        new_dst_file_path = os.path.join(dst_directory, new_dst_file_name)
                    dst_file = new_dst_file_path
                
                # Copy each file
                shutil.copy2(src_file, dst_file)
                print(f"Copied: {src_file} to {dst_file}")

# User input for source and destination directories
src_directory_input = input("Enter the path of the source directory: ")
dst_directory_input = input("Enter the path of the destination directory: ")

# Define a tuple with ebook formats
ebook_formats = ('.epub', '.mobi', '.pdf', '.azw')

copy_ebook_files(src_directory_input, dst_directory_input, ebook_formats)

print("Ebook files have been copied successfully.")
