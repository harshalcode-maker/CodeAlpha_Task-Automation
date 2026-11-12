
import os
import shutil

# Source and destination folders
source_folder = "MyImages"
destination_folder = "JPG_Images"

# Create destination folder if it does not exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
    print("Destination folder created!")

# Count moved files
moved_count = 0

# Read all files from source folder
for filename in os.listdir(source_folder):

    # Check whether file is a JPG image
    if filename.lower().endswith(".jpg"):

        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)

        # Move JPG file
        shutil.move(source_path, destination_path)

        print("Moved:", filename)
        moved_count += 1

# Display final result
print("\n================================")
print("       JPG FILE ORGANIZER")
print("================================")

print("Total JPG files moved:", moved_count)

print("Automation completed successfully!")
