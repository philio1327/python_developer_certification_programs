import os
import shutil
from datetime import datetime

# Path to your Downloads directory
downloads_dir = "Downloads"

# List all files in the Downloads directory
files = os.listdir(downloads_dir)

# Iterate over each file in the Downloads folder
for file in files:
    file_path = os.path.join(downloads_dir, file)

    # Get the modification time of the file
    modified_time = os.path.getmtime(file_path)

    # Convert the modification time to a datetime object
    date = datetime.fromtimestamp(modified_time)
    year = date.year
    month = date.strftime("%B")

    # Print each file and their modification dates (for testing purposes)
    print(f"File: {file}, Modified: {month} {year}")

    # Create the directory path for the year and month
    directory_year = f"{year}"
    directory_month = f"{month}"

    directory_year_path = os.path.join(downloads_dir, directory_year)
    directory_month_path = os.path.join(directory_year_path, directory_month)

    # Create the directory if it doesn't exist
    os.makedirs(directory_year_path, exist_ok=True)
    os.makedirs(directory_month_path, exist_ok=True)

    # Move the file to the new directory
    shutil.move(file_path, directory_month_path)

    # Print a confirmation message
    print(f"Moved '{file}' to {directory_month_path}")


