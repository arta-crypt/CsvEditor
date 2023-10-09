import tkinter as tk
import pandas as pd
import csv
from tkinter import ttk
from tkinter import filedialog
from design_pattern.command_pattern.command import Command
from viewmodel.file_control_viewmodel import FileControlViewModel


class _SetDataCommand(Command):
    def __init__(self,
                 data: pd.DataFrame,
                 receiver: FileControlViewModel) -> None:
        self.data = data
        self.receiver = receiver

    def execute(self):
        self.receiver.set_data(data=self.data)

    def unexecute(self):
        pass


class FileControlFrame(ttk.Frame):
    PATH_LABEL_TEXT = 'File path'
    OPEN_BUTTON_TEXT = '...'
    OPEN_BUTTON_WIDTH = 2
    READ_BUTTON_TEXT = 'Read'
    PATH_ENTRY_WIDTH = 100

    def __init__(self,
                 master,
                 viewmodel: FileControlViewModel) -> None:
        super().__init__(master=master)
        self._viewmodel = viewmodel
        self._file_path = tk.StringVar()
        self._dialect = csv.excel()
        self._dialect.delimiter = ','
        self._encoding = 'utf-8_sig'
        self.create_widget()

    def create_widget(self) -> None:
        path_label = ttk.Label(master=self,
                               text=FileControlFrame.PATH_LABEL_TEXT)
        open_button = ttk.Button(master=self,
                                 text=FileControlFrame.OPEN_BUTTON_TEXT,
                                 width=FileControlFrame.OPEN_BUTTON_WIDTH,
                                 command=self.open_file_dialog)
        read_button = ttk.Button(master=self,
                                 text=FileControlFrame.READ_BUTTON_TEXT,
                                 command=self.read_file)
        path_entry = ttk.Entry(master=self,
                               textvariable=self._file_path,
                               width=FileControlFrame.PATH_ENTRY_WIDTH)
        x_scrollbar = ttk.Scrollbar(master=self,
                                    orient=tk.HORIZONTAL,
                                    command=path_entry.xview)
        # Config
        path_entry.configure(xscrollcommand=x_scrollbar.set)
        # Pack
        path_label.grid(column=0, row=0)
        path_entry.grid(column=1, row=0)
        x_scrollbar.grid(column=1, row=1, sticky=tk.EW)
        open_button.grid(column=2, row=0)
        read_button.grid(column=3, row=0)
        self.pack(anchor=tk.CENTER)

    def open_file_dialog(self,
                         inital_dir: str = R'E:\Users\w8-ki\Downloads\1_seiseki',
                         file_types: list = [('csv', '*.csv')]) -> None:
        file_path = filedialog.askopenfilename(initialdir=inital_dir,
                                               filetypes=file_types)
        self._file_path.set(file_path)

    def read_file(self) -> None:
        data = self.read_file_core()
        if not data is None:
            _SetDataCommand(data=data,
                            receiver=self._viewmodel).execute()
        else:
            pass

    def read_file_core(self) -> pd.DataFrame | None:
        data: pd.DataFrame = None
        file_path = self._file_path.get()
        print(file_path)
        try:
            data = pd.read_csv(filepath_or_buffer=file_path,
                               header=0,
                               dialect=self._dialect,
                               encoding=self._encoding,
                               skip_blank_lines=True,
                               dtype=str)
        except IOError as e:
            print(e)
            ret = False
        except Exception as e:
            print(e)
            ret = False
        return data
