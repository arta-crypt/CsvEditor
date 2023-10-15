import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
from injector import inject, Module, singleton


class Model:
    def __init__(self):
        self.data = None
        self.observers = []

    def load_csv(self, file_path):
        self.data = pd.read_csv(file_path)
        self.notify_observers()

    def save_csv(self, file_path):
        if self.data is not None:
            self.data.to_csv(file_path, index=False)

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer()


class IModel:
    def load_csv(self, file_path):
        pass

    def save_csv(self, file_path):
        pass

    def register_observer(self, observer):
        pass

    def notify_observers(self):
        pass


class ViewModel:
    @inject
    def __init__(self, model: IModel):
        self.model = model
        self.file_path = ""

    def load_csv(self):
        self.file_path = filedialog.askopenfilename(
            filetypes=[("CSV files", "*.csv")])
        if self.file_path:
            self.model.load_csv(self.file_path)

    def save_csv(self):
        if self.file_path:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
            if file_path:
                self.model.save_csv(file_path)

    def register_observer(self, observer):
        self.model.register_observer(observer)

    def notify_observers(self):
        self.model.notify_observers()


class View:
    @inject
    def __init__(self, root: tk.Tk, view_model: ViewModel):
        self.root = root
        self.viewModel = view_model
        self.create_widgets()

    def create_widgets(self):
        self.load_button = ttk.Button(
            self.root, text="Load CSV", command=self.viewModel.load_csv)
        self.load_button.pack(pady=10)

        self.save_button = ttk.Button(
            self.root, text="Save CSV", command=self.viewModel.save_csv)
        self.save_button.pack(pady=10)

        self.textbox = tk.Text(self.root, height=10, width=40)
        self.textbox.pack(padx=10, pady=10)

        self.viewModel.register_observer(self.update_textbox)

    def update_textbox(self):
        if self.viewModel.model.data is not None:
            self.textbox.delete(1.0, tk.END)
            self.textbox.insert(tk.END, str(self.viewModel.model.data))


class AppModule(Module):
    def configure(self, binder):
        binder.bind(IModel, to=Model, scope=singleton)
        binder.bind(ViewModel, to=ViewModel, scope=singleton)
        binder.bind(View, to=View, scope=singleton)


if __name__ == "__main__":
    from injector import Injector
    injector = Injector(AppModule())
    view = injector.get(View)

    # root = tk.Tk()
    view.root.title("CSV File Processor")

    # view = View(root, ViewModel(IModel()))

    # root.mainloop()

    view.root.mainloop()
