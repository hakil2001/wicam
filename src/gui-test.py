import tkinter as tk
from tkinter import ttk
def on_connect_click():
    ip_address_value = ip_address_entry.get()
    bus_id_value = bus_id_entry.get()

    # Add your connection logic here
    # For now, let's just print the values
    print(f"Connecting with IP Address: {ip_address_value}, Bus ID: {bus_id_value}")


    # For demonstration purposes, add data to the Treeview
    tree.insert("", "end", values=(ip_address_value, bus_id_value, "Connected"))

    # Switch to the second screen (Tree View)
    notebook.select(1)

# Create the main window
root = tk.Tk()
root.title("WebCAM")
root.geometry("500x200")

root.iconbitmap(r'C:\Users\ADMIN-PC\Desktop\GUI\icon.ico')

# Create a notebook (tabs)
notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True)

# First screen (Connect)
connect_frame = ttk.Frame(notebook)
notebook.add(connect_frame, text="Connect")

# Widgets for the Connect screen
ip_address_label = tk.Label(connect_frame, text="IP Address:", bg="#f0f0f0")
ip_address_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

ip_address_entry = tk.Entry(connect_frame)
ip_address_entry.grid(row=0, column=1, padx=10, pady=10)

bus_id_label = tk.Label(connect_frame, text="Bus ID:", bg="#f0f0f0")
bus_id_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

bus_id_entry = tk.Entry(connect_frame)
bus_id_entry.grid(row=1, column=1, padx=10, pady=10)

connect_button = tk.Button(connect_frame, text="Connect",bg="#90EE90", command=on_connect_click)
connect_button.grid(row=2, column=0, columnspan=2, pady=10)

# Second screen (Tree View)
tree_frame = ttk.Frame(notebook)
notebook.add(tree_frame, text="Tree View")
# Add Treeview for connected device info
columns = ("IP Address", "Bus ID", "Status")
tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=5)
for col in columns:
    tree.heading(col, text=col, anchor="w", command=lambda c=col: sort_treeview(tree, c, False))
    tree.column(col, width=80, minwidth=80, anchor="w")
tree.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Add scrollbar to Treeview
tree_scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=tree_scrollbar.set)
tree_scrollbar.grid(row=0, column=1, sticky="ns")

# Configure row and column weights for resizing
tree_frame.grid_rowconfigure(0, weight=1)
tree_frame.grid_columnconfigure(0, weight=1)
# Start the GUI event loop
root.mainloop()
