# Importing necessary libraries
import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog


# Creating a database connection
conn = sqlite3.connect('steam_keys.db')
c = conn.cursor()

# Creating the Steam keys table if it doesn't already exist
c.execute('''CREATE TABLE IF NOT EXISTS steam_keys
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             key TEXT NOT NULL,
             used BOOLEAN NOT NULL,
             date_used TEXT)''')

# Defining the main application window
class SteamKeyManager(tk.Tk):
    def __init__(self):
        super().__init__()

        # Setting window properties
        self.title('Steam Key Manager')
        self.geometry('800x800')
        self.resizable(True, True)

        # Adding widgets to the window
        self.add_label = tk.Label(self, text='Add a new Steam key:', font=('Arial', 12))
        self.add_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        self.name_label = tk.Label(self, text='Game name:', font=('Arial', 10))
        self.name_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')

        self.name_entry = tk.Entry(self, width=30)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)

        self.key_label = tk.Label(self, text='Game key:', font=('Arial', 10))
        self.key_label.grid(row=2, column=0, padx=10, pady=5, sticky='w')

        self.key_entry = tk.Entry(self, width=30)
        self.key_entry.grid(row=2, column=1, padx=10, pady=5)

        self.add_button = tk.Button(self, text='Add key', command=self.add_key)
        self.add_button.grid(row=3, column=1, padx=10, pady=10)

        self.edit_label = tk.Label(self, text='Edit an existing Steam key:', font=('Arial', 12))
        self.edit_label.grid(row=4, column=0, padx=10, pady=10, sticky='w')

        self.search_label = tk.Label(self, text='Search by name:', font=('Arial', 10))
        self.search_label.grid(row=5, column=0, padx=10, pady=5, sticky='w')

        self.search_entry = tk.Entry(self, width=30)
        self.search_entry.grid(row=5, column=1, padx=10, pady=5)

        self.search_button = tk.Button(self, text='Search', command=self.search_key)
        self.search_button.grid(row=5, column=2, padx=10, pady=5)

        self.edit_button = tk.Button(self, text='Edit key', command=self.edit_key, state='disabled')
        self.edit_button.grid(row=6, column=1, padx=10, pady=10)

        self.delete_button = tk.Button(self, text='Delete key', command=self.delete_key, state='disabled')
        self.delete_button.grid(row=6, column=2, padx=10, pady=10)

        self.view_all_button = tk.Button(self, text='View all keys', command=self.view_all_keys)
        self.view_all_button.grid(row=7, column=1, padx=10, pady=10)

        # Creating a listbox to display the search results
        self.results_listbox = tk.Listbox(self, width=50, height=15)
        self.results_listbox.grid(row=8, column=0, columnspan=3, padx=10, pady=10)

        # Binding the listbox to handle double-click events
        self.results_listbox.bind('<Double-Button-1>', self.select_key)

    # Function to add a key to the database
    def add_key(self):
        name = self.name_entry.get()
        key = self.key_entry.get()

        # Checking if the name and key entries are not empty
        if name and key:
            # Creating a tuple to insert into the database
            t = (name, key, 0, None)

            # Executing the INSERT query
            c.execute('INSERT INTO steam_keys (name, key, used, date_used) VALUES (?, ?, ?, ?)', t)
            conn.commit()

            # Clearing the entry fields
            self.name_entry.delete(0, tk.END)
            self.key_entry.delete(0, tk.END)

            # Showing a success message
            messagebox.showinfo('Success', 'Steam key added successfully!')
        else:
            # Showing an error message
            messagebox.showerror('Error', 'Name and key fields must not be empty!')

    # Function to search for a key in the database
    def search_key(self):
        name = self.search_entry.get()

        # Checking if the search entry is not empty
        if name:
            # Executing the SELECT query
            c.execute('SELECT * FROM steam_keys WHERE name LIKE ?', ('%' + name + '%',))
            results = c.fetchall()

            # Checking if there are any results
            if results:
                # Deleting any previous search results
                self.results_listbox.delete(0, tk.END)

                # Populating the listbox with the search results
                for row in results:
                    self.results_listbox.insert(tk.END, row)

                # Enabling the edit and delete buttons
                self.edit_button.config(state='normal')
                self.delete_button.config(state='normal')
            else:
                # Showing an error message
                messagebox.showerror('Error', 'No results found!')
        else:
            # Showing an error message
            messagebox.showerror('Error', 'Search field must not be empty!')

    # Function to edit a key in the database
    def edit_key(self):
        # Getting the selected key's ID
        key_id = self.results_listbox.get(tk.ACTIVE)[0]
        
        # Showing an input dialog to get the new key
        new_key = simpledialog.askstring('Edit key', 'Enter the new Steam key:', parent=self)
        # new_key = tk.simpledialog.askstring('Edit key', 'Enter the new Steam key:', parent=self)

        # Checking if the new key is not empty
        if new_key:
            # Creating a tuple to update the database
            t = (new_key, key_id)

            # Executing the UPDATE query
            c.execute('UPDATE steam_keys SET key = ? WHERE id = ?', t)
            conn.commit()

            # Showing a success message
            messagebox.showinfo('Success', 'Steam key updated successfully!')
        else:
            # Showing an error message
            messagebox.showerror('Error', 'Key field must not be empty!')

    # Function to delete a key from the database
    def delete_key(self):
        # Getting the selected key's ID
        key_id = self.results_listbox.get(tk.ACTIVE)[0]

        # Confirming the deletion
        if messagebox.askyesno('Confirm', 'Are you sure you want to delete this key?'):
            # Executing the DELETE query
            c.execute('DELETE FROM steam_keys WHERE id = ?', (key_id,))
            conn.commit()

            # Showing a success message
            messagebox.showinfo('Success', 'Steam key deleted successfully!')

    # Function to view all the keys in the database
    def view_all_keys(self):
        # Executing the SELECT query
        c.execute('SELECT * FROM steam_keys')
        results = c.fetchall()

        # Deleting any previous search results
        self.results_listbox.delete(0, tk.END)

        # Populating the listbox with the search results
        for row in results:
            self.results_listbox.insert(tk.END, row)

    # Function to select a key from the listbox
    def select_key(self, event):
        # Getting the selected key's ID
        key_id = self.results_listbox.get(tk.ACTIVE)[0]

        # Enabling the edit and delete buttons
        self.edit_button.config(state='normal')
        self.delete_button.config(state='normal')

if __name__ == '__main__':
    app = SteamKeyManager()
    app.mainloop()

# Closing the database connection
conn.close()