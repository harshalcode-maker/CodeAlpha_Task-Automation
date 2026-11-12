📁 JPG File Organizer Using Python
📌 Project Overview
The JPG File Organizer is a simple Python automation project that
moves all .jpg image files from a source folder into a destination
folder.

The program checks the source folder, identifies JPG files, creates the
destination folder if it does not already exist, and moves the matching
images automatically. It also displays the number of files moved.
🎯 Project Objectives
- Automate the repetitive task of organizing JPG images.
- Identify JPG files in a specified folder.
- Create a destination folder automatically when needed.
- Move JPG files using Python.
- Display a summary of the files moved.
✨ Features
- Automatically scans the source folder.
- Detects files with the .jpg extension (case-insensitive).
- Creates the destination folder if it does not exist.
- Moves JPG files from the source folder to the destination folder.
- Displays each moved filename.
- Shows the total number of JPG files moved.
- Requires no external Python packages.
🛠️ Technologies and Concepts Used
- Programming Language: Python 3
- Modules: os, shutil
- Concepts: File handling, folders and paths, loops, conditional
  statements, string methods, and automation.
📂 Project Structure
Create the following folder structure:
JPG-File-Organizer/
│
├── file_organizer.py
├── MyImages/
│   ├── photo1.jpg
│   ├── photo2.jpg
│   └── document.pdf
└── JPG_Images/
MyImages is the source folder. Put the images you want to organize
inside it.

JPG_Images is the destination folder. The program creates it
automatically if it does not exist.

Important: Keep file_organizer.py and the MyImages folder in the
same working directory when using the relative folder paths in the
script.
⚙️ Requirements
- Python 3.x
- Visual Studio Code or another Python editor (recommended)
- No external libraries required. os and shutil are included with
  Python.
🚀 How to Run the Project
1. Create a project folder named JPG-File-Organizer.
2. Inside it, create a folder named MyImages.
3. Add one or more .jpg images to MyImages.
4. Save the Python program as file_organizer.py in the project
   folder.
5. Open the project folder in Visual Studio Code.
6. Open the terminal in that folder and run:
python file_organizer.py
After the program finishes, check the JPG_Images folder for the moved
images.
🖥️ Sample Output
If MyImages contains photo1.jpg, photo2.jpg, and document.pdf,
the output will look like:
Destination folder created!
Moved: photo1.jpg
Moved: photo2.jpg

================================
       JPG FILE ORGANIZER
================================
Total JPG files moved: 2
Automation completed successfully!
The PDF file is not moved because the program only selects files ending
in .jpg (case-insensitive).
🔍 How the Program Works
1. Set folder names: source_folder identifies MyImages, and
   destination_folder identifies JPG_Images.
2. Create destination: os.path.exists() checks whether the
   destination folder exists. If not, os.makedirs() creates it.
3. Scan source folder: os.listdir() gets the names of entries in
   the source folder.
4. Filter JPG files: filename.lower().endswith(".jpg") checks the
   file extension without being affected by uppercase or lowercase
   letters.
5. Build paths: os.path.join() creates the source and destination
   paths.
6. Move files: shutil.move() moves each matching file.
7. Count and report: The program increments moved_count and
   prints the total after processing.
📚 Key Python Functions
  Function             Purpose
  os.path.exists()   Checks whether a folder or path exists
os.makedirs()      Creates the destination folder
os.listdir()       Lists entries in the source folder
os.path.join()     Builds file paths safely
str.lower()        Makes extension matching case-insensitive
str.endswith()     Checks whether a filename ends with .jpg
shutil.move()      Moves a file to the destination
⚠️ Notes and Limitations
- The source folder MyImages must exist before running the script.
  Otherwise, Python raises a FileNotFoundError.
- The script moves .jpg files only; it does not move .jpeg or
  other image formats.
- If a file with the same name already exists in the destination
  folder, check the behavior before running the script because moving
  files with duplicate names can cause a conflict.
- The script scans entries returned by os.listdir() and is intended
  for a folder containing image files, not nested folders.
🔮 Possible Future Enhancements
- Support .jpeg, .png, and other image formats.
- Organize images into folders by date or file type.
- Add error handling for missing source folders and file conflicts.
- Allow users to enter source and destination folder paths.
- Generate a log file containing the names of moved files.
- Add a graphical user interface.
🎓 Learning Outcomes
By completing this project, I learned how to:
- Use Python's os module to work with folders and file paths.
- Use shutil.move() to move files.
- Filter filenames by extension.
- Automate a repetitive file-management task.
- Use loops and conditional statements to process multiple files.

Project: JPG File Organizer Using Python
⭐ If you find this project useful, feel free to star the repository!
