# Evernote Tag Renamer

## Overview
This Python script automates the process of renaming tags in Evernote using PyAutoGUI. It is particularly useful when you have a large number of tags to rename and want to save time by automating the process. Naturally, an easier way to do this would be to use authentication tokens or something, but this method also worked for my use case, so why not.

## Prerequisites
Before running the script, make sure you have the following dependencies installed:
- Python 3.x
- PyAutoGUI
- Pyperclip


(You can install them using pip)


## Usage
1. Run the script in a Python environment.
2. Ensure that Evernote is open and positioned correctly on the screen.
3. The script will automatically start renaming tags. You can interrupt the process at any time by pressing the 'esc' key.
4. By default, the script renames tags every 15 seconds. You can adjust this interval as needed.
5. The script will pause automatically after renaming 350 tags. You can modify this limit if necessary.

## Important Notes
- Ensure that Evernote is in focus and positioned correctly on the screen before running the script.
- Make sure to review and customize the script according to your specific requirements before running it.
- Use caution when running automation scripts, as they can potentially cause unintended actions or errors.

## License
This project is licensed under the [MIT License]((https://opensource.org/license/mit)https://opensource.org/license/mit).
