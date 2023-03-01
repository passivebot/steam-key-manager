# Steam Key Manager 

<img src="https://i.imgur.com/TWa2onv.png">

An open-source Python program to store and manage Steam keys. It uses an SQLite database to store the keys and a Tkinter GUI, allowing users to easily add, edit, and delete keys. This program also has a search feature that allows users to quickly find keys by searching for the game name.

### Overview
This open-source program uses a combination of Python, SQLite, and Tkinter to allow users to store and manage their Steam keys easily. The program has a graphical user interface that allows users to add, edit, and delete keys and search for keys by game name. The program also stores date-used information, enabling users to determine which keys have already been used.

### Frameworks:
[SQLite](https://www.sqlite.org/index.html) - a relational database management system. 

[Tkinter](https://docs.python.org/3/library/tkinter.html) - a GUI library for Python.

### Language: 

- [Python](https://www.python.org/)

### Flow diagrams:

This is a Python script that creates a GUI application for managing Steam keys using the Tkinter library. The application allows users to add new keys, search for existing keys by name, edit and delete keys, and view all keys in the database.

The script starts by importing the necessary libraries, including sqlite3 and Tkinter. It then creates a connection to a SQLite database and creates a table for storing the Steam keys if it doesn't already exist.

The main application window is defined as a class called SteamKeyManager which inherits from tk.Tk. In the __init__ method of the class, the window properties are set, widgets are added to the window, and event bindings are defined.

The add_key method adds a new key to the database when the user clicks the "Add key" button. The method retrieves the values entered in the name and key fields, checks that they are not empty, creates a tuple with the values, and executes an INSERT query to insert the tuple into the database. If the insertion is successful, a success message is shown, and the entry fields are cleared. If either of the fields is empty, an error message is shown.

The search_key method searches for keys in the database based on the name entered in the search field when the user clicks the "Search" button. The method retrieves the search query, executes a SELECT query with a LIKE clause to find all rows where the name column contains the search query, fetches all the results into a list, and populates the results_listbox with the results. If no results are found, an error message is shown. If the search field is empty, nothing happens.

Other methods include edit_key, which allows the user to edit an existing key, delete_key, which allows the user to delete an existing key, and view_all_keys, which allows the user to view all keys in the database.

Overall, this script provides a simple GUI application for managing Steam keys and can be further extended to include additional functionality.

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
