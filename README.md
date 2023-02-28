# Steam Key Manager 

<img src="https://i.imgur.com/sUPfwtF.png">

An open-source Python program to store and manage Steam keys. It uses an SQLite database to store the keys and a Tkinter GUI, allowing users to easily add, edit, and delete keys. This program also has a search feature that allows users to quickly find keys by searching for the game name.

### Overview
This open-source program uses a combination of Python, SQLite, and Tkinter to allow users to store and manage their Steam keys easily. The program has a graphical user interface that allows users to add, edit, and delete keys and search for keys by game name. The program also stores date-used information, enabling users to determine which keys have already been used.

### Frameworks:
[SQLite](https://www.sqlite.org/index.html) - a relational database management system. 

[Tkinter](https://docs.python.org/3/library/tkinter.html) - a GUI library for Python.

### Language: 

- [Python](https://www.python.org/)

### Flow diagrams:

### Requirements:

- Python 3.x 
- SQLite 
- Tkinter

### Modules:
- sqlite3
- tkinter

### API:

### Classes:

1. SteamKeyManager - The main class of the Steam Key Manager program. This class creates the main window and adds the necessary widgets and functions.

### Functions:

1. add_key - Adds a Steam key to the database. 
2. search_key - Searches for a Steam key in the database. 
3. edit_key - Edits an existing Steam key in the database. 
4. delete_key - Deletes a Steam key from the database. 
5. view_all_keys - Views all the Steam keys in the database.
6. select_key - Selects a Steam key from the listbox.

### Procedure:

1. Download and install Python 3.x. 
2. Install the necessary modules. 
3. Create a SQLite database to store the Steam keys. 
4. Create the Steam keys table in the database. 
5. Create the main application window. 
6. Create the necessary widgets and functions. 
7. Run the program and add, edit, and delete Steam keys as necessary.
