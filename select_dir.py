### Prompt user to select directories to go through looking for movie-type files.

from tkinter import Tk
from tkinter.filedialog import askdirectory

def add_folder():
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askdirectory() # show an "Open" dialog box and return the path to the selected file

    with open("files/selected_directories.txt", 'w+') as file:
        content = file.readlines()
        if not filename in content:
            file.seek(0)
            file.write(f"{filename}\n")