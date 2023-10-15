import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.font import Font
import pandas as pd


class Model:
    def __init__(self):
        self.df = None


class ViewModel:
    def __init__(self, model):
        self.model = model

    def load_csv(self, file_path):
        # Specify dtype=str to read all data as strings
        self.model.df = pd.read_csv(file_path, dtype=str)

    def save_csv(self, file_path):
        self.model.df.to_csv(file_path, index=False)

    def update_row(self, row_index, updated_values):
        # Check if the DataFrame is available and the row index is valid
        if self.model.df is not None and row_index >= 0 and row_index < len(self.model.df):
            # Update the specified row with the updated values
            self.model.df.iloc[row_index, :] = updated_values


class View:
    def __init__(self, root, vm):
        self.root = root
        self.vm = vm
        self.setup_ui()

    def setup_ui(self):
        self.root.title("CSV Editor")
        self.root.geometry("800x400")  # Set initial window size

        # Load CSV button
        load_button = ttk.Button(
            self.root, text="Load CSV", command=self.load_csv)
        load_button.pack()

        # TreeView to display CSV data
        self.tree = ttk.Treeview(self.root)
        self.tree.pack(expand=True, fill='both')

        # Bind a function to item selection
        self.tree.bind("<<TreeviewSelect>>", self.show_selected_data)

        # Textbox for selected row data
        self.selected_data_textbox = tk.Text(self.root, height=5, width=30)
        self.selected_data_textbox.pack()

        # Update button
        update_button = ttk.Button(
            self.root, text="Update", command=self.update_data)
        update_button.pack()

        # Save CSV button
        save_button = ttk.Button(
            self.root, text="Save CSV", command=self.save_csv)
        save_button.pack()

        # Disable resizing of the window
        self.root.resizable(False, False)

    def load_csv(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.vm.load_csv(file_path)
            self.display_data()

    def display_data(self):
        self.tree.delete(*self.tree.get_children())
        if self.vm.model.df is not None:
            # Insert data into Treeview
            columns = self.vm.model.df.columns.tolist()
            self.tree["columns"] = columns
            for idx, row in self.vm.model.df.iterrows():
                values = row.tolist()  # Convert all values to string
                self.tree.insert("", "end", iid=idx,
                                 text=str(idx), values=values)

            # Set headers from CSV file
            for col in columns:
                if col == "index":
                    # Set a specific width for the 'index' column
                    self.tree.column(col, width=50)
                else:
                    self.tree.heading(col, text=col)

            # Adjust column widths based on content
            for col in columns:
                if col != "index":
                    # Adjust width based on the maximum length of the content in the column
                    self.tree.column(col, width=Font().measure(
                        max(str(val) for val in self.vm.model.df[col])) + 20)

            # Reduce the width of the 'index' column
            # Adjust the width of the 'index' column to be narrower
            self.tree.column("#0", width=50)

    def show_selected_data(self, event):
        selected_items = self.tree.selection()
        if selected_items:
            item = selected_items[0]
            item_values = self.tree.item(item, "values")
            self.selected_data_textbox.delete("1.0", tk.END)
            # Convert the values to a comma-separated string
            selected_data_str = ', '.join(str(value) for value in item_values)
            self.selected_data_textbox.insert(tk.END, selected_data_str)

    def update_data(self):
        selected_items = self.tree.selection()
        if selected_items:
            selected_row = int(selected_items[0])
            updated_data = self.selected_data_textbox.get(
                "1.0", tk.END).strip()
            updated_values = updated_data.split(",")
            # Update the ViewModel with the updated values
            self.vm.update_row(selected_row, updated_values)
            self.display_data()

    def save_csv(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                                 filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.vm.save_csv(file_path)


if __name__ == "__main__":
    root = tk.Tk()

    model = Model()
    vm = ViewModel(model)
    view = View(root, vm)

    root.mainloop()
