import os

# Define a function to search for files with a given extension and write their paths to a file
def find_files_by_extension(directory, extension, output_file):
    with open(output_file, "w") as f:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(extension):
                    file_path = os.path.join(root, file)
                    f.write(file_path + "\n")

# Prompt user for file extension to search for
extension = input("Enter file extension to search for (e.g. '.txt', '.pdf', '.docx'): ")

# Prompt user for drive to search
drive = input("Enter the drive to search (e.g. 'C:', 'D:', etc.): ")

# Set the directory to search for files with the given extension on the specified drive (change as needed)
directory_to_search = os.path.join(drive, "\\")

# Set the output file name and path to be in the same directory as the script (change as needed)
script_dir = os.path.dirname(os.path.realpath(__file__))
output_file_name = f"files_with_{extension}_extension.txt"
output_file_path = os.path.join(script_dir, output_file_name)

# Call the find_files_by_extension function
find_files_by_extension(directory_to_search, extension, output_file_path)

# Print a message indicating where the output file was written
print(f"Output written to {output_file_path}")
