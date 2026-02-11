#rename backup_notes.txt to final_notes.txt
import os
try:
    os.rename("C:\\Users\\sahuk\\OneDrive\\Desktop\\Complete Python from Scratch\\chapter 8\\backup_notes.txt", 
              "C:\\Users\\sahuk\\OneDrive\\Desktop\\Complete Python from Scratch\\chapter 8\\Final_notes.txt")
    print("FILE RENAMED SUCCESSFULLY from backup_notes.txt to Final_notes.txt")
except FileNotFoundError:
    print("The file backup_notes.txt does not exist.")
except PermissionError:
    print("Permission denied to rename the file.")